# -*- coding: utf-8 -*-
"""
Created on 2018-9-16

@author: cheng.li
"""

def fibonacci(n):
    if n == 1 or n == 2:
        return 1
    elif n >= 3:
        return fibonacci(n-1) + fibonacci(n-2)
    else:
        raise ValueError("n can't be negative")
        
        
if __name__ == '__main__':
    assert fibonacci(1) == 1, "fibonacci(1) is not equale to 1"
    assert fibonacci(2) == 1, "fibonacci(2) is not equale to 1"
    assert fibonacci(3) == fibonacci(1) + fibonacci(2), "fibonacci(3) is not equal to fibonacci(1) + fibonacci(2)"
    
    try:
        fibonacci(-1)
    except ValueError:
        pass
    else:
        raise Exception("fibonacci(-1) does not correctly raise ValueError")
    print("Every thing is Ok")