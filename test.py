#!/usr/bin/python3
"""
    Test module.
"""

from components.base import Base

dic = {'name': "calm", 'id': "asigned one no problem."}

print("object 1:")
obj1 = Base(**dic)
print(obj1.id, obj1.name)

print()
print("object 2:")
obj2 = Base()
print(obj2.id)

print()
print("object 3:")
obj3 = Base()
print(obj3.id)
