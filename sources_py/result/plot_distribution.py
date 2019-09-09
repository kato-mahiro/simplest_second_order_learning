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
command += " | grep average_num_of_neuron | cut -d ' ' -f 2 > ./num_of_neuron"
command = ''.join(command)
os.system(command)

command = []
command += 'cat '
command += args[1]
command += " | grep average_num_of_modulation_neuron | cut -d ' ' -f 2 > ./num_of_modulation_neuron"
command = ''.join(command)
os.system(command)

command = []
command += 'cat '
command += args[1]
command += " | grep average_num_of_hidden_neuron | cut -d ' ' -f 2 > ./num_of_hidden_neuron"
command = ''.join(command)
os.system(command)

num_of_neuron_data = open("num_of_neuron","r")
num_of_neuron_lines = num_of_neuron_data.readlines()
num_of_neuron_data.close()

num_of_modulation_neuron_data = open("num_of_modulation_neuron","r")
num_of_modulation_neuron_lines = num_of_modulation_neuron_data.readlines()
num_of_modulation_neuron_data.close()

num_of_hidden_neuron_data = open("num_of_hidden_neuron","r")
num_of_hidden_neuron_lines = num_of_hidden_neuron_data.readlines()
num_of_hidden_neuron_data.close()

x = np.arange(1,501,1)
for i in range(500):
    num_of_neuron_lines[i] = float(num_of_neuron_lines[i])
    num_of_modulation_neuron_lines[i] = float(num_of_modulation_neuron_lines[i])
    num_of_hidden_neuron_lines[i] = float(num_of_hidden_neuron_lines[i])

plt.title(args[1])
plt.ylim(0.0,4.0)
plt.xlim(0,510)
plt.yticks([1.0,2.0,3.0,4.0])
plt.grid(True)
plt.xlabel('Generation')
plt.ylabel('average_num_of_neuron')

#plt.plot(x,num_of_neuron_lines,label='num of total neuron')
plt.plot(x,num_of_modulation_neuron_lines,label='num of moddulation neuron')
plt.plot(x,num_of_hidden_neuron_lines,label='num of hidden neuron(not modulation)')


#plt.plot(x,min_lines,label='worst')
#plt.plot(x,min_ave_line,label='average of worst fitness')
#print('min-ave:',sum(min_lines)/len(min_lines))
#print('min-max:',max(min_lines))

plt.legend()
#plt.show()
plt.savefig('./graphs/' + args[1] + '_result.png')
