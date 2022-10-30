

def move(discos, tubo_inicial=1, auxiliar=2, tubo_final=3):

	if discos > 0:

		move(discos - 1, tubo_inicial, tubo_final, auxiliar)
		print(f'Move disk {discos} from {tubo_inicial} —> {tubo_final}')
		move(discos - 1, auxiliar, tubo_inicial, tubo_final)

if __name__ == '__main__':

	n = 64
	move(n)