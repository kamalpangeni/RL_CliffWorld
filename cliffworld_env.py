from environment import BaseEnvironment

import numpy as np
from copy import deepcopy

class Environment(BaseEnvironment):
    '''
    Implements the environment for an RLGlue environment
    '''

    def env_init(self,env_info={}):
        '''Setup for the environment called when the experiment first starts'''

        self.rows = 4
        self.cols = 12
        self.start = [0,0]
        self.goal = [0,11]
        self.current_state = None

    def env_start(self):
        '''
        :return: The first state observation from the environment
        '''
        self.current_state = self.start
        self.reward_obs_term = (0.0,self.observation(self.current_state),False)

        return self.reward_obs_term[1]

    def env_step(self,action):
        '''
        :param action:
        :return: a tuple of the reward, state observation, and boolean indicating if it's terminal
        '''

        new_state = deepcopy(self.current_state)

        if action == 0: #right
            new_state[1] = min(new_state[1]+1,self.cols-1)
        elif action == 1: #down
            new_state[0] = max(new_state[0]-1,0)
        elif action == 2: #left
            new_state[1] = max(new_state[1]-1,0)
        elif action ==3: # up
            new_state[0] = min(new_state[0]+1, self.rows-1)
        else:
            raise Exception('Invalid action')
        self. current_state = new_state

        reward = -1.0

        is_terminal = False

        if self.current_state[0]==0 and self.current_state[1]>0:
            if self.current_state[1]<self.cols-1:
                reward = -100.0
                self.current_state = deepcopy(self.start)
            else:
                is_terminal = True
        self.reward_obs_term = (reward, self.observation(self.current_state), is_terminal)

        return self.reward_obs_term

    def observation(self,state):
        return state[0]*self.cols+state[1]

    def env_cleanup(self):
        pass

    def env_message(self,message):

        if message == 'what is the current reward?':
            return '{}'.format(self.reward_obs_term[0])
        else:
            return "I don't know how to respond your message"
