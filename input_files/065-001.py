from main import run_app
from miller import Move

moves = []
traversespeed = 8
retractspeed = 8
cuttingspeed = 4.0
plungespeed = 4.0
z_down = -0.005
z_up = 0.05
moves.append(Move(None, None, 0.05, 8))
moves.append(Move(0.877, 1.055, 0.05, 8))
moves.append(Move(None, None, -0.005, 4.0))
moves.append(Move(0.899, 1.055, -0.005, 4.0))
moves.append(Move(0.9, 1.054, -0.005, 4.0))
moves.append(Move(0.902, 1.052, -0.005, 4.0))
moves.append(Move(0.903, 1.051, -0.005, 4.0))
moves.append(Move(0.905, 1.051, -0.005, 4.0))
moves.append(Move(0.905, 1.053, -0.005, 4.0))
moves.append(Move(0.908, 1.054, -0.005, 4.0))
moves.append(Move(0.909, 1.055, -0.005, 4.0))
moves.append(Move(0.93, 1.055, -0.005, 4.0))
moves.append(Move(0.931, 1.054, -0.005, 4.0))
moves.append(Move(0.933, 1.052, -0.005, 4.0))
moves.append(Move(0.934, 1.048, -0.005, 4.0))
moves.append(Move(0.934, 0.995, -0.005, 4.0))
moves.append(Move(0.933, 0.994, -0.005, 4.0))
moves.append(Move(0.931, 0.992, -0.005, 4.0))
moves.append(Move(0.927, 0.991, -0.005, 4.0))
moves.append(Move(0.908, 0.991, -0.005, 4.0))
moves.append(Move(0.907, 0.992, -0.005, 4.0))
moves.append(Move(0.905, 0.994, -0.005, 4.0))
moves.append(Move(0.904, 0.995, -0.005, 4.0))
moves.append(Move(0.902, 0.995, -0.005, 4.0))
moves.append(Move(0.902, 0.993, -0.005, 4.0))
moves.append(Move(0.899, 0.992, -0.005, 4.0))
moves.append(Move(0.898, 0.991, -0.005, 4.0))
moves.append(Move(0.877, 0.991, -0.005, 4.0))
moves.append(Move(0.876, 0.992, -0.005, 4.0))
moves.append(Move(0.874, 0.994, -0.005, 4.0))
moves.append(Move(0.873, 0.998, -0.005, 4.0))
moves.append(Move(0.873, 1.051, -0.005, 4.0))
moves.append(Move(0.874, 1.052, -0.005, 4.0))
moves.append(Move(0.876, 1.054, -0.005, 4.0))
moves.append(Move(0.877, 1.055, -0.005, 4.0))
moves.append(Move(None, None, 0.05, 8))
moves.append(Move(0.751, 1.055, 0.05, 8))
moves.append(Move(None, None, -0.005, 4.0))
moves.append(Move(0.773, 1.055, -0.005, 4.0))
moves.append(Move(0.774, 1.054, -0.005, 4.0))
moves.append(Move(0.776, 1.052, -0.005, 4.0))
moves.append(Move(0.777, 1.051, -0.005, 4.0))
moves.append(Move(0.779, 1.051, -0.005, 4.0))
moves.append(Move(0.779, 1.053, -0.005, 4.0))
moves.append(Move(0.782, 1.054, -0.005, 4.0))
moves.append(Move(0.783, 1.055, -0.005, 4.0))
moves.append(Move(0.804, 1.055, -0.005, 4.0))
moves.append(Move(0.805, 1.054, -0.005, 4.0))
moves.append(Move(0.807, 1.052, -0.005, 4.0))
moves.append(Move(0.808, 1.048, -0.005, 4.0))
moves.append(Move(0.808, 0.995, -0.005, 4.0))
moves.append(Move(0.807, 0.994, -0.005, 4.0))
moves.append(Move(0.805, 0.992, -0.005, 4.0))
moves.append(Move(0.801, 0.991, -0.005, 4.0))
moves.append(Move(0.782, 0.991, -0.005, 4.0))
moves.append(Move(0.781, 0.992, -0.005, 4.0))
moves.append(Move(0.779, 0.994, -0.005, 4.0))
moves.append(Move(0.778, 0.995, -0.005, 4.0))
moves.append(Move(0.776, 0.995, -0.005, 4.0))
moves.append(Move(0.776, 0.993, -0.005, 4.0))
moves.append(Move(0.773, 0.992, -0.005, 4.0))
moves.append(Move(0.772, 0.991, -0.005, 4.0))
moves.append(Move(0.751, 0.991, -0.005, 4.0))
moves.append(Move(0.75, 0.992, -0.005, 4.0))
moves.append(Move(0.748, 0.994, -0.005, 4.0))
moves.append(Move(0.747, 0.998, -0.005, 4.0))
moves.append(Move(0.747, 1.051, -0.005, 4.0))
moves.append(Move(0.748, 1.052, -0.005, 4.0))
moves.append(Move(0.75, 1.054, -0.005, 4.0))
moves.append(Move(0.751, 1.055, -0.005, 4.0))
moves.append(Move(None, None, 0.05, 8))
moves.append(Move(1.089, 1.102, 0.05, 8))
moves.append(Move(None, None, -0.005, 4.0))
moves.append(Move(1.175, 1.102, -0.005, 4.0))
moves.append(Move(1.176, 1.101, -0.005, 4.0))
moves.append(Move(1.178, 1.099, -0.005, 4.0))
moves.append(Move(1.179, 1.095, -0.005, 4.0))
moves.append(Move(1.179, 1.066, -0.005, 4.0))
moves.append(Move(1.178, 1.065, -0.005, 4.0))
moves.append(Move(1.176, 1.063, -0.005, 4.0))
moves.append(Move(1.172, 1.062, -0.005, 4.0))
moves.append(Move(1.089, 1.062, -0.005, 4.0))
moves.append(Move(1.088, 1.063, -0.005, 4.0))
moves.append(Move(1.086, 1.065, -0.005, 4.0))
moves.append(Move(1.085, 1.068, -0.005, 4.0))
moves.append(Move(0.965, 1.068, -0.005, 4.0))
moves.append(Move(0.965, 1.051, -0.005, 4.0))
moves.append(Move(0.968, 1.051, -0.005, 4.0))
moves.append(Move(0.968, 1.053, -0.005, 4.0))
moves.append(Move(0.971, 1.054, -0.005, 4.0))
moves.append(Move(0.972, 1.055, -0.005, 4.0))
moves.append(Move(0.993, 1.055, -0.005, 4.0))
moves.append(Move(0.994, 1.054, -0.005, 4.0))
moves.append(Move(0.996, 1.052, -0.005, 4.0))
moves.append(Move(0.997, 1.048, -0.005, 4.0))
run_app(moves)
