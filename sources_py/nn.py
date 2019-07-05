import numpy as np
import random
from enum import Enum

from const import *

class NeuronType(Enum):
    INPUT = 1
    HIDDEN = 2
    OUTPUT = 3
    MODURATION = 4

class Neuron:
    def __init__(self, neuron_type:NeuronType):
        self.neuron_type = neuron_type
        self.bias = random.uniform(BIAS_LOWER_LIMIT, BIAS_UPPER_LIMIT)
        self.activation = 0.0
        self.moduration = 0.0

class NeuralNetwork:
    def __init__(self):
        self.num_of_neuron = 0
        self.neurons = []
        self.moduration_vector = []
        self.connections = np.zeros((self.num_of_neuron, self.num_of_neuron))

    def push_neuron(self, neuron):
        if(not type(neuron) == Neuron):
            raise Exception('Type error at NeuralNetwork.push_neuron()')
        self.num_of_neuron += 1
        self.neurons.append(neuron)
        connections_list = self.connections.tolist()
        connections_list.append( [random.uniform(WEIGHT_LOWER_LIMIT, WEIGHT_UPPER_LIMIT) for i in range(self.num_of_neuron-1) ])
        for i in range(self.num_of_neuron):
            connections_list[i].append( random.uniform(WEIGHT_LOWER_LIMIT, WEIGHT_UPPER_LIMIT) )
        self.connections = np.array(connections_list)

    def del_neuron(self, idx):
        pass

    @property
    def activation_vector(self):
        activation_vector = []
        for i in range(self.num_of_neuron):
            activation_vector.append(self.neurons[i].activation)
        return activation_vector

    @property
    def moduration_vector(self):
        moduration_vector = []
        for i in range(self.num_of_neuron):
            moduration_vector.append(self.neurons[i].moduration)
        return moduration_vector

if __name__=='__main__':
    n1 = Neuron( NeuronType.INPUT )
    n2 = Neuron( NeuronType.MODURATION)
    n3 = Neuron( NeuronType.MODURATION)
    print(n1.neuron_type, n1.bias, n1.activation, n1.moduration)
    print(n1.neuron_type.name)

    nn1 = NeuralNetwork()
    nn1.push_neuron(n1)
    nn1.push_neuron(n2)
    nn1.push_neuron(n3)
    print(nn1.num_of_neuron)
    print(nn1.activation_vector)
