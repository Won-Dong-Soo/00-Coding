# %%
import gymnasium as gym
import torch
import torch.nn as nn
from coremltools.models import MLModel
import numpy as np

# 신경망 구조 코딩(선형)
class DQN(nn.Module):
    
    def __init__(self, state_dim, action_dim):# state_dim = 상태 크기(변수 갯수), action_dim = 행동 크기(행동 가짓수)
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(state_dim, 128),
            nn.ReLU(),
            nn.Linear(128, 128),
            nn.ReLU(),
            nn.Linear(128, 128),
            nn.ReLU(),
            nn.Linear(128, action_dim)
        )
    
    def forward(self, x):
        return self.net(x)
    

env = gym.make("CartPole-v1", render_mode = "human", max_episode_steps = 1000000000)

state_dim = env.observation_space.shape[0]
action_dim = env.action_space.n
coreml_model = MLModel(input("Select model : ")+".mlpackage")
episodes = 10

for ep in range(episodes):
    obs, _ = env.reset()
    state = np.array(obs, dtype = np.float32).reshape(1, 4)
    done = False
    total_reward = 0
    while not done:
        # Core ML 모델로 action 선택
        action_values = coreml_model.predict({"x": state})
        action = int(np.argmax(list(action_values.values())[0]))  # 최대 Q-value 선택

        # 환경 진행
        next_state, reward, terminated, truncated, info = env.step(action)
        # 노이즈 추가 (실제 환경에서의 불확실성 시뮬레이션가능)
        noise_scale = 1e-2

        noisy_state = next_state + np.random.normal(
            0, noise_scale, size=state.shape
        )
        noisy_state = np.clip(noisy_state, -10.0, 10.0)

        output = coreml_model.predict({
            "x": noisy_state.reshape(1, 4).astype(np.float32)
        })
        done = terminated or truncated
        state = np.array(noisy_state, dtype=np.float32).reshape(1, 4)
        total_reward += reward

    print(f"Episode {ep+1}: Total Reward = {total_reward}")
        
env.close()
# %%
