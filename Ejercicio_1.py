
def TorreDeHanoi(Discos, agujaFuente, agujaDestino, agujaAuxiliar):
	if Discos == 0: 
		return None
	elif Discos > 0:
		TorreDeHanoi(Discos-1, agujaFuente, agujaAuxiliar, agujaDestino)
		print("Mover disco: ", Discos, "desde la aguja: ", agujaFuente, "hasta la aguja: ", agujaDestino) 


TorreDeHanoi(74,1,2,3)
