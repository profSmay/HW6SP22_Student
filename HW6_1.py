from scipy.optimize import fsolve

def fn(I):
    """
    This function is for fsolve to work on for the circuit in problem 1.
    There are two loop equations and one node equation.
    :param I: list of currents
    """
    # loop equations
    eq1=4*I[0]+I[2]-16
    eq2=4*I[1]+I[2]-32
    # node equation
    eq3=I[0]+I[1]-I[2]
    return [eq1, eq2, eq3]

def main():
    """
    This program solves for the unknown currents in the circuit of the homework assignment.
    :return: nothing
    """
    #initial guess
    I0=[1,1,1]
    I=fsolve(fn,I0)
    print("I1 = {:0.1f}".format(I[0]))
    print("I2 = {:0.1f}".format(I[1]))
    print("I3 = {:0.1f}".format(I[2]))

if __name__=="__main__":
    main()