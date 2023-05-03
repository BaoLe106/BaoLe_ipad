import random
import threading

E, x, y = 100, None, None

def func1():
    global E, x, y # to change global variable inside a function
    while E > 1e-2:
        x = random.random()
        y = random.random()
        
def func2():
    global E, x, y # to change global variable inside a function
    while E > 1e-2:
        E = x**2 + y**2
        print(x, y, E)
        
t1 = threading.Thread(target = func1)
t2 = threading.Thread(target = func2)

t1.start()
t2.start()