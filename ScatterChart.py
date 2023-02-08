import matplotlib.pyplot as scat
def main():
    x = [1 , 5 , 6 , 4 , 11]
    y = [1 , 3 , 7 , 2,9]
    x2 = [3, 2, 4, 5, 7]
    y2 = [1, 6, 7, 2, 9]

    scat.scatter (x, y, label ="Data 1 ", color ='red', marker='*')
    scat.scatter (x2, y2, label ="Data 2 ", color ='green', marker='*')
    scat.title ("Scatter Example Graph")
    scat.xlabel ("xAxis")
    scat.ylabel ("yAxis")
    scat.legend()
    scat.show()
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
