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
command += " | grep total_modulated_agent | cut -d ' ' -f 2 > ./mod"
command = ''.join(command)
os.system(command)

command = []
command += 'cat '
command += args[1]
command += " | grep total_not_modulated_agent | cut -d ' ' -f 2 > ./not_mod"
command = ''.join(command)
os.system(command)


mod_data = open("mod","r")
mod_lines = mod_data.readlines()
mod_data.close()

not_mod_data = open("not_mod","r")
not_mod_lines = not_mod_data.readlines()
not_mod_data.close()

add_lines = []
for i in range(500):
    mod_lines[i] = int(mod_lines[i])
    not_mod_lines[i] = int(not_mod_lines[i])

x = np.arange(1,501)
fig,axes = plt.subplots()
axes.bar(x, not_mod_lines,width=1.0,color='plum',label="not_modulated")
axes.bar(x, mod_lines, width=1.0,bottom = not_mod_lines,color='aquamarine',label="modulated")

plt.title(args[1])
plt.legend()
#plt.show()
plt.savefig('./graphs/' + args[1] + '_distribution.png')
