# Importation styles


"""
from fibo import fib, fib2
fib(500)
"""
=======================
"""
import fibo
fibo.fib(1000)
fib = fibo.fib
fib(500)
"""
=======================
"""
from fibo import *
fib(500)
print(fib2(500))
"""
========================
'''
import fibo as _fib
_fib.fib(500)
'''

===================================================
'''
from fibo import fib as fibonacci
from fibo import fib2 as _fibonacci

fibonacci(500)
print(_fibonacci(800))
'''
================================================
"""
import sys
sys.stdout.write("#pythoniscool\n")

*******************************************

sys = __import__('sys')
sys.stdout.write("#pythoniscool\n")
arguments = sys.argv
for i, arg in enumerate(arguments):
    print(f"Argument {i}: {arg}")

"""
=============================================

