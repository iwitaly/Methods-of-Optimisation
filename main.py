__author__ = 'iwitaly'

'''
this programm has a three solver function to find extremum

1) const(x0)
gradient method with const step
2) newton(x0)
classical Newton's method
3) armiho(x0)
gradients Armihos method
'''


eps = 1.e-10

from math import *

def f(x):
    # return log(exp(x)+exp(-x))
    # return -log(x) + x
    return x**2 + x

def df(x):
    # return (-1 + exp(2*x)) / (1 + exp(2*x))
    # return -1.0/x + 1.0
    return 2*x + 1.0

def d2f(x):
    # return (4 * exp(2*x)) / ((1 + exp(2*x))**2)
    # return 1.0/(x**2)
    return 2.0

def const(x0):
    c = 0.1
    x = x0 - c*df(x0)

    numberOfAlgorithmsSteps = 0

    while abs(x0-x) > eps or abs(df(x)) > eps:
        numberOfAlgorithmsSteps += 1

        try:
            x = x0 - c*df(x0)
        except:
            print 'exception was caught, smt goes wrong!'
            exit(-1)

        x0 = x

    print 'zero is ' + str(round(x, 2))
    print 'with value ' + str(round(f(x), 2))
    print 'number of steps ' + str(numberOfAlgorithmsSteps)


def newton(x0):
    '''
    find extremum of function f, using derivate of f
    '''

    numberOfAlgorithmsSteps = 0

    x = x0 - df(x0)/d2f(x0)

    while abs(x - x0) >= eps or abs(df(x)) > eps:
        y = x

        numberOfAlgorithmsSteps += 1

        try:
            x = x0 - df(x0)/d2f(x0)
        except:
            print 'exception was caught, smt goes wrong!'
            exit(-1)

        x0 = y

    print 'extremum is ' + str(round(x, 2))
    print 'with value ' + str(round(f(x), 2))
    print 'number of steps ' + str(numberOfAlgorithmsSteps)

def armiho(x0):
    e = 0.01
    teta = 0.1

    numberOfAlgorithmsSteps = 0

    x = 1000
    alpha = 1000

    def calculateAlpha(x0, alpha):

        try:
            f(x0 - alpha*df(x0)) > f(x0) - e*alpha*(df(x0)**2)
        except:
            print 'exception was caught, smt goes wrong!'
            exit(-1)

        while f(x0 - alpha*df(x0)) > f(x0) - e*alpha*(df(x0)**2):
            alpha *= teta
        return alpha

    while abs(x0-x) > eps or abs(df(x)) > eps:
        alpha = calculateAlpha(x0, alpha)
        x = x0 - alpha*df(x0)
        x0 = x

        numberOfAlgorithmsSteps += 1

        try:
            abs(x0-x) > eps
            abs(df(x)) > eps
        except ValueError:
            print 'exception was caught, smt goes wrong!'


    print 'zero is ' + str(round(x, 2))
    print 'with value ' + str(round(f(x), 2))
    print 'number of steps ' + str(numberOfAlgorithmsSteps)

if __name__ == '__main__':
    const(1.0)