import matplotlib.pyplot as plt
def main():
    x = (1 , 5)
    y = (4 , 7)
    x2 = (4 , 7)
    y2 = (5 , 6)
    plt.plot (x , y , label = "First Line")
    plt.plot (x2 , y2 , label = "Second Line")
    plt.title ("Lines Example Graph")
    plt.xlabel ("xAxis")
    plt.ylabel ("yAxis")
    plt.legend()
    plt.show()
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
