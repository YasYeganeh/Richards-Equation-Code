import numpy as np
import matplotlib.pyplot as plt

Dt=np.arange(1,121)
# print(Dt)
Dx=np.arange(0,99) # np.arange(0,100)
# print(Dx)
n=100
A = np.ones((n))*0.2
# print(A)
# print(A[99])
A[0]=0.7
# print(A)

D=A
for t in Dt:
    print(t)
    M= np.zeros((n))
    for x in Dx[1:]:
        # print(x)
        # print(D[x])
        teta_new=0.4*D[x-1]+0.2*D[x]+0.4*D[x+1]
        D[x]=teta_new
        # print(D[x])
    print(D)

