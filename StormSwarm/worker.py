"""
Worker Bees:
    Functions for creating workers that generate the experience 
    for the learner to learn the optimal control startegy. 
"""
from multiprocessing import Pool
import multiprocessing
from StormSwarm import environment

def worker_bee(config):
    """
    Generates Parallel SWMM environments based on
    multiprocessing 
    """
    env = environment(config)
    done = False
    experience = {}
    experience["state"] = []
    experience["state_new"] = []
    experience["reward"] = []
    experience["done"] = []

    controller = config["controller"]

    state = env.initial_state()
    while not done:
        actions = controller(state)

        state_new, reward, done = env.step(actions)

        state = state_new
        
        experience["state"].append(state)
        experience["state_new"].append(state_new)
        experience["reward"].append(reward)
        experience["done"].append(done)
    
    env._terminate()
    return experience

def generate_swarm(config, workers, jobs):
    """
    Generate workers based on the environment and controller 
    """
    swarm_inputs = [config for i in range(0, jobs)]

    with Pool(workers) as p:
        data = p.map(worker_bee, swarm_inputs)

    return data 

