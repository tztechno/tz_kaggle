## change PPO form to CIP form

from stable_baselines3.common.policies import ActorCriticPolicy
import torch
import torch.nn as nn


class CIPPolicy(ActorCriticPolicy):
    def __init__(self, observation_space, action_space, lr_schedule, *args, **kwargs):
        super().__init__(observation_space, action_space, lr_schedule, *args, **kwargs)
        obs_dim = observation_space.shape[0]  # 26 dimensions
        embed_dim = 26          
        self.causal_attention = nn.MultiheadAttention(
            embed_dim=embed_dim, 
            num_heads=2  # Since 26 is divisible by 2
        )
        self.obs_projection = nn.Sequential(
            nn.Linear(obs_dim, embed_dim),
            nn.LayerNorm(embed_dim)
        )
        self.causal_projection = nn.Sequential(
            nn.Linear(embed_dim, obs_dim),
            nn.LayerNorm(obs_dim)
        )

    def forward(self, obs, deterministic=False):
        obs = obs.float()
        embedded_obs = self.obs_projection(obs)
        causal_features, _ = self.causal_attention(
            embedded_obs.unsqueeze(0), 
            embedded_obs.unsqueeze(0), 
            embedded_obs.unsqueeze(0)
        )
        causal_features = causal_features.squeeze(0)
        enhanced_features = self.causal_projection(causal_features)
        return super().forward(enhanced_features, deterministic)


def create_cip_ppo_model(env, learning_rate=3e-4):
    policy_kwargs = {
        'net_arch': [dict(pi=[64, 64], vf=[64, 64])]
    }
    model = PPO(
        policy=CIPPolicy, 
        env=env, 
        learning_rate=learning_rate,
        policy_kwargs=policy_kwargs,
        verbose=1
    )
    return model

    
###########################################

#env = gym.make("CartPole-v1")
    
#model = PPO("MlpPolicy", env, verbose=1) ### delete this
#model = create_cip_ppo_model(env)        ### add this

#model.learn(total_timesteps=10000)

###########################################
