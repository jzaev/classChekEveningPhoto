import sys
import random

def func():
    print("in func")

a = 5
b = a + 2

func()

print(dir(random))

for i in range(100):
    print(random.randint(1,100))