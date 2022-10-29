
"determinante matriz iterativa"
from sympy import Determinant


matriz=[[1,2,3],[3,5,6],[6,7,8]]
"""1,2,3
   3,5,6
   6,7,8
   
   (1*5*8)+(3*7*3)+(2*6*6)-(()) """
#matriz=matriz*2
#matriz.pop(-1)
#print(matriz)

def det_iterativa(matriz):
    matriz=matriz*2
    matriz.pop(-1)
    for i in range(0,3):
        termino1=matriz[i][0]*matriz[i-1][1]*matriz[i-2][2]
        termino2=matriz[i][0]*matriz[i+1][1]*matriz[i+2][2]
    determinante= termino1-termino2
    print(determinante)

det_iterativa(matriz)

