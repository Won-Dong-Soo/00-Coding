# %%
import gymnasium as gym
import torch
import torch.optim as optim
import torch.nn as nn
import random
from collections import deque
import coremltools as ct

# 신경망 구조 코딩(DQN)
class net(nn.Module):
    
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
    
    
env = gym.make("CartPole-v1", max_episode_steps = 1000000000)
    
state_dim = env.observation_space.shape[0]
action_dim = env.action_space.n
policy_net = net(state_dim, action_dim)
policy_net.load_state_dict(torch.load(input("Select model : ") + ".pth"))
policy_net.eval()
example_input = torch.rand(1, 4)
traced_model = torch.jit.trace(policy_net, example_input)
mlmodel = ct.convert(traced_model, inputs=[ct.TensorType(shape=example_input.shape)])
mlmodel.save( input("Select converted model's name : ")+".mlpackage")

env.close()
# %%
