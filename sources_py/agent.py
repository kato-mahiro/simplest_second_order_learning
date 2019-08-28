import copy

from const import *
from nn import *

class NeuralNetworkAgent:
    def __init__(self):
        self.nn = NeuralNetwork()
        self.nn.push_neuron(Neuron(NeuronType.INPUT))
        self.nn.push_neuron(Neuron(NeuronType.INPUT))
        self.nn.push_neuron(Neuron(NeuronType.INPUT))
        self.nn.push_neuron(Neuron(NeuronType.INPUT))
        self.nn.push_neuron(Neuron(NeuronType.OUTPUT))
        self.nn.push_neuron(Neuron(NeuronType.OUTPUT))
        self.nn.push_neuron(Neuron(NeuronType.HIDDEN))
        self.nn.push_neuron(Neuron(NeuronType.HIDDEN))

        self.original_connections = copy.deepcopy(self.nn.connections)
        self.original_mask_array = copy.deepcopy(self.nn.mask_array)

        self.num_correct_answer = 0
        self.fitness = 0.0

        self.lifelog = []

    def revert_to_initial_state(self):
        self.nn.connections = self.original_connections
        self.nn.mask_array = self.original_mask_array
        self.num_correct_answer = 0

    def mutate(self):
        for r in range(self.nn.num_of_neuron):
            for c in range(self.nn.num_of_neuron):
                if(random.random() < MUTATION_PROB):
                    self.nn.connections[r][c] += random.uniform(-0.1,0.1)
                    self.nn.mask_array[r][c] = random.choice([0,1])
            if(random.random() < MUTATION_PROB):
                self.nn.neurons[r].bias += random.uniform(-0.1,0.1)

    def crossover(self,agent_B):
        new_agent = copy.deepcopy(self)
        for r in range(self.nn.num_of_neuron):
            for c in range(self.nn.num_of_neuron):
                new_agent.nn.connections[r][c], new_agent.nn.mask_array[r][c] = \
                random.choice([ [self.nn.connections[r][c],self.nn.mask_array[r][c]] ,\
                                [agent_B.nn.connections[r][c],agent_B.nn.mask_array[r][c]] ])

            new_agent.nn.neurons[r].bias = \
            random.choice( [ self.nn.neurons[r].bias, agent_B.nn.neurons[r].bias ])
        return new_agent

class HebbianNetworkAgent(NeuralNetworkAgent):
    def __init__(self):
        self.nn = HebbianNetwork()
        self.nn.push_neuron(Neuron(NeuronType.INPUT))
        self.nn.push_neuron(Neuron(NeuronType.INPUT))
        self.nn.push_neuron(Neuron(NeuronType.INPUT))
        self.nn.push_neuron(Neuron(NeuronType.INPUT))
        self.nn.push_neuron(Neuron(NeuronType.OUTPUT))
        self.nn.push_neuron(Neuron(NeuronType.OUTPUT))
        self.nn.push_neuron(Neuron(NeuronType.HIDDEN))
        self.nn.push_neuron(Neuron(NeuronType.HIDDEN))

        self.original_connections = copy.deepcopy(self.nn.connections)
        self.original_mask_array = copy.deepcopy(self.nn.mask_array)

        self.num_correct_answer = 0
        self.fitness = 0.0

        self.lifelog = []

class ModulatedHebbianNetworkAgent_1(NeuralNetworkAgent):
    def __init__(self):
        self.nn = ModulatedHebbianNetwork()
        self.nn.push_neuron(Neuron(NeuronType.INPUT))
        self.nn.push_neuron(Neuron(NeuronType.INPUT))
        self.nn.push_neuron(Neuron(NeuronType.INPUT))
        self.nn.push_neuron(Neuron(NeuronType.INPUT))
        self.nn.push_neuron(Neuron(NeuronType.OUTPUT))
        self.nn.push_neuron(Neuron(NeuronType.OUTPUT))
        self.nn.push_neuron(Neuron(NeuronType.HIDDEN))
        self.nn.push_neuron(Neuron(NeuronType.MODULATION))

        self.original_connections = copy.deepcopy(self.nn.connections)
        self.original_mask_array = copy.deepcopy(self.nn.mask_array)

        self.num_correct_answer = 0
        self.fitness = 0.0

        self.lifelog = []

class ModulatedHebbianNetworkAgent_2(NeuralNetworkAgent):
    def __init__(self):
        self.nn = ModulatedHebbianNetwork()
        self.nn.push_neuron(Neuron(NeuronType.INPUT))
        self.nn.push_neuron(Neuron(NeuronType.INPUT))
        self.nn.push_neuron(Neuron(NeuronType.INPUT))
        self.nn.push_neuron(Neuron(NeuronType.INPUT))
        self.nn.push_neuron(Neuron(NeuronType.OUTPUT))
        self.nn.push_neuron(Neuron(NeuronType.OUTPUT))
        self.nn.push_neuron(Neuron(NeuronType.MODULATION))
        self.nn.push_neuron(Neuron(NeuronType.MODULATION))

        self.original_connections = copy.deepcopy(self.nn.connections)
        self.original_mask_array = copy.deepcopy(self.nn.mask_array)

        self.num_correct_answer = 0
        self.fitness = 0.0

        self.lifelog = []

class ExtendedHebbianNetworkAgent(NeuralNetworkAgent):
    def __init__(self):
        self.nn = ExtendedHebbianNetwork()
        self.nn.push_neuron(Neuron(NeuronType.INPUT))
        self.nn.push_neuron(Neuron(NeuronType.INPUT))
        self.nn.push_neuron(Neuron(NeuronType.INPUT))
        self.nn.push_neuron(Neuron(NeuronType.INPUT))
        self.nn.push_neuron(Neuron(NeuronType.OUTPUT))
        self.nn.push_neuron(Neuron(NeuronType.OUTPUT))
        self.nn.push_neuron(Neuron(NeuronType.HIDDEN))
        self.nn.push_neuron(Neuron(NeuronType.HIDDEN))

        self.original_connections = copy.deepcopy(self.nn.connections)
        self.original_mask_array = copy.deepcopy(self.nn.mask_array)
        self.original_A = self.nn.A
        self.original_B = self.nn.B
        self.original_C = self.nn.C
        self.original_D = self.nn.D

        self.num_correct_answer = 0
        self.fitness = 0.0

        self.lifelog = []

    def revert_to_initial_state(self):
        self.nn.connections = self.original_connections
        self.nn.mask_array = self.original_mask_array
        self.nn.A = self.original_A
        self.nn.B = self.original_B
        self.nn.C = self.original_C
        self.nn.D = self.original_D
        self.num_correct_answer = 0

    def mutate(self):
        for r in range(self.nn.num_of_neuron):
            for c in range(self.nn.num_of_neuron):
                if(random.random() < MUTATION_PROB):
                    self.nn.connections[r][c] += random.uniform(-0.1,0.1)
                    self.nn.mask_array[r][c] = random.choice([0,1])
            if(random.random() < MUTATION_PROB):
                self.nn.neurons[r].bias += random.uniform(-0.1,0.1)

        if(random.random() < MUTATION_PROB):
            self.nn.A += random.uniform(-0.1,0.1)
        if(random.random() < MUTATION_PROB):
            self.nn.B += random.uniform(-0.1,0.1)
        if(random.random() < MUTATION_PROB):
            self.nn.C += random.uniform(-0.1,0.1)
        if(random.random() < MUTATION_PROB):
            self.nn.D += random.uniform(-0.1,0.1)

    def crossover(self,agent_B):
        new_agent = copy.deepcopy(self)
        for r in range(self.nn.num_of_neuron):
            for c in range(self.nn.num_of_neuron):
                new_agent.nn.connections[r][c], new_agent.nn.mask_array[r][c] = \
                random.choice([ [self.nn.connections[r][c],self.nn.mask_array[r][c]] ,\
                                [agent_B.nn.connections[r][c],agent_B.nn.mask_array[r][c]] ])

            new_agent.nn.neurons[r].bias = \
            random.choice( [ self.nn.neurons[r].bias, agent_B.nn.neurons[r].bias ])

        new_agent.nn.A = random.choice([self.nn.A, agent_B.nn.A])
        new_agent.nn.B = random.choice([self.nn.B, agent_B.nn.B])
        new_agent.nn.C = random.choice([self.nn.C, agent_B.nn.C])
        new_agent.nn.D = random.choice([self.nn.D, agent_B.nn.D])

        return new_agent

class ModulatedExtendedHebbianNetworkAgent_1(ExtendedHebbianNetworkAgent):
    def __init__(self):
        self.nn = ModulatedExtendedHebbianNetwork()
        self.nn.push_neuron(Neuron(NeuronType.INPUT))
        self.nn.push_neuron(Neuron(NeuronType.INPUT))
        self.nn.push_neuron(Neuron(NeuronType.INPUT))
        self.nn.push_neuron(Neuron(NeuronType.INPUT))
        self.nn.push_neuron(Neuron(NeuronType.OUTPUT))
        self.nn.push_neuron(Neuron(NeuronType.OUTPUT))
        self.nn.push_neuron(Neuron(NeuronType.HIDDEN))
        self.nn.push_neuron(Neuron(NeuronType.MODULATION))

        self.original_connections = copy.deepcopy(self.nn.connections)
        self.original_mask_array = copy.deepcopy(self.nn.mask_array)
        self.original_A = self.nn.A
        self.original_B = self.nn.B
        self.original_C = self.nn.C
        self.original_D = self.nn.D

        self.num_correct_answer = 0
        self.fitness = 0.0

        self.lifelog = []

class ModulatedExtendedHebbianNetworkAgent_2(ExtendedHebbianNetworkAgent):
    def __init__(self):
        self.nn = ModulatedExtendedHebbianNetwork()
        self.nn.push_neuron(Neuron(NeuronType.INPUT))
        self.nn.push_neuron(Neuron(NeuronType.INPUT))
        self.nn.push_neuron(Neuron(NeuronType.INPUT))
        self.nn.push_neuron(Neuron(NeuronType.INPUT))
        self.nn.push_neuron(Neuron(NeuronType.OUTPUT))
        self.nn.push_neuron(Neuron(NeuronType.OUTPUT))
        self.nn.push_neuron(Neuron(NeuronType.MODULATION))
        self.nn.push_neuron(Neuron(NeuronType.MODULATION))

        self.original_connections = copy.deepcopy(self.nn.connections)
        self.original_mask_array = copy.deepcopy(self.nn.mask_array)
        self.original_A = self.nn.A
        self.original_B = self.nn.B
        self.original_C = self.nn.C
        self.original_D = self.nn.D

        self.num_correct_answer = 0
        self.fitness = 0.0

        self.num_correct_answer = 0
        self.fitness = 0.0

        self.lifelog = []

if __name__=='__main__':
    a = NeuralNetworkAgent()
    print("--a--")
    print(a.nn.mask_array)
    b = NeuralNetworkAgent()
    print("--b--")
    print(b.nn.mask_array)

    #a.mutate()
    #print("--a--")
    #print(a.nn.mask_array)

    c = a.crossover(b)
    print("-a+b-")

    print(c.nn.mask_array)
    print("--a--")
    print(a.nn.mask_array)
