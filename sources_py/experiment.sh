#!/bin/bash
python main.py N 8 > ./result/Task8_Normal
python main.py H 8 > ./result/Task8_Hebbian
python main.py M1H 8 > ./result/Task8_M1_Hebbian
python main.py M2H 8 > ./result/Task8_M2_Hebbian
python main.py E 8 > ./result/Task8_Extended_Hebbian
echo 'completed!';
