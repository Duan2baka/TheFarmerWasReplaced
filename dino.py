
while True:
	clear()
	change_hat(Hats.Dinosaur_Hat)
	n = get_world_size()
	a = []
	len_snake = 1
	dir = [East, West]
	while len_snake < n * n:
		for i in range(get_world_size() - 1):
			if measure():
				len_snake += 1
			move(North)
		if measure():
			len_snake += 1
		move(East)
		t = 0
		for j in range(get_world_size()):
			for i in range(get_world_size() - 2):
				if measure():
					len_snake += 1
				move(dir[t])
			t = 1 - t
			if measure():
				len_snake += 1
			move(South)
		if measure():
			len_snake += 1
		move(West)

	change_hat(Hats.Carrot_Hat)
