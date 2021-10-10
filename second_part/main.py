import matplotlib.pyplot as plt
import matplotlib.animation as animation


fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)
files = ['data.txt']
for file_name in files:
    step = 1
    x = []
    y = []
    x_ = []
    y_ = []
    with open(file_name, 'r') as file:
        for line in file:
            if step % 2 == 1:
                x.append([float(i) for i in line[:-1].split(" ")])
                x_.append(min([float(i) for i in line[:-1].split(" ")]))
                x_.append(max([float(i) for i in line[:-1].split(" ")]))
            else:
                y.append([float(i) for i in line[:-1].split(" ")])
                y_.append(min([float(i) for i in line[:-1].split(" ")]))
                y_.append(max([float(i) for i in line[:-1].split(" ")]))
            step += 1

        y_max = max(y_)*1.1
        x_max = max(x_)
        y_min = min(y_)*1.1
        x_min = min(x_)
        print(x_min, x_max, y_min, y_max)


def animate(i):
    i = i % (2*len(x))
    ax1.clear()
    ax1.set_ylim([y_min, y_max])
    ax1.set_xlim([x_min, x_max])
    if i < len(x):
        ax1.plot(x[i], y[i])
    else:
        ax1.plot(x[len(x) - i - 1], y[len(x) - i -1])


ani = animation.FuncAnimation(fig, animate)
ani.save('animation.gif', writer='imagemagick', fps=10)