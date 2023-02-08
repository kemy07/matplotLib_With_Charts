import matplotlib.pyplot as fun
import  numpy as np
def main():
    x = np.arange(0 , 3 * np.pi , 0.1 )
    #y = np.sin (x)
    y = np.cos (x)
    fun.plot (x , y)
    #fun.title ("sin Function")
    fun.title ("Cos Function")
    fun.show()
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
