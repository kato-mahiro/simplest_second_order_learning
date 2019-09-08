from operator import attrgetter
import copy
import sys
import pickle
from const import *
from nn import *
from task import *
from agent import *

if __name__=='__main__':
    args = sys.argv
    if args[1] == 'N':
        agents = [NeuralNetworkAgent() for i in range(POPULATION_NUM)]
    elif args[1] == 'H':
        agents = [HebbianNetworkAgent() for i in range(POPULATION_NUM)]
    elif args[1] == 'M1H':
        agents = [ModulatedHebbianNetworkAgent_1() for i in range(POPULATION_NUM)]
    elif args[1] == 'M2H':
        agents = [ModulatedHebbianNetworkAgent_2() for i in range(POPULATION_NUM)]
    elif args[1] == 'EH':
        agents = [ExtendedHebbianNetworkAgent() for i in range(POPULATION_NUM)]
    elif args[1] == 'M1EH':
        agents = [ModulatedExtendedHebbianNetworkAgent_1() for i in range(POPULATION_NUM)]
    elif args[1] == 'M2EH':
        agents = [ModulatedExtendedHebbianNetworkAgent_2() for i in range(POPULATION_NUM)]
    elif args[1] == 'FH':
        agents = [FreeHebbianNetworkAgent() for i in range(POPULATION_NUM)]
    elif args[1] == 'FEH':
        agents = [FreeExtendedHebbianNetworkAgent() for i in range(POPULATION_NUM)]

    for g_num in range(GENERATION_NUM):

        if args[2] == '1':
            task = Task_1(g_num)
        elif args[2] == '2':
            task = Task_2(g_num)
        elif args[2] == '3':
            task = Task_3(g_num)
        elif args[2] == '4':
            task = Task_4(g_num)
        elif args[2] == '5':
            task = Task_5(g_num)
        elif args[2] == '6':
            task = Task_6(g_num)
        elif args[2] == '7':
            task = Task_7(g_num)
        elif args[2] == '8':
            task = Task_8(g_num)

        for a_num in range(POPULATION_NUM):
            for l_num in range(LIFETIME_NUM):
                q_v,a_v = task.question()
                result = agents[a_num].nn.get_output(q_v)
                reshaped_result = [0,0]
                try:
                    reshaped_result[result.index(max(result))] = 1
                except:
                    print("ここ")
                    print(result)
                    agents[a_num].self_introduction()
                    exit()
                if(reshaped_result == a_v):
                    agents[a_num].num_correct_answer +=1
                    agents[a_num].answer_history.append(1)
                    agents[a_num].nn.get_output(task.feedback(True))
                else:
                    agents[a_num].answer_history.append(0)
                    agents[a_num].nn.get_output(task.feedback(False))
            agents[a_num].fitness = agents[a_num].num_correct_answer / LIFETIME_NUM
            agents[a_num].num_correct_answer = 0.0
            agents[a_num].revert_initial_state()

        # evolution
        next_agents=[]
        fitness_list = []
        agents = sorted(agents, key=attrgetter('fitness'), reverse=True)
        for i in range(POPULATION_NUM):
            fitness_list.append(agents[i].fitness)

        num_of_perfect_ind = 0
        num_of_not_perfect_ind = 0

        print(' --- generation: ',g_num+1, '---')
        print('max: ',fitness_list[0])
        print('min: ',fitness_list[-1])
        print('ave: ',sum(fitness_list)/len(fitness_list))

        for a_num in range(POPULATION_NUM):
            if agents[a_num].fitness == 1.0:
                num_of_perfect_ind += 1
            else:
                num_of_not_perfect_ind += 1

        print('perfect: ',num_of_perfect_ind)
        print('not_perfect: ',num_of_not_perfect_ind)
        print('history_of_best:',agents[0].correct_answer_rate_history)
        print('history_of_worst:',agents[-1].correct_answer_rate_history)

        for a_num in range(POPULATION_NUM):
            agents[a_num].answer_history = []

        n_sum = 0
        h_sum = 0
        m_sum = 0
        for a_num in range(POPULATION_NUM):
            n_sum += agents[a_num].nn.num_of_neuron
            h_sum += agents[a_num].nn.num_of_hidden_neuron
            m_sum += agents[a_num].nn.num_of_modulation_neuron
        print('average_num_of_neuron', n_sum / POPULATION_NUM)
        print('average_num_of_hidden_neuron', h_sum / POPULATION_NUM)
        print('average_num_of_modulation_neuron', m_sum / POPULATION_NUM)

        # if the last generation of evolution, see best individual and pickle agents
        if(g_num == GENERATION_NUM-1):
            agents[0].self_introduction()
            pickle_string = agents[0].__class__.__name__  + '_' + task.__class__.__name__ + '.pickle'
            with open(pickle_string,'wb') as f:
                pickle.dump(agents,f)

        next_agents = copy.deepcopy(agents[0:ELITE_NUM]) #エリート選択
        for i in range(POPULATION_NUM - ELITE_NUM):

            if args[1] == 'FH' or args[1] == 'FEH':
                new_agent = copy.deepcopy(random.choices(agents, weights = fitness_list)[0])
                new_agent.mutate()
            else:
                parent_A = random.choices(agents, weights = fitness_list)[0]
                parent_B = random.choices(agents, weights = fitness_list)[0]
                new_agent = parent_A.crossover(parent_B)
                new_agent.mutate()
            new_agent.get_initial_state()
            next_agents.append(new_agent)

        agents = next_agents
