from typing import Tuple

import numpy as np


def get_motor_left_matrix(shape: Tuple[int, int]) -> np.ndarray:
  
    res = np.zeros(shape=shape, dtype="float32")
    #Main Goal: Detect duckies in short range, curve around them. 
    # the farther left/right a duckie is, the less difference -> bigger radius of the curve.
    
    res[250:480,500:580] = -0.5
    res[250:480,420:500] = -0.75
    res[250:480,320:420] = -1
    res[250:480,220:320] = 1 
    res[250:480,140:220] = 0.75
    res[250:480,60:140] = 0.5
   
    
    
    return res


def get_motor_right_matrix(shape: Tuple[int, int]) -> np.ndarray:
    # TODO: write your function instead of this one
    res = np.zeros(shape=shape, dtype="float32")
    #same goals as left Matrix, mirrored function

    res[250:480,60:140] = -0.5
    res[250:480,140:220] = -0.75
    res[250:480,220:320] = -1
    res[250:480,320:420] = 1
    res[250:480,420:500] = 0.75
    res[250:480,500:580] = 0.5
  
    
   
    return res
