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
moves.append(Move(1.027, 1.387, 0.05, 8))
moves.append(Move(None, None, -0.005, 4.0))
moves.append(Move(1.117, 1.387, -0.005, 4.0))
moves.append(Move(1.117, 1.342, -0.005, 4.0))
moves.append(Move(1.027, 1.342, -0.005, 4.0))
moves.append(Move(1.027, 1.387, -0.005, 4.0))
moves.append(Move(None, None, 0.05, 8))
moves.append(Move(1.487, 1.867, 0.05, 8))
moves.append(Move(None, None, -0.005, 4.0))
moves.append(Move(1.637, 1.867, -0.005, 4.0))
moves.append(Move(1.637, 1.782, -0.005, 4.0))
moves.append(Move(1.487, 1.782, -0.005, 4.0))
moves.append(Move(1.487, 1.867, -0.005, 4.0))
moves.append(Move(None, None, 0.05, 8))
moves.append(Move(1.067, 1.867, 0.05, 8))
moves.append(Move(None, None, -0.005, 4.0))
moves.append(Move(1.212, 1.867, -0.005, 4.0))
moves.append(Move(1.212, 1.782, -0.005, 4.0))
moves.append(Move(1.067, 1.782, -0.005, 4.0))
moves.append(Move(1.067, 1.867, -0.005, 4.0))
moves.append(Move(None, None, 0.05, 8))
moves.append(Move(1.332, 1.137, 0.05, 8))
moves.append(Move(None, None, -0.005, 4.0))
moves.append(Move(1.372, 1.137, -0.005, 4.0))
moves.append(Move(1.372, 1.097, -0.005, 4.0))
moves.append(Move(1.332, 1.097, -0.005, 4.0))
moves.append(Move(1.332, 1.137, -0.005, 4.0))
moves.append(Move(None, None, 0.05, 8))
moves.append(Move(1.282, 1.137, 0.05, 8))
moves.append(Move(None, None, -0.005, 4.0))
moves.append(Move(1.322, 1.137, -0.005, 4.0))
moves.append(Move(1.322, 1.097, -0.005, 4.0))
moves.append(Move(1.282, 1.097, -0.005, 4.0))
moves.append(Move(1.282, 1.137, -0.005, 4.0))
moves.append(Move(None, None, 0.05, 8))
moves.append(Move(1.232, 1.137, 0.05, 8))
moves.append(Move(None, None, -0.005, 4.0))
moves.append(Move(1.267, 1.137, -0.005, 4.0))
moves.append(Move(1.267, 1.097, -0.005, 4.0))
moves.append(Move(1.232, 1.097, -0.005, 4.0))
moves.append(Move(1.232, 1.137, -0.005, 4.0))
moves.append(Move(None, None, 0.05, 8))
moves.append(Move(1.332, 1.187, 0.05, 8))
moves.append(Move(None, None, -0.005, 4.0))
moves.append(Move(1.372, 1.187, -0.005, 4.0))
moves.append(Move(1.372, 1.147, -0.005, 4.0))
moves.append(Move(1.332, 1.147, -0.005, 4.0))
moves.append(Move(1.332, 1.187, -0.005, 4.0))
moves.append(Move(None, None, 0.05, 8))
moves.append(Move(1.292, 1.187, 0.05, 8))
moves.append(Move(None, None, -0.005, 4.0))
moves.append(Move(1.307, 1.187, -0.005, 4.0))
moves.append(Move(1.312, 1.182, -0.005, 4.0))
moves.append(Move(1.317, 1.177, -0.005, 4.0))
moves.append(Move(1.322, 1.162, -0.005, 4.0))
moves.append(Move(1.317, 1.157, -0.005, 4.0))
moves.append(Move(1.307, 1.147, -0.005, 4.0))
moves.append(Move(1.287, 1.147, -0.005, 4.0))
moves.append(Move(1.282, 1.167, -0.005, 4.0))
moves.append(Move(1.282, 1.177, -0.005, 4.0))
moves.append(Move(1.292, 1.187, -0.005, 4.0))
moves.append(Move(None, None, 0.05, 8))
moves.append(Move(1.232, 1.187, 0.05, 8))
moves.append(Move(None, None, -0.005, 4.0))
moves.append(Move(1.267, 1.187, -0.005, 4.0))
moves.append(Move(1.267, 1.147, -0.005, 4.0))
moves.append(Move(1.232, 1.147, -0.005, 4.0))
moves.append(Move(1.232, 1.187, -0.005, 4.0))
moves.append(Move(None, None, 0.05, 8))
moves.append(Move(1.907, 1.207, 0.05, 8))
moves.append(Move(None, None, -0.005, 4.0))
moves.append(Move(2.052, 1.207, -0.005, 4.0))
moves.append(Move(2.052, 1.122, -0.005, 4.0))
moves.append(Move(1.907, 1.122, -0.005, 4.0))
moves.append(Move(1.907, 1.207, -0.005, 4.0))
moves.append(Move(None, None, 0.05, 8))
moves.append(Move(1.387, 1.207, 0.05, 8))
moves.append(Move(None, None, -0.005, 4.0))
moves.append(Move(1.532, 1.207, -0.005, 4.0))
moves.append(Move(1.532, 1.122, -0.005, 4.0))
moves.append(Move(1.387, 1.122, -0.005, 4.0))
moves.append(Move(1.387, 1.207, -0.005, 4.0))
moves.append(Move(None, None, 0.05, 8))
moves.append(Move(1.127, 1.227, 0.05, 8))
moves.append(Move(None, None, -0.005, 4.0))
moves.append(Move(1.212, 1.227, -0.005, 4.0))
moves.append(Move(1.212, 1.082, -0.005, 4.0))
moves.append(Move(1.127, 1.082, -0.005, 4.0))
moves.append(Move(1.127, 1.227, -0.005, 4.0))
moves.append(Move(None, None, 0.05, 8))
moves.append(Move(1.562, 1.597, 0.05, 8))
moves.append(Move(None, None, -0.005, 4.0))
moves.append(Move(1.557, 1.602, -0.005, 4.0))
moves.append(Move(1.517, 1.602, -0.005, 4.0))
moves.append(Move(1.517, 1.632, -0.005, 4.0))
moves.append(Move(1.497, 1.632, -0.005, 4.0))
moves.append(Move(1.497, 1.622, -0.005, 4.0))
moves.append(Move(1.342, 1.622, -0.005, 4.0))
moves.append(Move(1.342, 1.662, -0.005, 4.0))
moves.append(Move(1.497, 1.662, -0.005, 4.0))
moves.append(Move(1.497, 1.652, -0.005, 4.0))
moves.append(Move(1.542, 1.652, -0.005, 4.0))
moves.append(Move(1.542, 1.627, -0.005, 4.0))
moves.append(Move(1.562, 1.627, -0.005, 4.0))
moves.append(Move(1.567, 1.632, -0.005, 4.0))
run_app(moves)
