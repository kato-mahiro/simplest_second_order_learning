from operator import attrgetter
import copy
import sys
from const import *
from nn import *
from task import *

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

if __name__=='__main__':
    agents = [Agent() for i in range(POPULATION_NUM)]
    for g_num in range(GENERATION_NUM):
        task = Task_1(g_num)

        for a_num in range(POPULATION_NUM):
            for l_num in range(LIFETIME_NUM):
                q_v,a_v = task.question()
                result = agents[a_num].nn.get_output(q_v)
                reshaped_result = [0,0]
                reshaped_result[result.index(max(result))] = 1
                if(reshaped_result == a_v):
                    agents[a_num].num_correct_answer +=1
                    agents[a_num].nn.get_output(task.feedback(True))
                else:
                    agents[a_num].nn.get_output(task.feedback(False))
            agents[a_num].fitness = agents[a_num].num_correct_answer / LIFETIME_NUM
            agents[a_num].make_initial_state()

        # evolution
        next_agents=[]
        fitness_list = []
        agents = sorted(agents, key=attrgetter('fitness'), reverse=True)
        for i in range(POPULATION_NUM):
            fitness_list.append(agents[i].fitness)
        print('generation: ',g_num+1)
        print('max: ',fitness_list[0])
        print('min: ',fitness_list[-1])
        print('ave: ',sum(fitness_list)/len(fitness_list))
        next_agents = copy.deepcopy(agents[0:ELITE_NUM]) #エリート選択
        for i in range(POPULATION_NUM - ELITE_NUM):
            parent_A = random.choices(agents, weights = fitness_list)[0]
            parent_B = random.choices(agents, weights = fitness_list)[0]
            new_Agent = copy.deepcopy(parent_A)
            for r in range(new_Agent.nn.num_of_neuron):
                for c in range(new_Agent.nn.num_of_neuron):
                    new_Agent.nn.connections[r][c] = \
                    random.choice([ parent_A.nn.connections[r][c], parent_B.nn.connections[r][c] ])
                    new_Agent.nn.mask_array[r][c] = \
                    random.choice([ parent_A.nn.mask_array[r][c], parent_B.nn.mask_array[r][c] ])

                new_Agent.nn.neurons[r].bias = \
                random.choice( [ parent_A.nn.neurons[r].bias, parent_B.nn.neurons[r].bias ])

            new_Agent.make_mutation()
            next_agents.append(copy.deepcopy(new_Agent))
        agents = next_agents
