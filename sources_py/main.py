from operator import attrgetter
import copy
import sys
from const import *
from nn import *
from task import *
from agent import *

if __name__=='__main__':
    agents = [ModulatedHebbianNetworkAgent_1() for i in range(POPULATION_NUM)]
    for g_num in range(GENERATION_NUM):
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
            agents[a_num].revert_to_initial_state()

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
            new_agent = parent_A.crossover(parent_B)
            new_agent.mutate()
            next_agents.append(new_agent)
        agents = next_agents
