import random
from enum import Enum

class CurrentRule(Enum):
    PIECE= 0
    EMERGENCY = 1

class CurrentState(Enum):
    SAFE = 0
    DANGER = 1

class Task:

    def get_current_rule(self):
        return CurrentRule.PIECE

    def get_current_state(self):
        return CurrentState.SAFE

    def question(self):
        current_rule = self.get_current_rule()
        print("ruleは",current_rule.name,"です")
        current_state = self.get_current_state()
        print("stateは",current_state.name,"です")
        if(current_state.name == 'SAFE'):
            if(current_rule.name == 'PIECE'):
                return([1,0,0,0],[1,0])
            elif(current_rule.name == 'EMERGENCY'):
                return([1,0,0,0],[0,1])
        elif(current_state.name == 'DANGER'):
            if(current_rule.name == 'PIECE'):
                return([0,1,0,0],[0,1])
            elif(current_rule.name == 'EMERGENCY'):
                return([0,1,0,0],[1,0])

    def feedback(self,is_correct_answer):
        if is_correct_answer == True:
            return [0,0,1,0]
        else:
            return [0,0,0,1]

class Task_1(Task): #Doesn't change rule
    def get_current_state(self):
        if(random.randint(0,1)):
            return CurrentState.SAFE
        else:
            return CurrentState.DANGER

class Task_2(Task_1): # Rule change randomly initialy.
    def __init__(self):
        if(random.randint(0,1)):
            self.rule = CurrentRule.PIECE
        else:
            self.rule = CurrentRule.EMERGENCY

    def get_current_rule(self):
        return self.rule

class Task_3(Task_1): # Rule change randomly by time.
    def get_current_rule(self):
        if(random.randint(0,1)):
            return CurrentRule.PIECE
        else:
            return CurrentRule.EMERGENCY

class Task_4(Task_1): # Rule change alternately every generation.
    def __init__(self,generation_num):
       self.generation_num = generation_num
    def get_current_rule(self):
        if(self.generation_num % 2):
            return CurrentRule.PIECE
        else:
            return CurrentRule.EMERGENCY

class Task_5(Task_1):
    def __init__(self):
        self.step = 0
    def get_current_rule(self):
        self.step += 1
        if(self.step % 2):
            return CurrentRule.PIECE
        else:
            return CurrentRule.EMERGENCY

class Task_6(Task_1):
    def __init__(self,generation_num):
       self.generation_num = generation_num //5
    def get_current_rule(self):
        if(self.generation_num % 2):
            return CurrentRule.PIECE
        else:
            return CurrentRule.EMERGENCY

class Task_7(Task_1):
    def __init__(self):
        self.step = -1
    def get_current_rule(self):
        self.step += 1
        if (self.step//5) % 2 == 0:
            return CurrentRule.PIECE
        else:
            return CurrentRule.EMERGENCY

if __name__=='__main__':
    task = Task_7()
    for i in range(100):
        print("question:",task.question())
        result = input()
        print(task.feedback(result))
