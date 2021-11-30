import matplotlib.pyplot as plt


def do_first_task(files):
    for file_name in files:
        with open(file_name, 'r') as file:
            n = int(file.readline())
            x = []
            y = []
            for i in range(n):
                line = [float(i) for i in file.readline().split(" ")]
                x.append(line[0])
                y.append(line[1])

        R_max = max(max(x), max(y))
        R_min = min(min(x), min(y))
        plt.scatter(x,y, s=7, marker="D", c='yellow', linewidths=1, edgecolors='red', alpha=0.8)
        plt.gca().set_aspect('equal', adjustable='box')

        #plt.ylim([R_min - 10, R_max + 10])
        #plt.xlim([R_min - 10, R_max +10])


        #plt.ylim([min(y), max(y)])
        #plt.xlim([min(x), max(x)])
        #plt.axis('equal')
        plt.title(file_name + ' points')
        plt.savefig('result_' + file_name[:3] + '.png')
        plt.close()

if __name__ == "__main__":
    my_files = ['001.dat', '002.dat', '003.dat', '004.dat', '005.dat']
    do_first_task(my_files)