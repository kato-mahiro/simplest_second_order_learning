import os
import sys
import numpy as np
import matplotlib
matplotlib.use('Agg')
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

command = []
command += 'cat '
command += args[1]
command += " | grep min | cut -d ' ' -f 3 > ./min"
command = ''.join(command)
os.system(command)

max_data = open("max","r")
max_lines = max_data.readlines()
max_data.close()

ave_data = open("ave","r")
ave_lines = ave_data.readlines()
ave_data.close()

#min_data = open("min","r")
#min_lines = min_data.readlines()
#min_data.close()

x = np.arange(1,501,1)
for i in range(500):
    max_lines[i] = float(max_lines[i])
    ave_lines[i] = float(ave_lines[i])
    #min_lines[i] = float(min_lines[i])

max_ave_line = [sum(max_lines)/len(max_lines) for i in range(len(max_lines))]
ave_ave_line = [sum(ave_lines)/len(ave_lines) for i in range(len(ave_lines))]
#min_ave_line = [sum(min_lines)/len(min_lines) for i in range(len(min_lines))]

plt.title(args[1])
plt.ylim(0.0,1.0)
plt.xlim(0,510)
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

#plt.plot(x,min_lines,label='worst')
#plt.plot(x,min_ave_line,label='average of worst fitness')
#print('min-ave:',sum(min_lines)/len(min_lines))
#print('min-max:',max(min_lines))

plt.legend()
#plt.show()
plt.savefig('./graphs/' + args[1] + '.png')
