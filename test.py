import gymnasium as gym
import math
import random
import matplotlib
import matplotlib.pyplot as plt
from collections import namedtuple, deque
from itertools import count

import torch
import torch.nn as nn
import torch.optim as optim
import torch.nn.functional as F
import random


env = gym.make("CartPole-v1", render_mode="human")


def random_run():

    env.reset()
    episodes = 25
    for episode in range(0, episodes):
        state = env.reset()
        terminated = False
        score = 0 
        
        while not terminated:
            env.render()
            action = random.choice([0,1])
            n_state, reward, terminated, truncated, info = env.step(action)
            score+=reward
        print('Episode:{} Score:{}'.format(episode, score))

    env.close()


random_run()