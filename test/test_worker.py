from StormSwarm import generate_swarm
from StormSwarm import environment

def reward(swmm_sim):
    return 0.0

def ctrl(state):
    return [1.0]

def test_generate_swarm():
    ## Test initialization

    config = { "swmm_input" : "./networks/parallel.inp",
        "state_elements"  : {"state_order" : ["P1", "P2"],
            "P1" : "depth",
            "P2" : "depth",
            "state_len" : 2},
        "control_elements" : ["1"],
        "controller" : ctrl,
        "reward_function" : reward,
        "timesteps" : 1}

    data = generate_swarm(config, 5, 10)

    assert(len(data) == 10)
    assert(len(data[0].keys()) == 4)
