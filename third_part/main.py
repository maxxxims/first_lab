import matplotlib.pyplot as plt
import numpy as np

data = 'students.csv'
teachers = []
groups = []
marks = []
result = [[0 for i in range(8)] for i in range(7)]



with open(data, 'r') as file:
    for line in file:
        prep_number = int(line.split(';')[0][-1]) - 1
        mark = int(line.split(';')[2]) - 3
        result[prep_number][mark] += 1


preps = ['prep' + str(i) for i in range(1,8)]
widht = 0.15

x = np.arange(len(preps))
dt = np.transpose(result)
for line in result:
    print(line)

fig, ax = plt.subplots()
rect = [0]*10

clc = ['red', 'orange', 'yellow', 'green', 'blue', 'purple', 'black', 'gray']

for i in range(0, 8):
    rect[i] = ax.bar(x + (i-4)*widht/2, dt[i], widht, label=str(i+3))

ax.set_xticks(x)
ax.set_xticklabels(preps)

#plt.xticks(preps)
plt.legend()


plt.show()

'''print(np.transpose(result))
print()
for line in result:
    print(line)'''
#print(teachers)
#plt.bar(teachers, marks)
#plt.show()