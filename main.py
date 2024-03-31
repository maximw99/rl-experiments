import gymnasium as gym

env = gym.make("LunarLander-v2", render_mode="human")
observation, info = env.reset()

for _ in range(100):
    action = env.action_space.sample()  # agent policy that uses the observation and info
    observation, reward, terminated, truncated, info = env.step(action)
    print(reward)

    if terminated or truncated:
        observation, info = env.reset()

env.close()

