import os
import sys
import numpy as np
import matplotlib.pyplot as plt

args = sys.argv

command = []
command += 'cat '
command += args[1]
command += " | grep max | cut -d ' ' -f 3 > ./max"
command = ''.join(command)
os.system(command)

command = []
command += 'cat '
command += args[1]
command += " | grep ave | cut -d ' ' -f 3 > ./ave"
command = ''.join(command)
os.system(command)

max_data = open("max","r")
max_lines = max_data.readlines()
max_data.close()

ave_data = open("ave","r")
ave_lines = ave_data.readlines()
ave_data.close()

x = np.arange(1,1001,1)
for i in range(1000):
    max_lines[i] = float(max_lines[i])
    ave_lines[i] = float(ave_lines[i])
plt.ylim(0.0,1.0)

plt.plot(x,max_lines)
plt.plot(x,ave_lines)
plt.show()
