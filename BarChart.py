import matplotlib.pyplot as br
def main():
    age = [10 , 15 , 36 , 45 , 11]
    salary = [100 , 300 , 600 , 450,654]
    age2 = [11, 20, 40, 65, 15]
    salary2 = [320, 140, 230, 254, 210]
    br.bar (age ,salary  , label = "Data 1 " , color = 'red')
    br.bar (age2 ,salary2  , label = "Data 2 " , color = 'green')
    br.title ("Bar Example Graph")
    br.xlabel ("Age")
    br.ylabel ("Salary")
    br.legend()
    br.show()
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
