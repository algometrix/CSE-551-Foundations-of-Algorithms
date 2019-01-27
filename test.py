
import matplotlib.pyplot as plt 
from timeit import default_timer as timer

def test(n):
    if n < 2:
        return n
    else:
        result = test(n - 2) + test(n - 1) 
        return result

def test1(n):
    i = 1;j = 0
    for i in range(1, n):
        j = i + j
        i = j - i

    return j


def test2(n):
    i = 1
    j = 0
    k = 0
    h = 1
    while n > 0:
        if (n%2!=0):
            t = j*h
            j = i*h + j*k + t
            i = i*k + t
        
        t = h**2
        h = 2*k*h + t
        k = k**2 + t
        n = n//2
    
    return j

def randome_data(n):
    i = 1
    while n/2 > 0:
        i = i * 2
        n = n // 2

    return i

x = []
y = []
for i in range(0):
    x.append(i)
    start = timer()
    result = test2(i)
    print(result, end = ' ')
    end = timer()
    time_elapsed = end-start
    y.append(1000*time_elapsed)

#plt.plot(x, y) 
#plt.show()
