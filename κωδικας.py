import threading
from time import sleep
sem_fun1 = threading.Semaphore(0)
sem_fun2 = threading.Semaphore(0)
sem_fun3 = threading.Semaphore(0)
sem_fun4 = threading.Semaphore(0)
def fun1(a, b):
 global c
 print("fun1 started ")
 c = a + b
 print("fun1 finished ")
 sem_fun1.release()
def fun2(d, e):
 global z
 print("fun2 started ")
 z = d * e
 print("fun2 finished ")
 sem_fun2.release()
def fun3(u, i):
 global h
 print("fun3 started ")
 h = u - i
 print("fun3 finished ")
 sem_fun3.release()


def fun4():
    global k
    sem_fun1.acquire()
    sem_fun2.acquire()
    print("fun4 started ")
    k = c + z
    print("fun4 finished ")
    sem_fun4.release()


def fun5():
    global l
    sem_fun3.acquire()
    sem_fun4.acquire()
    print("fun5 started ")
    l = h - k
    print("fun5 finished ")


a = int(input('Give a: '))
b = int(input('Give b: '))
d = int(input('Give d: '))
e = int(input('Give e: '))
u = int(input('Give u: '))
i = int(input('Give i: '))
c = 1
z = 1
h = 1
k = 1
l = 1

t1 = threading.Thread(target=fun1, args=(a, b))
t2 = threading.Thread(target=fun2, args=(d, e))
t3 = threading.Thread(target=fun3, args=(u, i))
t4 = threading.Thread(target=fun4)
t5 = threading.Thread(target=fun5)
t1.start()
t2.start()
t3.start()
t4.start()
t5.start()
t1.join()
t2.join()
t3.join()
t4.join()
t5.join()
print('c = ' + str(c))
print('z = ' + str(z))
print('h = ' + str(h))
print('k = ' + str(k))
print('l = ' + str(l))
print("All Threads done Exiting")