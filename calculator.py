# -*- coding: utf-8 -*-
"""
Created on Tue Jul 10 20:11:25 2018

@author: Harsh
"""

import math
import sys


def calc(term):
    """
        input: term of type str
        output: returns the result of the computed term.
        purpose: This function is the actual calculator and the heart of the application
    """
    
    # This part is for reading and converting arithmetic terms.
    term = term.replace(' ', '')
    term = term.replace('^', '**')
    term = term.replace('=', '')
    term = term.replace('?', '')
    term = term.replace('%', '/100')
    term = term.replace('rad', 'radians')
    term = term.replace('mod', '%')

    functions = ['sin', 'cos', 'tan', 'cosh', 'sinh', 'tanh', 'sqrt', 'pi', 'radians', 'e'] 

    # This part is for reading and converting function expressions.
    term = term.lower()
    
    for function in functions:            
        if function in term:
            withmath = 'math.' + function
            term = term.replace(function, withmath)

    try:

        # here goes the actual evaluating.
        term = eval(term)

    # here goes to the error cases.
    except ZeroDivisionError:

        print("Can't divide by 0.  Please try again.")

    except NameError:

        print('Invalid input.  Please try again')

    except AttributeError:

        print('Please check usage method and try again.')
        
    return term


def result(term):
    """
        input:  term of type str
        output: none
        purpose: passes the argument to the function calc(...) and 
                prints the result onto console.
    """
    print("\n" + str(calc(term)))


def main():
    """
        main-program
        purpose: handles user input and prints 
                 information to the console.
    """
    
    print("\nScientific Calculator\n\nFor Example: sin(rad(90)) + 50% * (sqrt(16)) + round(1.42^2)"+\
          "- 12mod3\n\nEnter quit to exit")

    if sys.version_info.major >= 3:
        while True:
            k = input("\nWhat is ")
            if k == 'quit':
                break
            result(k)

    else:
        while True:
            k = raw_input("\nWhat is ")
            if k == 'quit':
                break
            result(k)


if __name__ == '__main__':
    main()