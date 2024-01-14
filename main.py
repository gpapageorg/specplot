from sympy import *
import time
import matplotlib.pyplot as plt
import numpy as np


class Expression:
    def __init__(self, string):
        self.x = Symbol('x')
        self.string = string
        self.sexpr = sympify(self.string)
    
    def eval(self, point):
        return self.sexpr.evalf(subs={self.x:point})


class Math:
    def __init__(self, exprobj, h, start, end):
        self.exprobj = exprobj
        self.h = h
        self.start = start
        self.end = end
        self.val, self.axis = self.__createValues()

    def fft(self):
        fastFourier = np.fft.fft(self.val)
        return np.abs(fastFourier)

    def __createValues(self):
        val = np.array([])
        axis = np.array([])
        #val = []
        #axis = []

        k = self.start 
        v = int((abs(self.start - self.end) / self.h))
        print(v)

        for i in range(v):
            #val.append(self.exprobj.eval(k))
            val = np.append(val, self.exprobj.eval(k))
            k += self.h
            axis = np.append(axis, k)
            #axis.append(k)

        return val, axis


def main():
    start = time.time()
    string = 'sin(2*pi*x)' 
    e = Expression(string)
    
    m = Math(e, 0.1, -2*pi, 2*pi) 
    end = time.time()
    #plt.plot(m.axis, m.val)
    #plt.show()
    
    f = m.fft() 
    a = np.linspace(-62,62,num = 125)
    plt.plot(a, f)
    plt.show()

    print(a)




if __name__ == "__main__":
    main()
