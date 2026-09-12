# 3B 규모 유사 LLM: 데이터 생성 → 학습 → 추론 (MacBook Pro M4용, 현실적 기본값 포함)
# 사용법: 이 파일을 Jupyter 노트북(.ipynb)으로 불러와 셀 단위로 실행
# 요약: 실제 3B 파라미터 모델을 M4에서 완전 학습하는 것은 비현실적임. 대신 여기서는
# 1) 합성 데이터 생성
# 2) 가변 크기(디폴트는 소형) Transformer 모델 구성
# 3) 학습(작은 scale로 빠르게 데모 가능)
# 4) 저장 및 간단 추론
# 필요 라이브러리: transformers, datasets, accelerate, tokenizers, torch

# ---------------------------
# 0) 환경 준비 (터미널에서 한 번만 실행)
# ---------------------------
# pip install --upgrade pip
# pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/nightly/cpu
# pip install transformers datasets accelerate tokenizers evaluate
# (MPS 가속 사용 시 설치된 PyTorch가 MPS 지원 빌드인지 확인)

# ---------------------------
# 1) 설정
# ---------------------------
import os
from dataclasses import dataclass

import math
import random
import torch
from transformers import (
    AutoTokenizer,
    GPT2Config,
    AutoModelForCausalLM,
    TrainingArguments,
    Trainer,
    DataCollatorForLanguageModeling,
)
from datasets import Dataset

# 사용자 설정: 아래 값을 바꿔서 실험
@dataclass
class Config:
    model_name: str = None  # pretrained 사용할 경우 경로/이름
    target_param_scale: str = "demo"  # 'demo' (작게), '3b' (설명용 - 실제 학습 권장하지 않음)
    seq_len: int = 128
    vocab_size: int = 50257
    train_samples: int = 2000
    val_samples: int = 200
    epochs: int = 2
    batch_size: int = 4
    learning_rate: float = 5e-5
    output_dir: str = "output-llm"

cfg = Config()

# 디바이스 설정: MPS 우선, 없으면 CPU
if torch.backends.mps.is_available():
    device = torch.device("mps")
else:
    device = torch.device("cpu")
print(f"사용 디바이스: {device}")

# ---------------------------
# 2) 모델 구성 (크기 선택)
# ---------------------------
# 현실적으로 M4에서 "진짜" 3B 모델을 학습하려면 외부 GPU나 클라우드가 필요.
# 여기선 두 가지 모드 제공:
# - demo: 작은 모델 (실제로 학습 가능)
# - 3b: 구성만 정의 (학습 시 메모리 부족 경고)

if cfg.target_param_scale == "demo":
    # 소형 GPT 스타일 모델 (수십만 ~ 수백만 파라미터)
    n_layer = 6
    n_head = 8
    n_embd = 512
elif cfg.target_param_scale == "3b":
    # 3B급 근사: (실제로 M4로 학습 불가 — 예시로 config 생성 가능)
    n_layer = 40
    n_head = 32
    n_embd = 4096
else:
    raise ValueError("target_param_scale는 'demo' 또는 '3b'만 허용")

model_config = GPT2Config(
    vocab_size=cfg.vocab_size,
    n_positions=cfg.seq_len,
    n_ctx=cfg.seq_len,
    n_embd=n_embd,
    n_layer=n_layer,
    n_head=n_head,
)

print(f"모델 설정: layers={n_layer}, heads={n_head}, embd={n_embd}")

# 모델 초기화 (from_config => 학습 가능한 무작위 파라미터 모델)
model = AutoModelForCausalLM.from_config(model_config)
model.to(device)

# 모델 파라미터 수 확인
def count_parameters(model):
    return sum(p.numel() for p in model.parameters())

param_count = count_parameters(model)
print(f"모델 파라미터 수: {param_count:,}")

# ---------------------------
# 3) 토크나이저 및 합성 데이터 생성
# ---------------------------
# 데모용: GPT2 토크나이저 사용 (사전학습된 vocab 사용)
# 실제 파인튜닝 시 기기/사용 모델에 맞는 토크나이저를 사용하세요.

tokenizer = AutoTokenizer.from_pretrained("gpt2", use_fast=True)
if tokenizer.pad_token is None:
    tokenizer.add_special_tokens({"pad_token": "<|pad|>"})

# 합성 데이터 생성 함수
def generate_synthetic_text(num_samples, seq_len):
    samples = []
    for i in range(num_samples):
        # 간단한 패턴 텍스트: '문장 i: ...' 형식
        core = "".join(random.choices(
            ["AI","model","data","train","token","네트워크","학습","loss","optimizer","epoch","샘플"], k=seq_len//5
        ))
        text = f"샘플 {i}: {core}"
        samples.append(text)
    return samples

train_texts = generate_synthetic_text(cfg.train_samples, cfg.seq_len)
val_texts = generate_synthetic_text(cfg.val_samples, cfg.seq_len)

# 토크나이즈
train_enc = tokenizer(train_texts, truncation=True, padding="max_length", max_length=cfg.seq_len)
val_enc = tokenizer(val_texts, truncation=True, padding="max_length", max_length=cfg.seq_len)

train_ds = Dataset.from_dict({"input_ids": train_enc["input_ids"], "attention_mask": train_enc["attention_mask"]})
val_ds = Dataset.from_dict({"input_ids": val_enc["input_ids"], "attention_mask": val_enc["attention_mask"]})

# 데이터 콜레이터: causal LM
data_collator = DataCollatorForLanguageModeling(tokenizer=tokenizer, mlm=False)

# ---------------------------
# 4) Trainer 설정 및 학습
# ---------------------------
training_args = TrainingArguments(
    output_dir=cfg.output_dir,
    overwrite_output_dir=True,
    num_train_epochs=cfg.epochs,
    per_device_train_batch_size=cfg.batch_size,
    per_device_eval_batch_size=cfg.batch_size,
    evaluation_strategy="epoch",
    save_strategy="epoch",
    logging_strategy="steps",
    logging_steps=50,
    fp16=False,  # MPS는 fp16 지원 제한이 있으므로 기본 False
    gradient_accumulation_steps=4,
    learning_rate=cfg.learning_rate,
    weight_decay=0.01,
    save_total_limit=2,
)

trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=train_ds,
    eval_dataset=val_ds,
    data_collator=data_collator,
)

# 주의 알림: 3B 모드일 때는 실제 학습 시 메모리 부족 가능성
if cfg.target_param_scale == "3b":
    print("주의: 현재 구성은 3B급 모델을 생성합니다. Mac M4에서 전체 학습은 불가능할 확률이 높습니다.")

# 학습 실행
trainer.train()

# ---------------------------
# 5) 저장 및 간단 추론
# ---------------------------
os.makedirs(cfg.output_dir, exist_ok=True)
model.save_pretrained(cfg.output_dir)
tokenizer.save_pretrained(cfg.output_dir)

# 간단 추론 함수
from transformers import pipeline

pipe = pipeline("text-generation", model=model, tokenizer=tokenizer, device=0 if str(device)=="mps" else -1)
prompt = "인공지능 모델이란"
out = pipe(prompt, max_length=cfg.seq_len, do_sample=True, top_p=0.95, temperature=0.8, num_return_sequences=1)
print("=== 예시 생성 ===")
print(out[0]["generated_text"]) 

# ---------------------------
# 6) 확장(옵션)
# ---------------------------
# - 실제 대형 모델(사전학습된 3B)을 사용한 파인튜닝: from_pretrained(모델명, device_map='auto', torch_dtype=torch.float16)
#   단, Mac M4에서는 bitsandbytes/quantization 기반 QLoRA나 8-bit 훈련이 정상 동작하지 않을 수 있음.
# - LoRA(PEFT) 적용으로 파라미터 효율적 미세조정 가능 (권장)
# - accelerate 및 offloading을 이용해 CPU/GPU/디스크에 파라미터 분산 가능 (더 복잡)

# 끝
print('완료: 모델 학습 및 간단 추론 완료. output 폴더 확인')
