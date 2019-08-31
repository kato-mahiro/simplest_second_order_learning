import os
import sys
import numpy as np
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
axes.bar(x, cannot_lines,width=1.0,color='plum')
axes.bar(x, can_lines, width=1.0,bottom = cannot_lines,color='aquamarine')
axes.bar(x,perfect_lines, width=1.0,bottom = add_lines,color='darkblue')

plt.show()

"""
can_ave_line = [sum(can_lines)/len(can_lines) for i in range(len(can_lines))]
cannot_cannot_line = [sum(cannot_lines)/len(cannot_lines) for i in range(len(cannot_lines))]
perfect_ave_line = [sum(perfect_lines)/len(perfect_lines) for i in range(len(perfect_lines))]


plt.title(args[1])
plt.ylim(0,50)
plt.xlim(0,510)
plt.yticks([0,10,20,30,40,50])
plt.grid(True)
plt.xlabel('Generation')
plt.ylabel('number')

plt.plot(x,can_lines,label='can')
plt.plot(x,can_ave_line,label='average of best fitness')
print('can-ave:',sum(can_lines)/len(can_lines))
print('can-can:',max(can_lines))

plt.plot(x,cannot_lines,label='cannotrage')
plt.plot(x,cannot_cannot_line,label='cannotrage of cannotrage fitness')
print('cannot-cannot:',sum(cannot_lines)/len(cannot_lines))
print('cannot-max:',max(cannot_lines))

plt.plot(x,perfect_lines,label='worst')
plt.plot(x,perfect_ave_line,label='average of worst fitness')
print('perfect-ave:',sum(perfect_lines)/len(perfect_lines))
print('perfect-max:',max(perfect_lines))


plt.legend()
plt.show()
"""
