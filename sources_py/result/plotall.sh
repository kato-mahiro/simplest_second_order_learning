#!/bin/bash
for i in {1..7};
do 
    python plot.py Normal_Task$i;
    python plot_distribution.py Normal_Task$i;

    python plot.py Hebbian_Task$i;
    python plot_distribution.py Hebbian_Task$i;

    python plot.py M1_Hebbian_Task$i;
    python plot_distribution.py M1_Hebbian_Task$i;

    python plot.py M2_Hebbian_Task$i;
    python plot_distribution.py M2_Hebbian_Task$i;

    python plot.py Extended_Hebbian_Task$i;
    python plot_distribution.py Extended_Hebbian_Task$i;
done
