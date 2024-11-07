#!/usr/bin/env python
# encoding: utf-8
r"""
2D shallow water: radial dam break
==================================

Solve the 2D shallow water equations:

.. math::
    h_t + (hu)_x + (hv)_y = 0 \\
    (hu)_t + (hu^2 + \frac{1}{2}gh^2)_x + (huv)_y = 0 \\
    (hv)_t + (huv)_x + (hv^2 + \frac{1}{2}gh^2)_y = 0.

The initial condition is a circular area with high depth surrounded by lower-depth water.
The top and right boundary conditions reflect, while the bottom and left boundaries
are outflow.
"""

import numpy as np
from clawpack import riemann
from clawpack.riemann.shallow_roe_with_efix_2D_constants import depth, x_momentum, y_momentum, num_eqn

def qinit(state,h_in=2.,h_out=1.,dam_radius=0.5):
    x0=0.
    y0=0.
    X, Y = state.p_centers
    r = np.sqrt((X-x0)**2 + (Y-y0)**2)

    state.q[depth     ,:,:] = h_in*(r<=dam_radius) + h_out*(r>dam_radius)
    state.q[x_momentum,:,:] = 0.
    state.q[y_momentum,:,:] = 0.

    
def setup(kernel_language='Fortran', use_petsc=False, outdir='./_output',
          solver_type='classic', riemann_solver='roe',disable_output=False):
    if use_petsc:
        import clawpack.petclaw as pyclaw
    else:
        from clawpack import pyclaw

    if riemann_solver.lower() == 'roe':
        rs = riemann.shallow_roe_with_efix_2D
    elif riemann_solver.lower() == 'hlle':
        rs = riemann.shallow_hlle_2D

    if solver_type == 'classic':
        solver = pyclaw.ClawSolver2D(rs)
        solver.limiters = pyclaw.limiters.tvd.MC
        solver.dimensional_split=1
    elif solver_type == 'sharpclaw':
        solver = pyclaw.SharpClawSolver2D(rs)

    solver.bc_lower[0] = pyclaw.BC.extrap
    solver.bc_upper[0] = pyclaw.BC.wall
    solver.bc_lower[1] = pyclaw.BC.extrap
    solver.bc_upper[1] = pyclaw.BC.wall

    # Domain:
    xlower = -2.5
    xupper = 2.5
    mx = 150
    ylower = -2.5
    yupper = 2.5
    my = 150
    x = pyclaw.Dimension(xlower,xupper,mx,name='x')
    y = pyclaw.Dimension(ylower,yupper,my,name='y')
    domain = pyclaw.Domain([x,y])

    state = pyclaw.State(domain,num_eqn)

    # Gravitational constant
    state.problem_data['grav'] = 1.0

    qinit(state)

    claw = pyclaw.Controller()
    claw.tfinal = 2.5
    claw.solution = pyclaw.Solution(state,domain)
    claw.solver = solver
    if disable_output:
        claw.output_format = None
    claw.outdir = outdir
    claw.num_output_times = 10
    claw.setplot = setplot
    claw.keep_copy = True

    return claw
