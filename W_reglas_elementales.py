import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
#matplotlib inline

# DEFINIMOS AUTOMATA EN LA GENERACION

L = 200
X = np.zeros([1,L])
middle = int(np.floor(L/2))
X[0][middle-1]= 1
X[0][middle]= 1
X[0][middle+1]= 1

#DEFINIMOS REGLA 30

def rule_30(X:float,N:int,L:int):
    """
    rule_30 aplica la regla 30 de Wolfram durante N generaciones

    :param X: autómata
    :param N: número de generaciones 
    :param L: largo del autómata celular unidimensional  
    :return: autómata celular en la generación N, X_N
    """ 
    X_N = np.zeros([N,L])
    X_N[0][:] = X
    for gen in range(1,N):
        for i in range(1,L-1):
            Xleft = X_N[gen-1][i-1]
            Xright = X_N[gen-1][i+1]
            Xcenter = X_N[gen-1][i]
            if Xleft==1 and Xcenter==1 and Xright ==1:
                X_N[gen][i]=0
            if Xleft==1 and Xcenter==1 and Xright ==0:
                X_N[gen][i]=0
            if Xleft==1 and Xcenter==0 and Xright ==1:
                X_N[gen][i]=0
            if Xleft==1 and Xcenter==0 and Xright ==0:
                X_N[gen][i]=1
            if Xleft==0 and Xcenter==1 and Xright ==1:
                X_N[gen][i]=1
            if Xleft==0 and Xcenter==1 and Xright ==0:
                X_N[gen][i]=1
            if Xleft==0 and Xcenter==0 and Xright ==1:
                X_N[gen][i]=1
            if Xleft==0 and Xcenter==0 and Xright ==0:
                X_N[gen][i]=0
    return X_N

def rule_182(X:float,N:int,L:int):
    """
    rule_30 aplica la regla 30 de Wolfram durante N generaciones

    :param X: autómata generación 0
    :param N: número de generaciones  
    :return: autómata celular en la generación N, X_N
    """ 
    X_N = np.zeros([N,L])
    X_N[0][:] = X
    for gen in range(1,N):
        for i in range(1,L-1):
            Xleft = X_N[gen-1][i-1]
            Xright = X_N[gen-1][i+1]
            Xcenter = X_N[gen-1][i]
            if Xleft==1 and Xcenter==1 and Xright ==1:
                X_N[gen][i]=0
            if Xleft==1 and Xcenter==1 and Xright ==0:
                X_N[gen][i]=0
            if Xleft==1 and Xcenter==0 and Xright ==1:
                X_N[gen][i]=0
            if Xleft==1 and Xcenter==0 and Xright ==0:
                X_N[gen][i]=1
            if Xleft==0 and Xcenter==1 and Xright ==1:
                X_N[gen][i]=1
            if Xleft==0 and Xcenter==1 and Xright ==0:
                X_N[gen][i]=1
            if Xleft==0 and Xcenter==0 and Xright ==1:
                X_N[gen][i]=1
            if Xleft==0 and Xcenter==0 and Xright ==0:
                X_N[gen][i]=0
    return X_N


#GRAFICAMOS 

# Aplicamos la regla del autómata celular
gen = 100
X_N = rule_30(X,gen,L)

# Parámetros para graficar en dos colores
cmapmine = ListedColormap(['w', 'k'], N=2)

# Plot matrix
plt.imshow(X_N, cmap=cmapmine, vmin=0, vmax=1)
ax = plt.gca()
ax.set_axis_off()
plt.show()
