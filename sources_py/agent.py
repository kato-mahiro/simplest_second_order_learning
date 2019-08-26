from const import *
from nn import *

class Agent:
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

    def make_initial_state(self):
        self.nn.connections = self.original_connections
        self.nn.mask_array = self.original_mask_array

    def make_mutation(self):
        for r in range(self.nn.num_of_neuron):
            for c in range(self.nn.num_of_neuron):
                self.nn.connections[r][c] = \
                self.nn.mask_array[r][c] = \
                if(random.random() < MUTATION_PROB):
                    self.nn.connections[r][c] += random.uniform(-0.1,0.1)
                    self.nn.mask_array[r][c] = random.choice([0,1])
            if(random.random() < MUTATION_PROB):
            self.nn.neurons[r].bias += random.uniform(-0.1,0.1)

    def mutate(self):
        #突然変異を行う関数です。
        pass

    def crossover(self,agent_B)]
        #Agent_Bと交叉を行い、子孫を返す関数です
        pass
