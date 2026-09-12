import os
import json
import random
import torch
from datasets import load_dataset, concatenate_datasets
from transformers import GPT2Tokenizer, GPT2LMHeadModel, Trainer, TrainingArguments

# ---------------------------
# 1️⃣ 데이터 생성
# ---------------------------
os.makedirs("data/chunks", exist_ok=True)

날씨 = ["맑음","흐림","비","눈"]
기분 = ["좋음","나쁨","보통"]
행동 = ["공부","운동","프로그래밍","독서","게임","글쓰기"]
장소 = ["학교","집","카페","도서관","공원"]

num_sentences = 50000000  # 5천만
chunk_size = 1000000      # 1백만씩 분할

print("데이터 생성 시작...")
for chunk_id in range(num_sentences // chunk_size):
    file_path = f"data/chunks/kor_data_{chunk_id}.jsonl"
    if os.path.exists(file_path):
        print(f"Chunk {chunk_id} 이미 존재, 건너뜀")
        continue
    with open(file_path, "w", encoding="utf-8") as f:
        for _ in range(chunk_size):
            s = f"오늘 {random.choice(날씨)} 날씨에 {random.choice(장소)}에서 {random.choice(행동)}을 하니 기분이 {random.choice(기분)}."
            json.dump({"text": s}, f, ensure_ascii=False)
            f.write("\n")
    print(f"Chunk {chunk_id} 생성 완료")
print("데이터 생성 완료!")

# ---------------------------
# 2️⃣ 토크나이저 및 모델 초기화
# ---------------------------
tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
tokenizer.add_special_tokens({'pad_token':'[PAD]'})
model = GPT2LMHeadModel.from_pretrained("gpt2")
model.resize_token_embeddings(len(tokenizer))

# ---------------------------
# 3️⃣ 토크나이징 함수
# ---------------------------
def tokenize_batch(batch):
    return tokenizer(batch["text"], truncation=True, padding="max_length", max_length=64)

# ---------------------------
# 4️⃣ 데이터 로드 및 병합
# ---------------------------
dataset_list = []
for i in range(num_sentences // chunk_size):
    ds = load_dataset("json", data_files=f"data/chunks/kor_data_{i}.jsonl", split="train")
    ds = ds.map(tokenize_batch, batched=True)
    ds.set_format(type='torch', columns=['input_ids','attention_mask'])
    dataset_list.append(ds)

full_dataset = concatenate_datasets(dataset_list)

# ---------------------------
# 5️⃣ 학습 설정
# ---------------------------
training_args = TrainingArguments(
    output_dir="./mini_gpt_kor_model",
    overwrite_output_dir=True,
    num_train_epochs=3,
    per_device_train_batch_size=2,
    save_steps=100,
    save_total_limit=2,
    logging_steps=10,
    learning_rate=5e-5,
    fp16=torch.cuda.is_available(),
)

trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=full_dataset
)

# ---------------------------
# 6️⃣ 학습 실행
# ---------------------------
print("학습 시작...")
trainer.train()

# ---------------------------
# 7️⃣ 학습 완료 후 모델 저장
# ---------------------------
model.save_pretrained("./mini_gpt_kor_model")
tokenizer.save_pretrained("./mini_gpt_kor_model")
print("학습 완료 및 모델 저장 완료!")