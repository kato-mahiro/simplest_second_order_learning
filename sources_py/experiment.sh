#!/bin/bash
python main.py FH 1 > ./result/Task_1_FH
echo '1'
python main.py FEH 1 > ./result/Task_1_FEH
echo '2'
python main.py FH 2 > ./result/Task_2_FH
echo '3'
python main.py FEH 2 > ./result/Task_2_FEH
echo '4'
python main.py FH 8 > ./result/Task_8_FH
echo '5'
python main.py FEH 8 > ./result/Task_8_FEH
echo '6'
python main.py FH 10 > ./result/Task_10_FH
echo '7'
python main.py FEH 10 > ./result/Task_10_FEH
echo '8'
echo  
echo  
echo  
echo 'completed!';
