#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 17:50:20 2020

@author: prograqmista
"""

def fibonacci(n):
    if n < 2:
        return n 
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
    
Test 
#assert
    
print(fibonacci(15))
