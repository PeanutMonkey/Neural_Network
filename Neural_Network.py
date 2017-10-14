#we want to build a neural network from scratch that we can train

import numpy as np
import math as math
import random as rand

class Neuron:
    
    def __init__(self, ancestors):
        #ancestors is the number of weights associated with each neuron
        #initialize the vector of weights w with each entry in the range (-1,1)
        self.w = np.random.uniform(-1,1,ancestors)
        
    def forwardpass(self, x):
        dotpdt = np.dot(self.w,x)
        sigmoid = 1/(1+ math.exp(-dotpdt))
        return sigmoid
  

d = np.array([-1,3,1])              
neuron1 = Neuron(3)
print neuron1.forwardpass(d)