# doc.py
import doctest


def add(x, y):
    """
    >>> add(1, 2)
    3
    >>> add(3,5)
    8
    """
    return x + y


def power(x):
    """
    >>> power(2)
    4
    
    >>> power(9)
    81
    
    :param x: 
    :return: x*x
    """
    return x * x


def main():
    pass


if __name__ == '__main__':
    main()
