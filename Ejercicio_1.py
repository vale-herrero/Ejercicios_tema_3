def move(disks, tubo_inicial=1, auxiliary=2, tubo_final=3):

	if disks > 0:

		# move `n-1` discs from source to auxiliary using the target
		# as an intermediate pole
		move(disks - 1, tubo_inicial, tubo_final, auxiliary)

		# move one disc from source to target
		print(f'Move disk {disks} from {tubo_inicial} —> {tubo_final}')

		# move `n-1` discs from auxiliary to target using the source
		# as an intermediate pole
		move(disks - 1, auxiliary, tubo_inicial, tubo_final)


# Tower of Hanoi Problem
if __name__ == '__main__':

	n = 10
	move(n)