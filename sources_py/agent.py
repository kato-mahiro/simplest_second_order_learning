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
