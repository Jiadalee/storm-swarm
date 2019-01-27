from StormSwarm.environment import environment
import numpy as np

def test_initalization():
    def reward(swmm_sim):
        return 0.0
    ## Test initialization
    config = { "swmm_input" : "./networks/parallel.inp",
        "reward_function" : reward,
        "state_elements"  : {"state_order" : ["P1", "P2"],
            "P1" : "depth",
            "P2" : "depth",
            "state_len" : 2},
        "control_elements" : ["1"],
        "timesteps" : 1}
    env = environment(config)

def test_environment():
    def reward(swmm_sim):
        return 0.0

    config = { "swmm_input" : "./networks/parallel.inp",
    "reward_function" : reward,
    "state_elements"  : {"state_order" : ["P1", "P2"],
        "P1" : "depth",
        "P2" : "depth",
        "state_len" : 2},
    "control_elements" : ["1"],
    "timesteps" : 1}
    env = environment(config)

    ## Test SWMM run
    done = False 
    state = env._state()
    print(state)
    assert(len(state) == 2)
    step = 1
    while not done:
        action = np.random.rand()
        new_state, reward, done = env.step([action])
        state = new_state
        step += 1

    env._terminate()
    assert(done) == True
