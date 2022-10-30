
from pickle import TRUE


class Nave():
    def __init__(self, nombre, largo, tripulacion, cantidad_pasajeros):
        self.nombre= nombre
        self.largo=largo
        self.tripulacion= tripulacion
        self.cantidad_pasajeros=cantidad_pasajeros

    def __str__(self):
        return "{}".format(self.nombre)




#punto 1
def ordenar(lista_naves):
    lista_ordenada=sorted(lista_naves,key=lambda x:(x.nombre, x.largo))
    return lista_ordenada
    #print([(i.nombre,i.largo) for i in lista_ordenada])
    

halcon_milenario= Nave("Halcón Milenario",34.37, "piloto, copiloto y 2 artilleros",1000)
x_wing = Nave("X-wing", 12.5,"1 piloto y 1 androide", 346)
TIE_fighter=Nave("TIE Fighter", 6.3, "1 piloto", 45)
Estrella_muerte=Nave("Estrella de la muerte", 178,"825.984 soldados de asalto, 100.000 pilotos militares y pasajeros civiles.", 1000000)
quinta= Nave("quinta",134,"piloto y pasajeros", 453)
sexta = Nave("sexta", 45,"copiloto, piloto, androide",6)
naves=[halcon_milenario, x_wing,TIE_fighter,Estrella_muerte, quinta, sexta]

naves=ordenar(naves)

#punto 2
#print(halcon_milenario.__dict__)
#print(Estrella_muerte.__dict__)

#punto 3

def buscar(lista_naves):
    lista_ordenada=sorted(lista_naves,key=lambda x:x.cantidad_pasajeros, reverse= True)
    print([(i.nombre, i.cantidad_pasajeros) for i in lista_ordenada])

buscar(naves)