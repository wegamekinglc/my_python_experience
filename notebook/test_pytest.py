# -*- coding: utf-8 -*-
"""
Created on 2018-9-16

@author: cheng.li
"""
import pytest


def fibonacci(n):
    if n == 1 or n == 2:
        return 1
    elif n >= 3:
        return fibonacci(n-1) + fibonacci(n-2)
    else:
        raise ValueError("n can't be negative")
        

def test_fibonacci_less_than_three():
    assert fibonacci(1) == 1

    
def test_fibonacci_recursive():
    for n in range(3, 11):
        assert fibonacci(n) == fibonacci(n-1) + fibonacci(n-2)

    
def test_fibonacci_with_negative():
    with pytest.raises(ValueError):
            _ = fibonacci(-1)