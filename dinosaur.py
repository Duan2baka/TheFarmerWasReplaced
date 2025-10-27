def add(x, tp):
	return (x[0] + tp[0], x[1] + tp[1])

def check(pos, tar):
	if tar == pos[0]:
		return True
	return tar not in pos

def check_valid(x):
	return x[0] >= 0 and x[0] < get_world_size() and x[1] >= 0 and x[1] < get_world_size()

def check_path(pos, st, end):
	q = [st]
	l = 0
	dir = [(-1, 0), (1, 0), (0, 1), (0, -1)]
	while len(q) > l:
		v = q[l]
		l += 1
		for i in dir:
			tar = add(v, i)
			if check_valid(tar) == False:
				continue
			if tar == end:
				return True
			if (tar not in q) and (tar not in pos):
				q.append(tar)
	return False

def getdir(pos, next):
	cur = pos[len(pos) - 1]
	lis = []
	if get_pos_x() < next[0]:
		lis = [(East, (1, 0)), (West, (-1, 0))]
	else:
		lis = [(West, (-1, 0)), (East, (1, 0))]
	if get_pos_y() < next[1]:
		lis.insert(1, (North, (0, 1)))
		lis.insert(2, (South, (0, -1)))
	else:
		lis.insert(1, (South, (0, -1)))
		lis.insert(2, (North, (0, 1)))

	for i in range(len(lis)):
		tar = add(cur, lis[i][1])
		if check_valid(tar) == False:
			continue
		if check(pos, tar) and check_path(pos, tar, next) and check_path(pos, next, pos[0]):
			return lis[i]
		
	lis = []
	if get_pos_x() < pos[0][0]:
		lis = [(East, (1, 0)), (West, (-1, 0))]
	else:
		lis = [(West, (-1, 0)), (East, (1, 0))]
	if get_pos_y() < pos[0][1]:
		lis.insert(1, (North, (0, 1)))
		lis.insert(2, (South, (0, -1)))
	else:
		lis.insert(1, (South, (0, -1)))
		lis.insert(2, (North, (0, 1)))

	for i in range(len(lis)):
		tar = add(cur, lis[i][1])
		if check_valid(tar) == False:
			continue
		if check(pos, tar) and check_path(pos, tar, pos[0]):
			return lis[i]

while True:
	clear()
	change_hat(Hats.Dinosaur_Hat)
	n = get_world_size()
	a = []
	len_snake = 1
	next = measure()
	next = (4, 4)
	pos = [(0, 0)]
	while len_snake <= n * n:
		if measure():
			pos.insert(0, pos[0])
			len_snake += 1
			next = measure()
			next = (4, 4)
		dir, tp = getdir(pos, next)
		move(dir)
		pos.pop(0)
		pos.append(add(pos[len(pos) - 1], tp))

	change_hat(Hats.Carrot_Hat)
