import numpy as np
import random
from enum import Enum

from const import *

class NeuronType(Enum):
    INPUT = 1
    HIDDEN = 2
    OUTPUT = 3
    MODULATION = 4

class Neuron:
    def __init__(self, neuron_type:NeuronType):
        self.neuron_type = neuron_type
        self.bias = random.uniform(BIAS_LOWER_LIMIT, BIAS_UPPER_LIMIT)
        self.activation = 0.0
        self.modulation = 0.0

    def set_activation(self,input_val):
        if self.neuron_type != 1:
            raise Exception('Error you are setting activation of non input neuron(at Neuron.set_activation() ) ')
        self.activation = float(input_val)

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
    def modulation_vector(self):
        modulation_vector = []
        for i in range(self.num_of_neuron):
            modulation_vector.append(self.neurons[i].modulation)
        return modulation_vector

    @property
    def num_of_input_neuron(self):
        num = 0
        for i in range(self.num_of_neuron):
            if self.neurons[i].neuron_type.name == 'INPUT':
                num += 1
        return num

    @property
    def num_of_hidden_neuron(self):
        num = 0
        for i in range(self.num_of_neuron):
            if self.neurons[i].neuron_type.name == 'HIDDEN':
                num += 1
        return num

    @property
    def num_of_output_neuron(self):
        num = 0
        for i in range(self.num_of_neuron):
            if self.neurons[i].neuron_type.name == 'OUTPUT':
                num += 1
        return num

    @property
    def num_of_modulation_neuron(self):
        num = 0
        for i in range(self.num_of_neuron):
            if self.neurons[i].neuron_type.name == 'MODULATION':
                num += 1
        return num

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

    def update_activations_and_modulations(self):
        input_v = np.array(self.activation_vector)
        result_v = np.dot(self.connections, input_v)
        for i in range (self.num_of_neuron):
            if self.neurons[i].neuron_type.name != 'MODULATION':
                self.neurons[i].activation = float(result_v[i])
            elif self.neurons[i].neuron_type.name == 'MODULATION':
                self.neurons[i].modulation = float(result_v[i])

    def get_output(self, input_vector, overwrite_input = True):
        if len(input_vector) != self.num_of_input_neuron:
            raise Exception('invalid length of input_vector')
        for i in range(self.num_of_input_neuron):
            if self.neurons[i].neuron_type.name != 'INPUT':
                raise Exception('input neurons must be at the beginning')
            if overwrite_input == True:
                self.neurons[i].activation = input_vector[i]
            elif overwrite_input == False:
                self.neurons[i].activation += input_vector[i]
        self.update_activations_and_modulations()

        output_vector = []
        for i in range(self.num_of_output_neuron):
            if self.neurons[self.num_of_input_neuron +i].neuron_type.name != 'OUTPUT':
                raise Exception('output neurons must be at the next of input neurons in line.')
            output_vector.append(self.neurons[self.num_of_input_neuron +i].activation)
        return output_vector

if __name__=='__main__':
    nn = NeuralNetwork()
    nn.push_neuron(Neuron(NeuronType.INPUT))
    nn.push_neuron(Neuron(NeuronType.OUTPUT))
    nn.push_neuron(Neuron(NeuronType.OUTPUT))
    nn.push_neuron(Neuron(NeuronType.OUTPUT))
    nn.push_neuron(Neuron(NeuronType.OUTPUT))

    print(nn.connections)
    print(nn.get_output([0]))
    print(nn.get_output([1]))
