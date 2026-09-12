import gymnasium as gym
import time

env = gym.make("CartPole-v1", render_mode = "human")

for episode in range(10):
    obs, info = env.reset()
    done = False
    while not done:
        action = env.action_space.sample()
        obs, reward, terminated, truncated, info = env.step(action)
        done = terminated or truncated
        time.sleep(0.02)
        state = discretize(obs)
        
env.close()