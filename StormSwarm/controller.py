import numpy as np

class controller:
    """
    Class for representing the policy of workers
    """
    def __init__(self,
                 constant_action,
                 policy,
                 exploration,
                 action_space):
        self.exploration = exploration
        self.action_space = action_space
        self.policy = policy 
        self.constant_action = constant_action
        
    def act(self, state):
        if np.random.rand() < self.exploration:
            action = np.random.choice(self.action_space)
        else:
            action = self._policy(state)
        return [action]
    
    def _policy(self, state):
        """
        Governing the actions to take given a state.
        This can be modified accordingly.
        """
        action = self.constant_action
        return action
