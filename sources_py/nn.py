import random
from enum import Enum

class Type(Enum):
    INPUT = 1
    HIDDEN = 2
    OUTPUT = 3
    MODURATION = 4

class Neuron:
    def __init__(self, neuron_type:Type):
        self.neuron_type = Type
        self.bias = random.random(-1.0, 1.0)
        self.activation = 0.0
        self.moduration = 0.0

class NeuralNetwork:
