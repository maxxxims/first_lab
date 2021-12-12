import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_pdf import PdfPages


data = 'students.csv'
result = [[0 for i in range(8)] for i in range(7)]
result2 = [[0 for i in range(8)] for i in range(6)]


pr = {}
u = 0

gr = {}
y = 0

with open(data, 'r') as file:
    for line in file:
        #prep_number = int(line.split(';')[0][-1]) - 1
        prep_ = line.split(';')[0]
        if prep_ in list(pr.keys()):
            pass
        else:
            pr[prep_] = u
            u+=1
        prep_number = pr[prep_]
        mark = int(line.split(';')[2]) - 3
        result[prep_number][mark] += 1

        #group_number = int(line.split(';')[1][-1]) - 1
        group_ = line.split(';')[1]
        if group_ in list(gr.keys()):
            pass
        else:
            gr[group_] = y
            y+=1
        group_number = gr[group_]
        result2[group_number][mark] += 1


#preps = ['prep' + str(i) for i in range(1,8)]
preps = list(pr.keys())
#group = ['75' + str(i+1) for i in range(6)]
group = list(gr.keys())
widht = 0.15

x = np.arange(len(preps))
dt = np.transpose(result)


fig, ax = plt.subplots()
rect = [0]*10
#clc = ['red', 'orange', 'yellow', 'green', 'blue', 'purple', 'black', 'gray']


for i in range(0, 8):
    rect[i] = ax.bar(x + (i-4)*widht/2, dt[i], widht, label=str(i+3))
ax.set_title("Marks per preps")
ax.set_xticks(x)
ax.set_xticklabels(preps)
plt.legend()
plt.show()
#plt.savefig('Marks per prepods.png')
#plt.close()

################################################################################

x2 = np.arange(len(group))
dt2 = np.transpose(result2)

fig2, ax2 = plt.subplots()
rect2 = [0]*10

for i in range(0, 8):
    rect2[i] = ax2.bar(x2 + (i-4)*widht/2, dt2[i], widht, label=str(i+3))
ax2.set_title("Marks per groups")
ax2.set_xticks(x2)
ax2.set_xticklabels(group)
plt.legend()
plt.savefig('Marks per groups.png')
plt.show()

pdf1 = PdfPages("result.pdf")
pdf1.savefig(fig)
pdf1.savefig(fig2)
pdf1.close()

