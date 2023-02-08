import matplotlib.pyplot as plt
import csv
def main():
    x = []
    y = []
    with open("values.txt" , 'r') as file :
        plots = csv.reader(file , delimiter = ',')
        for row in plots:
            x.append(int (row [0]))
            y.append(int (row [1]))
    plt.plot (x , y , label = "Reasing from file")
    plt.show()
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
