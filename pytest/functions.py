import sys

def growth(initial,final):
    '''
    returns the growth between two values of the
    same variables in succesive time period.

    initial: non-negative value
    final: non-negative value

    '''
    if not (isinstance(initial,(float,int)) or isinstance(final,(float,int))):
        raise TypeError('Invalid input')
    if initial>0:
        return ((final-initial)/initial)*100
    else:
        return (final-initial)*100

def target(growth_val):
    '''
    returns the target value.
    If growth is positive returns 1.
    if growth is negative returns 0.

    '''

    if growth_val>0:
        return 1
    else:
        return 0
