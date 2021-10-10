import matplotlib.pyplot as plt


data = 'students.csv'
teachers = set()
groups = []
marks = []

with open(data, 'r') as file:
    for line in file:
        print(line.split(';'))
        teachers.add(line.split(';')[0])
        groups.append(line.split(';')[1])
        marks.append(line.split(';')[2])
print(teachers)