'''
Abstract environment base class for RL-Glue-py
'''

from __future__ import print_function

from abc import ABCMeta, abstractmethod

class BaseEnvironment:
    '''
    Implements the environment for an RLGlue environment
    '''
    __metaclass__ = ABCMeta

    def __init__(self):
        reward  = None
        observation = None
        termination = None
        self.reward_obs_term = (reward, observation, termination)

    @abstractmethod
    def env_init(self,env_info={}):
        '''
        setup for the environment called when the experiment first starts
        :param env_info:
        :return:
        '''
    @abstractmethod
    def env_start(self):
        '''
        The first method called when the experiment starts, called before the agent starts
        :return:
        '''
    @abstractmethod
    def env_step(self,action):
        '''
        A step taken by the environment
        :param action:
        :return:
        '''
    @abstractmethod
    def env_cleanup(self):
        ''' Clean up done afte the environment ends'''

    @abstractmethod
    def env_message(self,message):
        ''' A message asking the environment for information'''