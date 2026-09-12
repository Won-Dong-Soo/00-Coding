import torch
import torch.nn as nn
import coremltools as ct

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


# Actor 로드 
STATE_DIM = 4   # CartPole 기준
ACTION_DIM = 2

actor = Actor(STATE_DIM, ACTION_DIM)
actor.load_state_dict(torch.load(input("Select model : ") + ".pth", map_location="cpu"))
actor.eval()


# TorchScript 변환 (trace)
example_input = torch.randn(1, STATE_DIM)  # (batch, state_dim)
traced_actor = torch.jit.trace(actor, example_input)


# Core ML 변환
mlmodel = ct.convert(
    traced_actor,
    inputs=[
        ct.TensorType(
            name="state",
            shape=(1, STATE_DIM)
        )
    ],
    compute_units=ct.ComputeUnit.ALL  # CPU / GPU / Neural Engine 자동
)

mlmodel.save("ppo_actor.mlpackage")