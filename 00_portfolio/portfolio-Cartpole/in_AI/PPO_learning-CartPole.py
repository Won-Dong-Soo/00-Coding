import gymnasium as gym
import torch
import torch.nn as nn
import torch.optim as optim
from torch.distributions import Categorical
import numpy as np

# 행동 결정용 Actor 신경망  
class Actor(nn.Module):
    def __init__(self, s_dim, a_dim):
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(s_dim, 64), 
            nn.Tanh(),
            nn.Linear(64, 128), 
            nn.Tanh(),
            nn.Linear(128, 64),
            nn.Tanh(), 
            nn.Linear(64, a_dim)
        )

    def forward(self, x):
        return torch.softmax(self.net(x), dim=-1)

# 상태 가치 평가용 Critic 신경망  
class Critic(nn.Module):
    def __init__(self, s_dim):
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(s_dim, 64), 
            nn.Tanh(),
            nn.Linear(64, 128), 
            nn.Tanh(),
            nn.Linear(128, 64),
            nn.Tanh(), 
            nn.Linear(64, 1)
        )

    def forward(self, x):
        return self.net(x).squeeze(-1)


# GAE (Generalized Advantage Estimation) 계산 함수  
def compute_gae(rewards, values, dones, last_value, gamma=0.99, lam=0.95):
    values = np.append(values, last_value)
    adv = np.zeros_like(rewards)
    gae = 0
    for t in reversed(range(len(rewards))):
        delta = rewards[t] + gamma * values[t+1] * (1 - dones[t]) - values[t]
        gae = delta + gamma * lam * (1 - dones[t]) * gae
        adv[t] = gae
    returns = adv + values[:-1]
    return adv, returns


# 환경 구성 및 네트워크 초기화  
env = gym.make("CartPole-v1")
s_dim = env.observation_space.shape[0]
a_dim = env.action_space.n

actor = Actor(s_dim, a_dim)
critic = Critic(s_dim)

actor_opt = optim.Adam(actor.parameters(), lr=3e-4)
critic_opt = optim.Adam(critic.parameters(), lr=1e-3)

# 하이퍼파라미터(고정값) 설정  
ROLLOUT = 512 # 경험 기록  
EPOCHS = 7 # 경험 학습 반복 횟수  
CLIP = 0.2 # 정책 업데이트 상한/하한 설정  
ENTROPY_COEF = 0.01 # 행동 다양성 유지 위해 엔트로피 보너스 계수  

state, _ = env.reset()
ep_reward = 0
episodes = 200000

# 환경 진행  
for ep in range(episodes):
    states, actions, rewards, dones, logps, values = [], [], [], [], [], []

    # Rollout 단계 : 행동 선택, 환경 상호작용, 경험 저장  
    for _ in range(ROLLOUT):
        s = torch.tensor(state, dtype=torch.float32)
        probs = actor(s)
        dist = Categorical(probs)
        a = dist.sample()

        next_state, r, term, trunc, _ = env.step(a.item())
        done = term or trunc

        states.append(state)
        actions.append(a.item())
        rewards.append(r)
        dones.append(done)
        logps.append(dist.log_prob(a).item())
        values.append(critic(s).item())

        ep_reward += r
        state = next_state

        if done:
            print(f"Episode {ep+1}, Reward: {ep_reward}")
            ep_reward = 0
            state, _ = env.reset()

    # 학습 단계
    with torch.no_grad():
        last_value = critic(torch.tensor(state, dtype=torch.float32)).item()

    adv, ret = compute_gae(
        np.array(rewards),
        np.array(values),
        np.array(dones),
        last_value
    )

    # 정규화 (필수)-> 학습 안정성 위해 이득(advantage) 정규화
    adv = (adv - adv.mean()) / (adv.std() + 1e-8)

    states = torch.tensor(states, dtype=torch.float32)
    actions = torch.tensor(actions)
    old_logps = torch.tensor(logps)
    returns = torch.tensor(ret, dtype=torch.float32)
    advantages = torch.tensor(adv, dtype=torch.float32)

    # PPO 업데이트 단계 : 경험 여러 번 학습
    for _ in range(EPOCHS):
        probs = actor(states)
        dist = Categorical(probs)
        logps_new = dist.log_prob(actions)

        ratio = torch.exp(logps_new - old_logps)
        surr1 = ratio * advantages
        surr2 = torch.clamp(ratio, 1-CLIP, 1+CLIP) * advantages
        actor_loss = -torch.min(surr1, surr2).mean()

        values_new = critic(states)
        critic_loss = 0.5 * (returns - values_new).pow(2).mean()

        entropy = dist.entropy().mean()

        loss = actor_loss + critic_loss - ENTROPY_COEF * entropy

        actor_opt.zero_grad()
        critic_opt.zero_grad()
        loss.backward()
        actor_opt.step()
        critic_opt.step()
        
env.close()
torch.save(actor.state_dict(), "actor.pth")
torch.save(critic.state_dict(), "critic.pth")

# # 학습된 모델 테스트
# env = gym.make("CartPole-v1", render_mode="human")

# for ep in range(episodes):
#     states, actions, rewards, dones, logps, values = [], [], [], [], [], []

#     # Rollout 단계 : 행동 선택, 환경 상호작용, 경험 저장  
#     for _ in range(ROLLOUT):
#         s = torch.tensor(state, dtype=torch.float32)
#         probs = actor(s)
#         dist = Categorical(probs)
#         a = dist.sample()

#         next_state, r, term, trunc, _ = env.step(a.item())
#         done = term or trunc

#         states.append(state)
#         actions.append(a.item())
#         rewards.append(r)
#         dones.append(done)
#         logps.append(dist.log_prob(a).item())
#         values.append(critic(s).item())

#         ep_reward += r
#         state = next_state