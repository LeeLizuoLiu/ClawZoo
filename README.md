# Dataset of Hyperbolic Conservation Laws

## Overview

This project provides a framework for generating dataset of hyperbolic conservation laws using the Clawpack library. Designed with flexibility and modularity in mind, it allows users to define initial conditions and simulation configurations independently, making it easier to experiment with different setups across multiple prototype problems.

## Project Structure

The project is organized as follows:

```plaintext
clawpack_project/
├── prototype_problems/          # Contains folders for individual problem setups
│   ├── problem1/                 # Folder for Problem 1
│   │   ├── config.json           # Configuration for Problem 1
│   │   └── main.py               # Main script for Problem 1
│   ├── problem2/                 # Folder for Problem 2
│   │   ├── config.json           # Configuration for Problem 2
│   │   └── main.py               # Main script for Problem 2
├── initial_conditions/           # Custom initial condition modules
│   ├── __init__.py               # Initialization file for the package
│   ├── condition1.py             # Example initial condition function 1
│   ├── condition2.py             # Example initial condition function 2
├── utils.py                      # Utility functions for loading config and initial conditions
└── README.md                     # Project documentation
```

## Key Components

- **Prototype Problems**: Each prototype problem folder (e.g., `problem1/`, `problem2/`) contains its own `config.json` file and a `main.py` script. This setup enables you to test and configure each problem independently, making it easy to switch between different simulation setups.

- **Initial Conditions**: The `initial_conditions` folder contains modules that define various initial conditions for the simulations. Each initial condition is implemented in a separate file (e.g., `condition1.py`), and these can be specified within each problem's configuration file.

- **Configurations**: Each prototype problem uses a `config.json` file to specify simulation parameters, such as the initial condition module, grid size, time steps, and final time. The project supports configurations in JSON format for easy editing and consistency across different simulations.

## Usage

1. **Set Up Initial Conditions**: Define initial conditions in separate files within the `initial_conditions` folder. Each initial condition file should provide a function that returns the initial state for the simulation.

2. **Configure Each Problem**: In each prototype problem folder, edit the `config.json` file to specify the initial condition module and simulation parameters.

3. **Run Simulations**: Navigate to a problem folder (e.g., `prototype_problems/problem1/`) and execute the `main.py` script to run the Clawpack simulation with the specified configuration.

## Example Config File (`config.json`)

Below is a sample configuration file that defines the initial condition module and simulation parameters:

```json
{
    "initial_condition_module": "condition1",
    "simulation_parameters": {
        "grid_size": [100, 100],
        "time_step": 0.01,
        "final_time": 1.0
    }
}
```


This structure and approach will help you manage multiple simulation setups and track experimental results efficiently. Let me know if you want further details on specific parts of the setup!
