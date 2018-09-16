# -*- coding: utf-8 -*-
"""
Created on 2018-9-16

@author: cheng.li
"""
import unittest


def fibonacci(n):
    if n == 1 or n == 2:
        return 1
    elif n >= 3:
        return fibonacci(n-1) + fibonacci(n-2)
    else:
        raise ValueError("n can't be negative")
        

class FibonacciTest(unittest.TestCase):
    
    def test_fibonacci_less_than_three(self):
        self.assertEqual(fibonacci(1), 1)
        self.assertEqual(fibonacci(2), 1)
        
    def test_fibonacci_recursive(self):
        for n in range(3, 11):
            self.assertEqual(fibonacci(n), fibonacci(n-1) + fibonacci(n-2))
            
    def test_fibonacci_with_negative(self):
        with self.assertRaises(ValueError):
            _ = fibonacci(-1)
            

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(FibonacciTest)
    unittest.TextTestRunner(verbosity=2).run(suite)