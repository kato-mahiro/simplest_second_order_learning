from const import *
import random
from enum import Enum
random.seed(SEED)

class CurrentRule(Enum):
    PIECE= 0
    EMERGENCY = 1

class CurrentState(Enum):
    SAFE = 0
    DANGER = 1

class Task:
    def __init__(self,generation_num=0):
       self.generation_num = generation_num

    def get_current_rule(self):
        return CurrentRule.PIECE

    def get_current_state(self):
        return CurrentState.SAFE

    def question(self):
        current_rule = self.get_current_rule()
        current_state = self.get_current_state()
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
    def __init__(self,generation):
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
    def get_current_rule(self):
        if(self.generation_num % 2):
            return CurrentRule.PIECE
        else:
            return CurrentRule.EMERGENCY

class Task_5(Task_1):
    def __init__(self,generation_num):
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
    def __init__(self,generation_num):
        self.step = -1
    def get_current_rule(self):
        self.step += 1
        if (self.step//5) % 2 == 0:
            return CurrentRule.PIECE
        else:
            return CurrentRule.EMERGENCY

class Task_8(Task_1):
    #ルールが生涯のちょうど真ん中で変更されるタスク
    def __init__(self,generation_num):
        self.step = 0
    def get_current_rule(self):
        self.step += 1
        if self.step == LIFETIME_NUM +1:
            self.step = 1
        #print(self.step)
        if(self.step <= LIFETIME_NUM // 2):
            return CurrentRule.PIECE
        else:
            return CurrentRule.EMERGENCY

class Task_9(Task_1):
    #ルールが生涯の真ん中あたりで変更されるタスク
    #ばらつきがある(ちょうど真ん中ではない)
    def __init__(self,generation_num):
        self.step = 0
        self.dispersion = random.randint(-10,10)
        print('disperison : ',self.dispersion)
    def get_current_rule(self):
        self.step += 1
        print(self.step)
        if(self.step <= LIFETIME_NUM // 2 + self.dispersion):
            return CurrentRule.PIECE
        else:
            return CurrentRule.EMERGENCY

if __name__=='__main__':
    task = Task_9(10)
    for i in range(100):
        print("question:",task.question())
        result = input()
        print(task.feedback(result))
    task = Task_4(11)
    for i in range(10):
        print("question:",task.question())
        result = input()
        print(task.feedback(result))
