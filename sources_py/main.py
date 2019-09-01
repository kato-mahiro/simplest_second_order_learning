from operator import attrgetter
import copy
import sys
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

        for a_num in range(POPULATION_NUM):
            for l_num in range(LIFETIME_NUM):
                q_v,a_v = task.question()
                result = agents[a_num].nn.get_output(q_v)
                reshaped_result = [0,0]
                reshaped_result[result.index(max(result))] = 1
                if(reshaped_result == a_v):
                    agents[a_num].num_correct_answer +=1
                    agents[a_num].answer_history.append(1)
                    agents[a_num].nn.get_output(task.feedback(True))
                else:
                    agents[a_num].answer_history.append(0)
                    agents[a_num].nn.get_output(task.feedback(False))
            agents[a_num].fitness = agents[a_num].num_correct_answer / LIFETIME_NUM
            agents[a_num].revert_to_initial_state()

        # evolution
        next_agents=[]
        fitness_list = []
        learning_ability_list = []
        agents = sorted(agents, key=attrgetter('fitness'), reverse=True)
        for i in range(POPULATION_NUM):
            fitness_list.append(agents[i].fitness)


        print(' --- generation: ',g_num+1, '---')
        print('max: ',fitness_list[0])
        print('min: ',fitness_list[-1])
        print('ave: ',sum(fitness_list)/len(fitness_list))

        for a_num in range(POPULATION_NUM):
            learning_ability_list.append(agents[a_num].is_exis_learning_ability)

        print('can_learning: ', learning_ability_list.count('yes'))
        print('cannot_learning: ', learning_ability_list.count('no'))
        print('perfect: ', learning_ability_list.count('unknown'))
        
        learning_ability_list = []
        #print('history_of_best:',agents[0].correct_answer_rate_history)
        #print(agents[0].is_exis_learning_ability)
        #print('history_of_worst:',agents[-1].correct_answer_rate_history)

        for a_num in range(POPULATION_NUM):
            agents[a_num].answer_history = []


        next_agents = copy.deepcopy(agents[0:ELITE_NUM]) #エリート選択
        for i in range(POPULATION_NUM - ELITE_NUM):
            parent_A = random.choices(agents, weights = fitness_list)[0]
            parent_B = random.choices(agents, weights = fitness_list)[0]
            new_agent = parent_A.crossover(parent_B)
            new_agent.mutate()
            next_agents.append(new_agent)
        agents = next_agents
