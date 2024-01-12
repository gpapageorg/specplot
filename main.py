from sympy import *


class Expression:
    def __init__(self, expr):
        self.x = Symbol('x')
        self.expr = expr
        self.sexpr = sympify(self.expr)
    
    def eval(self, point):
        print(self.sexpr.evalf(subs={self.x:point}))



def main():
    string = 'x**2' 
    e = Expression(string)

if __name__ == "__main__":
    main()
