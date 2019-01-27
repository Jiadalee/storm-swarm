#  ⛈️ ⛈️  Storm Swarm ⛈️ ⛈️
Modular API for running large ensembles of real time control simulations in EPA-SWMM 

## Dependencies  

This codebase heavily draws from the OWA's [pyswmm](https://github.com/OpenWaterAnalytics/pyswmm) and [SWMM](https://github.com/OpenWaterAnalytics/Stormwater-Management-Model). Though this code can be used along pyswmm, I've provided the necessary components from pyswmm with this library, so that it  can be used as a standalone package. 

### Additional Dependencies 

 1. Numpy
 2. Multiprocessing

## Installation
```bash
    git clone  https://github.com/kLabUM/storm-swarm.git
    pip/pip3 install .
```
## Getting Started

This library is 3 primary components:

 1. Config (dict)
 2. Environment (class)
 3. Swarm (function) 

### Config 
This dictionary configures the storm water network being stimulated and identifies the state and action space.
```python
        config = { "swmm_input" : "./networks/parallel.inp",
			       "state_elements"  : {"state_order" : ["P1", "P2"],
								        "P1" : "depth",
								        "P2" : "depth",
								        "state_len" : 2},
			       "control_elements" : ["1"],
                   "controller" : ctrl,
                   "reward_function" : reward,
                   "timesteps" : 1}
```

### Environment 

This class acts as a handle to control SWMM simulation and can also be used independently 
```python
    env = environment(config)
```
### Swarm 
This function can take single/mutiple config files and runs them in parallel.
```python
    generate_swarm(config, workers=3, jobs=10)
```

