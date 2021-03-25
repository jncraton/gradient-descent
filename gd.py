def calc_gradient(fn, x, z):
    """
    Returns the gradient of fn at x, z

    >>> round(calc_gradient(lambda x,z: 2*x+z, 2, 3)[0], 1)
    2.0

    >>> round(calc_gradient(lambda x,z: 2*x+z, 2, 3)[1], 1)
    1.0
    """

    delta_x = .01
    delta_z = .01
    grad_x = (fn(x+delta_x,z) - fn(x,z)) / delta_x
    grad_z = (fn(x,z+delta_z) - fn(x,z)) / delta_z
    return (grad_x, grad_z)

def find_extreme(fn, x=0, z=0, lr=.1):
    """

    >>> round(find_extreme(lambda x, z: x ** 2 + 3*x + 2*z ** 2 + 7)[0], 2)
    -1.5

    >>> int(find_extreme(lambda x, z: x ** 2 + 3*x + 2*z ** 2 + 7)[1])
    0
    """
    
    grad_x, grad_z = calc_gradient(fn, x, z)

    next_x = x - grad_x * lr
    next_z = z - grad_z * lr
    
    if abs(grad_x) > .01 or abs(grad_z) > .01:
        return find_extreme(fn, next_x, next_z)
    else:
        return (x, z)

if __name__ == '__main__':
    print(find_extreme(lambda x, z: x ** 2 + 3*x + 2*z ** 2 + 7))
