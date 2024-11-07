import numpy as np
import os

def generate_trajectories(config, generate_trajectory, mode='Train'):
    sol = []
    for _ in range(config['NumTraj']):
        output = generate_trajectory(config)
        sol.append(np.stack([output.frames[i].q for i in range(len(output.frames))]))
    Data = np.stack(sol) # B x T x D x X x Y
    if not os.path.exists('Data'):
        os.makedirs('Data',exist_ok=True)
    np.save('Data/'+config['problem'] + '_' + mode + 'Data'+'.npy', np.swapaxes(np.swapaxes(Data,2,3),3,4))


