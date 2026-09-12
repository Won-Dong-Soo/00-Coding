# %%
import gymnasium as gym
import numpy as np
import coremltools as ct

# Core ML 모델 로드
model = ct.models.MLModel(input("Select model : ") + ".mlpackage")

# 환경
env = gym.make("CartPole-v1", render_mode="human", max_episode_steps=1000000000)

EPISODES = 10
scores = []

for ep in range(EPISODES):
    state, _ = env.reset()
    done = False
    total_reward = 0

    while not done:
        # 노이즈 추가 (실제 환경에서의 불확실성 시뮬레이션가능)
        noise_scale = 1e-2

        noisy_state = state + np.random.normal(
            0, noise_scale, size=state.shape
        )
        noisy_state = np.clip(noisy_state, -10.0, 10.0)
        # Core ML 입력
        inputs = {
            "state_workaround": noisy_state.reshape(1, 4).astype(np.float32)
        }

        # 추론
        output = model.predict(inputs)

        # 출력(확률) → 행동 결정
        probs = list(output.values())[0]   # (1, 2)
        action = int(np.argmax(probs))
        
        

        state, reward, terminated, truncated, _ = env.step(action)
        done = terminated or truncated
        total_reward += reward

    scores.append(total_reward)
    print(f"Episode {ep+1}: {total_reward}")

env.close()

print("Mean:", np.mean(scores))
print("Std :", np.std(scores))
# %%
