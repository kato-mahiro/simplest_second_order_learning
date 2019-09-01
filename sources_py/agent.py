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

        self.answer_history = []

    @property
    def correct_answer_rate_history(self):
        l = LIFETIME_NUM // 4
        rate_1 = sum(self.answer_history[0:l]) / l
        rate_2 = sum(self.answer_history[l:l*2]) / l
        rate_3 = sum(self.answer_history[l*2:l*3]) / l
        rate_4 = sum(self.answer_history[l*3:l*4]) / l
        return [rate_1, rate_2, rate_3, rate_4]

    @property
    def is_exis_learning_ability(self):
        if self.correct_answer_rate_history[3] == self.correct_answer_rate_history[0] == 1.0:
            return 'unknown'
        elif self.correct_answer_rate_history[3] - self.correct_answer_rate_history[0] > 0.0:
            return 'yes'
        else:
            return 'no'

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

    def self_introduction(self):
        print(" === This is my self introduction !! === ")
        print("I am ", self.__class__.__name__)
        print("My original_connections:")
        print(self.original_connections)
        print("My original_mask_array:")
        print(self.original_mask_array)
        print("My fitness was ",self.fitness)
        print(" ====================================== ")

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

        self.answer_history = []

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

        self.answer_history = []

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

        self.answer_history = []

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

        self.answer_history = []

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

    def self_introduction(self):
        print(" === This is my self introduction !! === ")
        print("I am ", self.__class__.__name__)
        print("My original_connections:")
        print(self.original_connections)
        print("My original_mask_array:")
        print(self.original_mask_array)
        print("My evolutional parameters A,B,C,D :")
        print(self.original_A,self.original_B,self.original_C,self.original_D)
        print("My fitness was ",self.fitness)
        print(" ====================================== ")

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

        self.answer_history = []

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

        self.answer_history = []

if __name__=='__main__':
    a = ExtendedHebbianNetworkAgent()
    print("--a--")
    print(a.nn.mask_array)
    b = ExtendedHebbianNetworkAgent()
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

    a.self_introduction()
