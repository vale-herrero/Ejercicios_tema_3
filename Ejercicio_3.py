
from pickle import TRUE


class Nave():
    def __init__(self, nombre, largo, tripulacion, cantidad_pasajeros):
        self.nombre= nombre
        self.largo=largo
        self.tripulacion= tripulacion
        self.cantidad_pasajeros=cantidad_pasajeros

    def __str__(self):
        return "{}".format(self.nombre)




print("------------punto 1-----------------")
def ordenar_nombre(lista_naves):
    lista_ordenada=sorted(lista_naves,key=lambda x:x.nombre.lower())
    print([i.nombre for i in lista_ordenada])
    return lista_ordenada

def ordenar_largo(lista_naves):
    lista_ordenada=sorted(lista_naves,key=lambda x:x.largo, reverse = True)
    print([(i.nombre, i.largo) for i in lista_ordenada])
    return lista_ordenada
    

halcon_milenario= Nave("Halcón Milenario",34.37,3,1)
x_wing = Nave("X-wing", 12.5,2, 346)
TIE_fighter=Nave("TIE Fighter", 6.3, 1, 45)
Estrella_muerte=Nave("Estrella de la muerte", 178,200000, 1000000)
quinta= Nave("At-23000",134,3, 453)
sexta = Nave("Atras-24", 45,3,6)
naves=[halcon_milenario, x_wing,TIE_fighter,Estrella_muerte, quinta, sexta]

ordenar_nombre(naves)
ordenar_largo(naves)

print("------------punto 2-----------------")
print(halcon_milenario.__dict__)
print(Estrella_muerte.__dict__)

print("------------punto 3-----------------")

def buscar_cantidad_pasajeros(lista_naves):
    lista_ordenada=sorted(lista_naves,key=lambda x:x.cantidad_pasajeros, reverse= True)
    print([(i.nombre, i.cantidad_pasajeros) for i in lista_ordenada[0:5]])

buscar_cantidad_pasajeros(naves)

print("------------punto 4-----------------")

def tripulacion_mayor(lista_naves):
    lista_ordenada=sorted(lista_naves,key=lambda x:x.tripulacion, reverse= True)
    print(lista_ordenada[0].nombre, lista_ordenada[0].tripulacion)

tripulacion_mayor(naves)

print("------------punto 5-----------------")

def nombre_at(lista_naves):
    lista_AT= []
    for nave in lista_naves:
        if nave.nombre[0:2].lower()== "at":
            lista_AT.append(nave.nombre)
    print(lista_AT)

nombre_at(naves)

print("------------punto 6-----------------")

def cantidad_pasajeros(lista_naves):
    lista_pasajeros_6= []
    for nave in lista_naves:
        if nave.cantidad_pasajeros>=6:
            lista_pasajeros_6.append(nave)
    print([nave.nombre for nave in lista_pasajeros_6])

cantidad_pasajeros(naves)


print("------------punto 7-----------------")

def grande_pequeño(lista_naves):
    lista_ordenada=sorted(lista_naves,key=lambda x:x.largo)
    print("Nave más pequeña: {} y nave más grande: {}".format(lista_ordenada[0].__dict__,lista_ordenada[-1].__dict__))

grande_pequeño(naves)