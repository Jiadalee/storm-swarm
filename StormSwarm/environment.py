"""
Environment abstraction for SWMM. 

This encompasses all the things related to modelling 
SWMM.
"""
import numpy as np
from StormSwarm.simulation import Simulation

class environment:
    """
    """
    def __init__(self, config):
        """
        parmas:
        ----------------------------------------
        swmm_input       : path to the input file
        reward_function  : reward function based on the state.
        state_elements   : { "state_order" : [] # Order in which states should be considered
                             "node id"     : "<depth or flow>"
                             "state_len"   : int
                           }
        control_elements : List of control elements
        timesteps        : Time interval between each control step

        TODO: How would you handle CNN 1D ?
        """
        # Dimension of the state and action space
        self.state_len        = config["state_elements"]["state_len"]
        self.action_len       = len(config["control_elements"])
        

        # Assign the reward function
        self.reward_fun       = config["reward_function"]

        # SWMM object
        self.sim              = Simulation(config["swmm_input"])
        self.sim.start()

        # SWMM Config
        self.timesteps        = config["timesteps"]
        self.control_elements = config["control_elements"]
        self.state_elements   = config["state_elements"]
        
        # methods
        self.methods = {"depth": self._getDepth, "flow": self._getFlow}
    
    def _state(self):
        """
        Query the states based on the state elements
        """
        state = []
        for i in self.state_elements["state_order"]:
            state.append(self.methods[self.state_elements[i]](i))
        
        state = np.asarray(state)
        return state 

    def _reward(self):
        """
        Reward based on the user defined function 
        """
        reward = self.reward_fun(self.sim)
        return reward

    def step(self, actions):
        """
        Implements the control action and forwards
        the simulation to the predefined steps 

        params:
        ----------------------------------------
        actions  : actions to take as an array (1 x n)
        
        returns:
        ----------------------------------------
        new_state : Next state
        reward    : Reward based on the defimed reward func.
        done      : Terminal state
        meta      : Any meta data you would need...
        """
        # implement the actions
        for asset, valve_position in zip(self.control_elements, actions):

            self._setValvePosition(asset, valve_position)
        
        # take the step !
        time = self.sim._model.swmm_step()
        done = False if time > 0 else True

        new_state = self._state()
        reward    = self._reward()

        return new_state, reward, done


    def reset(self):
        """
        Resets the simulation and retuns the state 
        """
        self.sim._model.swmm_end()
        self.sim._model.swmm_close()

        # Start the next simulation
        self.sim._model.swmm_open()
        self.sim._model.swmm_start()

        # get the state
        state = self._state()
        return state


    def _getDepth(self, ID):
        return self.sim._model.getNodeResult(ID, 5)

    def _getFlow(self, ID):
        return self.sim._model.getLinkResult(ID, 0)

    def _getInflow(self, ID):
        pass

    def _setInflow(self, ID, value):
        pass 

    def _getValvePosition(self, ID):
        return self.sim._model.getLinkResult(ID, 6) 

    def _setValvePosition(self, ID, valve):
        self.sim._model.setLinkSetting(ID, valve) 

    def _getRainfall(self, gage):
        pass 

    def _setRainfall(self, gage, value):
        pass

    def _terminate(self):
        self.sim._model.swmm_end()
        self.sim._model.swmm_close()

    def initial_state(self):
        return self._state()
