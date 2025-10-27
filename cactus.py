clear()

size = get_world_size() // max_drones()
num = get_world_size() - size * max_drones()
pos = [0]
siz = [0]
for i in range(max_drones() - num):
	siz.append(size)
for i in range(num):
	siz.append(size + 1)
sum = 0
for i in range(max_drones()):
	sum += siz[i + 1]
	pos.append(get_world_size() - sum)

def init_drone(num):
	def run(n = num):
		for i in range(pos[n]):
			move(North)
		while num_items(Items.Cactus) < 33554432:
			for i in range(siz[n]):
				for j in range(get_world_size()):
					plant_cactus()
					ws = measure(West)
					cur = measure()
					if get_pos_x() > 0:
						if ws != None and cur != None and cur < ws:
							swap(West)
					st = measure(South)
					cur = measure()
					if get_pos_y() > 0  :
						if st != None and cur != None and cur < st:
							swap(South)
					move(East)
				if i != siz[n] - 1:
					move(North)
			for i in range(siz[n] - 1):
				move(South)
	return run

def check_and_harvest():
	if can_harvest():
		harvest()

def plant_cactus():
	if(get_ground_type() == Grounds.Grassland):
		till()
	plant(Entities.Cactus)

while num_drones() < max_drones():
	spawn_drone(init_drone(num_drones()))
swapped = 0
while num_items(Items.Cactus) < 33554432:
	swapped = 0
	for i in range(siz[max_drones()]):
		for j in range(get_world_size()):
			plant_cactus()
			if get_pos_x() > 0:
				ws = measure(West)
				cur = measure()
				if ws != None and cur != None and cur < ws:
					swap(West)
					swapped = 1
			if get_pos_y() > 0:
				st = measure(South)
				cur = measure()
				if st != None and cur != None and cur < st:
					swap(South)
					swapped = 1
			move(East)
		if i != siz[max_drones()] - 1:
			move(North)
	for i in range(siz[max_drones()] - 1):
		move(South)
	if swapped == 0:
		for i in range(get_world_size()):
			if swapped == 1:
				break
			for j in range(get_world_size()):
				if swapped == 1:
					break
				move(East)
				if get_pos_x() > 0:
					ws = measure(West)
					cur = measure()
					if ws != None and cur != None and cur < ws:
						swap(West)
						swapped = 1
				if get_pos_y() > 0:
					st = measure(South)
					cur = measure()
					if st != None and cur != None and cur < st:
						swap(South)
						swapped = 1
				
			move(North)
		if swapped == 0:
			check_and_harvest()
		else:
			while get_pos_x() != 0:
				if get_pos_x() < get_world_size() // 2:
					move(West)
				else:
					move(East)
			while get_pos_y() != 0:
				if get_pos_y() < get_world_size() // 2:
					move(South)
				else:
					move(North)
