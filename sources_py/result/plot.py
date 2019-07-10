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

max_ave_line = [sum(max_lines)/len(max_lines) for i in range(len(max_lines))]
ave_ave_line = [sum(ave_lines)/len(ave_lines) for i in range(len(ave_lines))]

plt.title(args[1])
plt.ylim(0.0,1.0)
plt.xlim(0,1010)
plt.yticks([0.0,0.25,0.50,0.75,1.0])
plt.grid(True)
plt.xlabel('Generation')
plt.ylabel('Fitness')
plt.plot(x,max_lines,label='max')
plt.plot(x,max_ave_line,label='average of best fitness')
print('max-ave:',sum(max_lines)/len(max_lines))
print('max-max:',max(max_lines))
plt.plot(x,ave_lines,label='average')
plt.plot(x,ave_ave_line,label='average of average fitness')
print('ave-ave:',sum(ave_lines)/len(ave_lines))
print('ave-max:',max(ave_lines))
plt.legend()
plt.show()
