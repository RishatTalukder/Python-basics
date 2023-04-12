import time
from numba import njit 

import random 
import math 

@njit()
def function(n):
    z= 0
    for i in range(n):
        x = random.random()
        y = random.random()
        z += math.sqrt(x**2 + y**2)
    
    return z 

start = time.time()
function(10000000)

end = time.time()

print(end-start)

start = time.time()
function(10000000)

end = time.time()

print(end-start)