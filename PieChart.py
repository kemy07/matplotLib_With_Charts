import matplotlib.pyplot as pie_var
def main():
    slices = [10 , 7 , 3 , 4 ]
    Activities = ['Working' , 'sleeping' , 'eating' ,'watching']
    color = ['r' , 'g' , 'b' , 'y']
    pie_var.pie (slices , labels= Activities , colors= color , startangle=90 , shadow=True ,
                 explode= (0 , 0 , 0 , 1 ) ,
                 autopct='%1.1f%%')
    pie_var.title ("Pie Example Graph")
    pie_var.show()
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
