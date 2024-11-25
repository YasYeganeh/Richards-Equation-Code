import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
mpl.rc('figure', max_open_warning = 0)

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

plt.xlabel("x (cm)", fontsize=15)
plt.ylabel("Teta (soil moisture content)", fontsize=15)
plt.ylim((0,1))
plt.title("soil moisture profile from t=0min to t=120min")
# plt.savefig(f"1initial.jpg")

D=A
plt.plot(np.append(Dx, 100), A)
for t in Dt:
    print(t)
    M= np.zeros((n))
    for x in Dx[1:]:
        # print(x)
        # print(D[x])
        teta_new=0.4*D[x-1]+0.2*D[x]+0.4*D[x+1]
        D[x]=teta_new
        # print(D[x])
        plt.plot(np.append(Dx, 100), D)
        plt.xlabel("x (cm)", fontsize=15)
        plt.ylabel("Teta (soil moisture content)", fontsize=15)
        plt.ylim((0, 1))
        plt.title("soil moisture profile from t=0min to t=120min")
        # plt.savefig(f"{t}minutepast.jpg")
plt.show()
