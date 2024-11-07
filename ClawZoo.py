import numpy as np
from utils import generate_trajectories

if __name__ == '__main__':
    from config import config
    from prototype_problems.twoD_Problems import Advection 
    generate_trajectory = Advection.generate_trajectory
    generate_trajectories(config, generate_trajectory)
