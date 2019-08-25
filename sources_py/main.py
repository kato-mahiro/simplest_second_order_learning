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

    @property
    def fitness(self):
        try:
            return self.num_correct_answer / LIFETIME_NUM
        except:
            return 0.0

    def make_initial_state(self):
        self.nn.connections = self.original_connections
        self.nn.mask_array = self.original_mask_array

if __name__=='__main__':
    args = sys.argv
    print(args)
    print(args[1])
    agents = [Agent() for i in range(POPULATION_NUM)]
    for g_num in range(GENERATION_NUM):
        if args[1] == '0':
            task = Task(g_num)
        elif args[1] == '1':
            task = Task_1(g_num)
        elif args[1] == '2':
            task = Task_2(g_num)
        elif args[1] == '3':
            task = Task_3(g_num)
        elif args[1] == '4':
            task = Task_4(g_num)
        elif args[1] == '5':
            task = Task_5(g_num)
        elif args[1] == '6':
            task = Task_6(g_num)
        elif args[1] == '7':
            task = Task_7(g_num)
            
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
            agents[a_num].num_correct_answer = 0
            agents[a_num].nn.connections = copy.deepcopy(agents[a_num].initial_connections)

        # evolution
        next_agents=[]
        fitness_list = []
        agents = sorted(agents, key=attrgetter('fitness'), reverse=True)
        for i in range(POPULATION_NUM):
            fitness_list.append(agents[i].fitness)
        print('generation: ',g_num+1)
        print('max: ',fitness_list[0])
        print('ave: ',sum(fitness_list)/len(fitness_list))
        next_agents = copy.deepcopy(agents[0:4]) #エリート選択
        for i in range(POPULATION_NUM - 4):
            parent_A = random.choices(agents, weights = fitness_list)[0]
            parent_B = random.choices(agents, weights = fitness_list)[0]
            new_Agent = copy.deepcopy(parent_A)
            for r in range(new_Agent.nn.num_of_neuron):
                for c in range(new_Agent.nn.num_of_neuron):
                    new_Agent.nn.connections[r][c] = \
                    random.choice([ parent_A.nn.connections[r][c], parent_B.nn.connections[r][c] ])
                    #if(random.random() < 0.001):
                        #new_Agent.nn.connections[r][c] += random.uniform(-0.1,0.1)
                new_Agent.nn.neurons[r].bias = \
                random.choice( [ parent_A.nn.neurons[r].bias, parent_B.nn.neurons[r].bias ])
                #if(random.random() < 0.001):
                    #new_Agent.nn.neurons[r].bias += random.uniform(-0.1,0.1)
                #new_Agent.nn.A = random.choice([ parent_A.nn.A ,parent_B.nn.A ])
                #new_Agent.nn.B = random.choice([ parent_A.nn.B ,parent_B.nn.B ])
                #new_Agent.nn.C = random.choice([ parent_A.nn.C ,parent_B.nn.C ])
                #new_Agent.nn.D = random.choice([ parent_A.nn.D ,parent_B.nn.D ])
            next_agents.append(copy.deepcopy(new_Agent))
        agents = next_agents
