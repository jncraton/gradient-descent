def calc_gradient(fn, x, z):
    """
    Returns the gradient of fn at x, z

    >>> round(calc_gradient(lambda x,z: 2*x+z, 2, 3)[0], 1)
    2.0

    >>> round(calc_gradient(lambda x,z: 2*x+z, 2, 3)[1], 1)
    1.0
    """

    return [0,0]

def find_extreme(fn, x=0, z=0, lr=.1):
    """

    >>> round(find_extreme(lambda x, z: x ** 2 + 3*x + 2*z ** 2 + 7)[0], 2)
    -1.5

    >>> int(find_extreme(lambda x, z: x ** 2 + 3*x + 2*z ** 2 + 7)[1])
    0
    """
    
    return [0,0]

if __name__ == '__main__':
    print(find_extreme(lambda x, z: x ** 2 + 3*x + 2*z ** 2 + 7))
