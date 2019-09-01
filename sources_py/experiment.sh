#!/bin/bash
python main.py N 1 > ./result/Normal_1;
python main.py N 2 > ./result/Normal_2;
python main.py N 3 > ./result/Normal_3;
python main.py N 4 > ./result/Normal_4;
python main.py N 5 > ./result/Normal_5;
python main.py N 6 > ./result/Normal_6;
python main.py N 7 > ./result/Normal_7;
echo 'Normal has done.';

python main.py H 1 > ./result/Hebbian_1;
python main.py H 2 > ./result/Hebbian_2;
python main.py H 3 > ./result/Hebbian_3;
python main.py H 4 > ./result/Hebbian_4;
python main.py H 5 > ./result/Hebbian_5;
python main.py H 6 > ./result/Hebbian_6;
python main.py H 7 > ./result/Hebbian_7;
echo 'Hebbian has done.';

python main.py M1H 1 > ./result/M1_Hebbian_1;
python main.py M1H 2 > ./result/M1_Hebbian_2;
python main.py M1H 3 > ./result/M1_Hebbian_3;
python main.py M1H 4 > ./result/M1_Hebbian_4;
python main.py M1H 5 > ./result/M1_Hebbian_5;
python main.py M1H 6 > ./result/M1_Hebbian_6;
python main.py M1H 7 > ./result/M1_Hebbian_7;
echo 'M1_Hebbian has done.';

python main.py M2H 1 > ./result/M2_Hebbian_1;
python main.py M2H 2 > ./result/M2_Hebbian_2;
python main.py M2H 3 > ./result/M2_Hebbian_3;
python main.py M2H 4 > ./result/M2_Hebbian_4;
python main.py M2H 5 > ./result/M2_Hebbian_5;
python main.py M2H 6 > ./result/M2_Hebbian_6;
python main.py M2H 7 > ./result/M2_Hebbian_7;
echo 'M2_Hebbian has done.';

python main.py EH 1 > ./result/Extended_Hebbian_1;
python main.py EH 2 > ./result/Extended_Hebbian_2;
python main.py EH 3 > ./result/Extended_Hebbian_3;
python main.py EH 4 > ./result/Extended_Hebbian_4;
python main.py EH 5 > ./result/Extended_Hebbian_5;
python main.py EH 6 > ./result/Extended_Hebbian_6;
python main.py EH 7 > ./result/Extended_Hebbian_7;
echo 'Extended_Hebbian has done.';
echo 'completed!';
