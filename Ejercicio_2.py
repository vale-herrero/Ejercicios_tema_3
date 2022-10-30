
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
    "forma iterativa"
    matriz=matriz*2
    matriz.pop(-1)
    determinante=0
    for i in range(0,3):
        sumas=matriz[i][0]*matriz[i+1][1]*matriz[i+2][2]
        restas=matriz[i][2]*matriz[i+1][1]*matriz[i+2][0]
        determinante= determinante + (sumas-restas)
    print(determinante)

det_iterativa(matriz)

def det_recursiva(matriz):
    matriz=matriz*2
    matriz.pop(-1)
    i=0
    sumas=matriz[i][0]*matriz[i+1][1]*matriz[i+2][2]
    det_iterativa(sumas)
    restas=matriz[i][2]*matriz[i+1][1]*matriz[i+2][0]
    i+=1
    det_recursiva(restas)
    print(det_recursiva(sumas)-det_recursiva(restas))
det_recursiva(matriz)
