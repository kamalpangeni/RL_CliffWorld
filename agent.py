''' An abstract class that specifies the Agent API for RL-Glue-py.'''
from __future__ import print_function
from abc import ABCMeta, abstractmethod

class BaseAgent:
    ''' Implements the agent for an RL-Glue environment'''

    __metaclass__ = ABCMeta

    def __init__(self):
        pass

    @abstractmethod
    def agent_init(self, agent_info={}):
        '''Setup for the agent called when the experiment first starts.'''

    @abstractmethod
    def agent_start(self, observation):
        '''The first method called when the experiment starts, called after
        the environment starts'''

    @abstractmethod
    def agent_step(selfself, reward, observation):
        '''
        A step taken by the agent
        :param reward:
        :param observation:
        :return:
        '''
    @abstractmethod
    def agent_end(self, reward):
        '''Run when the agent terminates'''

    @abstractmethod
    def agent_cleanup(self):
        '''Clean up done after the agent ends'''

    @abstractmethod
    def agent_message(self, message):
        '''A function used to pass information from the agent to the experiment'''