import numpy as np
import math
import random
from enum import Enum
from const import *

random.seed(SEED)

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
    def __init__(self,is_overwrite_input=True):
        self.neurons = []
        self.connections = np.zeros((0, 0))
        self.mask_array = np.zeros((0, 0))
        self.is_overwrite_input = is_overwrite_input

    @property
    def num_of_neuron(self):
        return len(self.neurons)

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

    @property
    def num_of_active_connection(self):
        num = 0
        try:
            for i in range(self.num_of_neuron):
                for ii in range(self.num_of_neuron):
                    if self.mask_array[i][ii] == 1:
                        num += 1
        except:
            pass
        return num

    def make_masking(self):
        self.connections = self.connections * self.mask_array

    def push_neuron(self, neuron):
        if(not type(neuron) == Neuron):
            raise Exception('Type error at NeuralNetwork.push_neuron()')
        self.neurons.append(neuron)
        connections_list = self.connections.tolist()
        connections_list.append( [random.uniform(WEIGHT_LOWER_LIMIT, WEIGHT_UPPER_LIMIT) for i in range(self.num_of_neuron-1) ])
        for i in range(self.num_of_neuron):
            connections_list[i].append( random.uniform(WEIGHT_LOWER_LIMIT, WEIGHT_UPPER_LIMIT) )
        mask_list = self.mask_array.tolist()
        mask_list.append( [random.choices([0,1],[1.0 - ACTIVE_CONNECTION_RATIO, ACTIVE_CONNECTION_RATIO])[0] for i in range(self.num_of_neuron-1)] )
        for i in range(self.num_of_neuron):
            mask_list[i].append( random.choices([0,1],[1.0 - ACTIVE_CONNECTION_RATIO, ACTIVE_CONNECTION_RATIO])[0] )

        self.connections = np.array(connections_list)
        self.mask_array = np.array(mask_list)
        self.make_masking()

    def del_neuron(self, idx):
        try:
            del(self.neurons[idx])
        except:
            raise Exception('invalid index')
        self.connections = np.delete(self.connections, idx, axis = 0)
        self.connections = np.delete(self.connections, idx, axis = 1)
        self.mask_array = np.delete(self.mask_array, idx, axis = 0)
        self.mask_array = np.delete(self.mask_array, idx, axis = 1)

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
                if(self.connections[r][c] > WEIGHT_UPPER_LIMIT):
                    self.connections[r][c] = WEIGHT_UPPER_LIMIT 
                elif(self.connections[r][c] < WEIGHT_LOWER_LIMIT):
                    self.connections[r][c] = WEIGHT_LOWER_LIMIT
        self.make_masking()

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

class ModulatedHebbianNetwork(HebbianNetwork):
    def hebbian_update(self, epsilon = EPSILON):
        input_v = np.array(self.modulation_vector)
        m_v = np.dot(self.connections, input_v)
        for i in range (self.num_of_neuron):
            m_v[i] = float(math.tanh(m_v[i]))

        for r in range(self.num_of_neuron):
            for c in range(self.num_of_neuron):
                self.connections[r][c] += \
                    epsilon * self.neurons[r].activation * self.neurons[c].activation * m_v[r]
                if(self.connections[r][c] > WEIGHT_UPPER_LIMIT):
                    self.connections[r][c] = WEIGHT_UPPER_LIMIT
                elif(self.connections[r][c] < WEIGHT_LOWER_LIMIT):
                    self.connections[r][c] = WEIGHT_LOWER_LIMIT

        self.make_masking()

class FreeHebbianNetwork(HebbianNetwork):
    """
    Modulationニューロンの有り/無しによって自動的にupdateのやり方を切り替える
    """
    def hebbian_update(self, epsilon = EPSILON):
        if(self.num_of_modulation_neuron == 0):
            #HebbianNetworkの hebbian_update()
            for r in range(self.num_of_neuron):
                for c in range(self.num_of_neuron):
                    self.connections[r][c] += epsilon * self.neurons[r].activation * self.neurons[c].activation
                    if(self.connections[r][c] > WEIGHT_UPPER_LIMIT):
                        self.connections[r][c] = WEIGHT_UPPER_LIMIT 
                    elif(self.connections[r][c] < WEIGHT_LOWER_LIMIT):
                        self.connections[r][c] = WEIGHT_LOWER_LIMIT
            self.make_masking()

        elif(self.num_of_modulation_neuron > 0):
            #ModulatedHebbianNetworkのhebbian_update()
            input_v = np.array(self.modulation_vector)
            m_v = np.dot(self.connections, input_v)
            for i in range (self.num_of_neuron):
                m_v[i] = float(math.tanh(m_v[i]))

            for r in range(self.num_of_neuron):
                for c in range(self.num_of_neuron):
                    self.connections[r][c] += \
                        epsilon * self.neurons[r].activation * self.neurons[c].activation * m_v[r]
                    if(self.connections[r][c] > WEIGHT_UPPER_LIMIT):
                        self.connections[r][c] = WEIGHT_UPPER_LIMIT
                    elif(self.connections[r][c] < WEIGHT_LOWER_LIMIT):
                        self.connections[r][c] = WEIGHT_LOWER_LIMIT
            self.make_masking()
        else:
            raise Exception('num_of_modulation_neuron is invalid')


class ExtendedHebbianNetwork(NeuralNetwork):
    def __init__(self,is_overwrite_input=True):
        super(ExtendedHebbianNetwork,self).__init__(is_overwrite_input)
        self.A = random.uniform(-1.0,1.0)
        self.B = random.uniform(-1.0,1.0)
        self.C = random.uniform(-1.0,1.0)
        self.D = random.uniform(-1.0,1.0)

    def extended_hebbian_update(self):
        for r in range(self.num_of_neuron):
            for c in range(self.num_of_neuron):
                self.connections[r][c] += \
                self.A * self.neurons[r].activation * self.neurons[c].activation + \
                self.B * self.neurons[r].activation + \
                self.C * self.neurons[c].activation + \
                self.D
                if(self.connections[r][c] > WEIGHT_UPPER_LIMIT):
                    self.connections[r][c] = WEIGHT_UPPER_LIMIT 
                elif(self.connections[r][c] < WEIGHT_LOWER_LIMIT):
                    self.connections[r][c] = WEIGHT_LOWER_LIMIT
        self.make_masking()

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

class ModulatedExtendedHebbianNetwork(ExtendedHebbianNetwork):

    def extended_hebbian_update(self):
        input_v = np.array(self.modulation_vector)
        m_v = np.dot(self.connections, input_v)
        for i in range (self.num_of_neuron):
            m_v[i] = float(math.tanh(m_v[i]))

        for r in range(self.num_of_neuron):
            for c in range(self.num_of_neuron):
                self.connections[r][c] += \
                (\
                self.A * self.neurons[r].activation * self.neurons[c].activation + \
                self.B * self.neurons[r].activation + \
                self.C * self.neurons[c].activation + \
                self.D \
                ) \
                * m_v[r]
                if(self.connections[r][c] > WEIGHT_UPPER_LIMIT):
                    self.connections[r][c] = WEIGHT_UPPER_LIMIT
                elif(self.connections[r][c] < WEIGHT_LOWER_LIMIT):
                    self.connections[r][c] = WEIGHT_LOWER_LIMIT

        self.make_masking()

class FreeExtendedHebbianNetwork(ExtendedHebbianNetwork):

    def extended_hebbian_update(self):
        if(self.num_of_modulation_neuron == 0):
            for r in range(self.num_of_neuron):
                for c in range(self.num_of_neuron):
                    self.connections[r][c] += \
                    self.A * self.neurons[r].activation * self.neurons[c].activation + \
                    self.B * self.neurons[r].activation + \
                    self.C * self.neurons[c].activation + \
                    self.D
                    if(self.connections[r][c] > WEIGHT_UPPER_LIMIT):
                        self.connections[r][c] = WEIGHT_UPPER_LIMIT 
                    elif(self.connections[r][c] < WEIGHT_LOWER_LIMIT):
                        self.connections[r][c] = WEIGHT_LOWER_LIMIT
            self.make_masking()
        elif(self.num_of_modulation_neuron > 0):
            input_v = np.array(self.modulation_vector)
            m_v = np.dot(self.connections, input_v)
            for i in range (self.num_of_neuron):
                m_v[i] = float(math.tanh(m_v[i]))

            for r in range(self.num_of_neuron):
                for c in range(self.num_of_neuron):
                    self.connections[r][c] += \
                    (\
                    self.A * self.neurons[r].activation * self.neurons[c].activation + \
                    self.B * self.neurons[r].activation + \
                    self.C * self.neurons[c].activation + \
                    self.D \
                    ) \
                    * m_v[r]
                    if(self.connections[r][c] > WEIGHT_UPPER_LIMIT):
                        self.connections[r][c] = WEIGHT_UPPER_LIMIT
                    elif(self.connections[r][c] < WEIGHT_LOWER_LIMIT):
                        self.connections[r][c] = WEIGHT_LOWER_LIMIT
            self.make_masking()
        else:
            raise Exception('num_of_modulation_neuron is invalid')

if __name__=='__main__':
    nn = FreeExtendedHebbianNetwork()
    print(nn.num_of_neuron)

    print(nn.mask_array)
    print(nn.num_of_active_connection)
    nn.push_neuron(Neuron(NeuronType.INPUT))
    nn.push_neuron(Neuron(NeuronType.OUTPUT))
    nn.push_neuron(Neuron(NeuronType.OUTPUT))
    #nn.push_neuron(Neuron(NeuronType.MODULATION))

    print(nn.num_of_neuron)
    print(nn.connections)
    print(nn.get_output([0]))
    print(nn.connections)
    print(nn.get_output([0]))
    print(nn.connections)
    print(nn.get_output([0]))
    print(nn.connections)
    nn.push_neuron(Neuron(NeuronType.MODULATION))
    print(nn.get_output([1]))
    print(nn.connections)

    print(nn.mask_array)
    print(nn.num_of_active_connection)

    nn.del_neuron(1)

    print(nn.mask_array)
    print(nn.connections)
