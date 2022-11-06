from sympy import Determinant

matriz=[[1,2,3],[3,5,6],[6,7,8]]

def det_iterativa(matriz):
    "forma iterativa"
    matriz=matriz*2
    matriz.pop(-1)
    determinante=0
    for i in range(0,3):
        sumas=matriz[i][0]*matriz[i+1][1]*matriz[i+2][2]
        restas=matriz[i][2]*matriz[i+1][1]*matriz[i+2][0]
        determinante= determinante + (sumas-restas)
    print("determinante iterativa: ", determinante)

det_iterativa(matriz)

def det_recursiva(matrix, nivel=0, det=0):
    if nivel < 3:
        det += matrix[0][0] * matrix[1][1] * matrix[2][2]
    elif nivel >= 3 and nivel < 6:
        det += -matrix[0][2] * matrix[1][1] * matrix[2][0]
    else:
        print("El determinante recursiva:", det)
        return None
    matrix = [ matrix[0][1:3] + [matrix[0][0]],
               matrix[1][1:3] + [matrix[1][0]],
               matrix[2][1:3] + [matrix[2][0]] ]

    det_recursiva(matrix, nivel+1, det)    

det_recursiva(matriz)