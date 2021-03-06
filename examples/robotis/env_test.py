#!/usr/bin/env python

import time
import gym
from gym import wrappers
import gym_gazebo
import numpy as np

if __name__ == '__main__':
    outdir = '/tmp/gazebo_gym_experiments/'
    env = gym.make('GazeboRobotisOp3-v0')
    env._max_episode_steps = 10000000000000
    env = gym.wrappers.Monitor(env, outdir, force=True, resume=False)
    while True:
        env.reset()
        while True:
            action = 0.5 * (np.random.rand(20) - 0.5)
            state, reward, done, info = env.step(action)
            # time.sleep(0.1)
            if done: break
    env.close()
