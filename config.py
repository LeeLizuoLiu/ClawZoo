config = {
    'problem': 'Advection',
    'NumTraj': 1,
    'use_petsc': False,
    'solver_type': 'classic',
    'dimensional_split': 1,
    'transverse_waves': 0,
    'x': {
        'size': 100,
        'domain': [0, 1],
    },
    'y': {
        'size': 100,
        'domain': [0, 1],
    },
    'num_output_steps': 200,
    'dt': 0.001 
}