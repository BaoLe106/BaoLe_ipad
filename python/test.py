import random
import threading

global E 
E = 100
global x, y
def func1():
    while E > 1e-2:
        x = random.random()
        y = random.random()
        
def func2():
    while E > 1e-2:
        E = x**2 + y**2
        print(x, y, E)
        
t1 = threading.Thread(target = func1)
t2 = threading.Thread(target = func2)

t1.start()
t2.start()