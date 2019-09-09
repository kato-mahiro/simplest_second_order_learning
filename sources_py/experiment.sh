#!/bin/bash
python main.py FH 1 > ./result/Task_1_FH
echo '1/4'
python main.py FEH 1 > ./result/Task_1_FEH
echo '2/4'
python main.py FH 8 > ./result/Task_8_FH
echo '3/4'
python main.py FEH 8 > ./result/Task_8_FEH
echo '4/4'
echo  
echo  
echo  
echo 'completed!';
