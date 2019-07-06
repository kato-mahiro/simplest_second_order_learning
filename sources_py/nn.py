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

    def set_activation(self,input_val):
        if self.neuron_type != 1:
            raise Exception('Error you are setting activation of non input neuron(at Neuron.set_activation() ) ')
        self.activation = input_val

class NeuralNetwork:
    def __init__(self):
        self.num_of_neuron = 0
        self.neurons = []
        self.connections = np.zeros((self.num_of_neuron, self.num_of_neuron))

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

    def pop_neuron(self, idx):
        pass

    def update_activation(self):
        pass

if __name__=='__main__':
    nn = NeuralNetwork()
    nn.push_neuron(Neuron(NeuronType.INPUT))
    print(nn.activation_vector)
    nn.push_neuron(Neuron(NeuronType.HIDDEN))
    nn.push_neuron(Neuron(NeuronType.OUTPUT))
    nn.push_neuron(Neuron(NeuronType.MODURATION))
    print(nn.neurons[0].neuron_type)
    print(nn.neurons[1].neuron_type)
    print(nn.neurons[2].neuron_type)
    print(nn.neurons[3].neuron_type)
    print(nn.num_of_neuron)
    print(nn.activation_vector)
