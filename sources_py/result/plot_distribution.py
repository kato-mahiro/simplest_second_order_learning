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
command += " | grep can_learning | cut -d ' ' -f 3 > ./can"
command = ''.join(command)
os.system(command)

command = []
command += 'cat '
command += args[1]
command += " | grep cannot_learning | cut -d ' ' -f 3 > ./cannot"
command = ''.join(command)
os.system(command)

command = []
command += 'cat '
command += args[1]
command += " | grep perfect | cut -d ' ' -f 3 > ./perfect"
command = ''.join(command)
os.system(command)

can_data = open("can","r")
can_lines = can_data.readlines()
can_data.close()

cannot_data = open("cannot","r")
cannot_lines = cannot_data.readlines()
cannot_data.close()

perfect_data = open("perfect","r")
perfect_lines = perfect_data.readlines()
perfect_data.close()

add_lines = []
for i in range(500):
    can_lines[i] = int(can_lines[i])
    cannot_lines[i] = int(cannot_lines[i])
    perfect_lines[i] = int(perfect_lines[i])
    add_lines.append(cannot_lines[i] + can_lines[i])

x = np.arange(1,501)
fig,axes = plt.subplots()
axes.bar(x, cannot_lines,width=1.0,color='plum',label="couldn't learning")
axes.bar(x, can_lines, width=1.0,bottom = cannot_lines,color='aquamarine',label="could learning")
axes.bar(x,perfect_lines, width=1.0,bottom = add_lines,color='darkblue',label="perfect")

plt.legend()
#plt.show()
plt.savefig('./graphs/' + args[1] + '_distribution.png')
