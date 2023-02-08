import matplotlib.pyplot as stack_Plot
def main():
    days = [1 , 2 , 3 , 4 , 5]
    Sleeping = [7 , 5 , 9 , 4,10]
    working = [10, 20, 44, 57, 7]
    eating = [16, 61, 7, 2, 9]
    stack_Plot.plot([] , [] , color = 'red' , label = 'Sleeping Hours')
    stack_Plot.plot([] , [] , color = 'green' , label = 'Workings Hours')
    stack_Plot.plot([] , [] , color = 'blue' , label = 'Eating Hours')
    stack_Plot.stackplot (days, Sleeping , working , eating, colors =[ 'r' , 'g' , 'b' ])
    #scat.stackplot (x2, y2, label ="Data 2 ", color ='green', marker='*')
    stack_Plot.title ("Stackplot Example Graph")
    stack_Plot.xlabel ("Days")
    stack_Plot.ylabel ("Stack")
    stack_Plot.legend()
    stack_Plot.show()
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
