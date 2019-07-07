import numpy as np
import math
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

class NeuralNetwork:
    def __init__(self,is_overwrite_input=True,is_self_connectoin=False):
        self.num_of_neuron = 0
        self.neurons = []
        self.connections = np.zeros((self.num_of_neuron, self.num_of_neuron))
        self.is_overwrite_input = is_overwrite_input
        self.is_self_connectoin = is_self_connectoin

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

    def make_self_connections_zero(self):
        if(self.is_self_connectoin == False):
            try:
                for r in range(self.num_of_neuron):
                    for l in range(self.num_of_neuron):
                        if r == l:
                            self.connections[r][l] = 0.0
            except:
                pass

    def push_neuron(self, neuron):
        if(not type(neuron) == Neuron):
            raise Exception('Type error at NeuralNetwork.push_neuron()')
        self.num_of_neuron += 1
        self.neurons.append(neuron)
        connections_list = self.connections.tolist()
        connections_list.append( [random.uniform(WEIGHT_LOWER_LIMIT, WEIGHT_UPPER_LIMIT) for i in range(self.num_of_neuron-1) ])
        for i in range(self.num_of_neuron):
            connections_list[i].append( random.uniform(WEIGHT_LOWER_LIMIT, WEIGHT_UPPER_LIMIT) )
        self.make_self_connections_zero()
        self.connections = np.array(connections_list)

    def pop_neuron(self, idx):
        pass

    def update_activations_and_modulations(self):
        input_v = np.array(self.activation_vector)
        result_v = np.dot(self.connections, input_v)
        for i in range (self.num_of_neuron):
            if self.neurons[i].neuron_type.name != 'MODULATION':
                self.neurons[i].activation = float(math.tanh(result_v[i] +self.neurons[i].bias))
            elif self.neurons[i].neuron_type.name == 'MODULATION':
                self.neurons[i].modulation = float(math.tanh(result_v[i] +self.neurons[i].bias))

    def get_output(self, input_vector):
        if len(input_vector) != self.num_of_input_neuron:
            raise Exception('invalid length of input_vector')
        for i in range(self.num_of_input_neuron):
            if self.neurons[i].neuron_type.name != 'INPUT':
                raise Exception('input neurons must be at the beginning')
            if self.is_overwrite_input == True:
                self.neurons[i].activation = input_vector[i]
            elif self.is_overwrite_input == False:
                self.neurons[i].activation += input_vector[i]
        self.update_activations_and_modulations()

        output_vector = []
        for i in range(self.num_of_output_neuron):
            if self.neurons[self.num_of_input_neuron +i].neuron_type.name != 'OUTPUT':
                raise Exception('output neurons must be at the next of input neurons in line.')
            output_vector.append(self.neurons[self.num_of_input_neuron +i].activation)
        return output_vector

class HebbianNetwork(NeuralNetwork):

    def hebbian_update(self, epsilon = EPSILON):
        for r in range(self.num_of_neuron):
            for c in range(self.num_of_neuron):
                self.connections[r][c] += epsilon * self.neurons[r].activation * self.neurons[c].activation
        self.make_self_connections_zero()

    def get_output(self, input_vector):
        if len(input_vector) != self.num_of_input_neuron:
            raise Exception('invalid length of input_vector')
        for i in range(self.num_of_input_neuron):
            if self.neurons[i].neuron_type.name != 'INPUT':
                raise Exception('input neurons must be at the beginning')
            if self.is_overwrite_input == True:
                self.neurons[i].activation = input_vector[i]
            elif self.is_overwrite_input == False:
                self.neurons[i].activation += input_vector[i]
        self.update_activations_and_modulations()

        self.hebbian_update()

        output_vector = []
        for i in range(self.num_of_output_neuron):
            if self.neurons[self.num_of_input_neuron +i].neuron_type.name != 'OUTPUT':
                raise Exception('output neurons must be at the next of input neurons in line.')
            output_vector.append(self.neurons[self.num_of_input_neuron +i].activation)
        return output_vector

class ExtendedHebbianNetwork(NeuralNetwork):
    def __init__(self,is_overwrite_input=True,is_self_connectoin=False):
        super(ExtendedHebbianNetwork,self).__init__(is_overwrite_input,is_self_connectoin)
        self.A = random.uniform(-1.0,1.0)
        self.B = random.uniform(-1.0,1.0)
        self.C = random.uniform(-1.0,1.0)
        self.D = random.uniform(-1.0,1.0)

    def extended_hebbian_update(self, epsilon = EPSILON):
        for r in range(self.num_of_neuron):
            for c in range(self.num_of_neuron):
                self.connections[r][c] += \
                self.A * self.neurons[r].activation * self.neurons[c].activation + \
                self.B * self.neurons[r].activation + \
                self.C * self.neurons[c].activation + \
                self.D
        self.make_self_connections_zero()

    def get_output(self, input_vector):
        if len(input_vector) != self.num_of_input_neuron:
            raise Exception('invalid length of input_vector')
        for i in range(self.num_of_input_neuron):
            if self.neurons[i].neuron_type.name != 'INPUT':
                raise Exception('input neurons must be at the beginning')
            if self.is_overwrite_input == True:
                self.neurons[i].activation = input_vector[i]
            elif self.is_overwrite_input == False:
                self.neurons[i].activation += input_vector[i]
        self.update_activations_and_modulations()

        self.extended_hebbian_update()

        output_vector = []
        for i in range(self.num_of_output_neuron):
            if self.neurons[self.num_of_input_neuron +i].neuron_type.name != 'OUTPUT':
                raise Exception('output neurons must be at the next of input neurons in line.')
            output_vector.append(self.neurons[self.num_of_input_neuron +i].activation)
        return output_vector

if __name__=='__main__':
    nn = ExtendedHebbianNetwork()
    nn.push_neuron(Neuron(NeuronType.INPUT))
    nn.push_neuron(Neuron(NeuronType.INPUT))
    nn.push_neuron(Neuron(NeuronType.OUTPUT))
    nn.push_neuron(Neuron(NeuronType.OUTPUT))

    print(nn.num_of_neuron)
    print(nn.A)

    print(nn.connections)
    print(nn.get_output([0,1]))
    print(nn.connections)
    print(nn.get_output([0,1]))
    print(nn.connections)
    print(nn.get_output([0,0]))
    print(nn.connections)
    print(nn.get_output([1,1]))
    print(nn.connections)
