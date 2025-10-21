clear()
#st = get_tick_count() 
#till()
#plant(Entities.Pumpkin)
#while can_harvest() == False:
#    continue
#
#base = get_tick_count() - st
#quick_print("Base time: " + str(base))

T = 7

#while (0.2 ** T) * (get_world_size() ** 2) > 1:
#	T += 1

#T += 1
#print(T)

#def wait(t):
#	st = get_tick_count()
#	while get_tick_count() - st <= t:
#		continue

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
		while True:
			for i in range(siz[n]):
				for j in range(get_world_size()):
					plant_pumpkin()
					move(East)
				if i != siz[n] - 1:
					move(North)
			for i in range(siz[n] - 1):
				move(South)
	return run

def check_and_harvest():
	if get_water() <= 0.75 and num_items(Items.Water) > 0:
		use_item(Items.Water)
	if can_harvest():
		harvest()

def plant_pumpkin():
	if get_water() <= 0.75 and num_items(Items.Water) > 0:
		use_item(Items.Water)
	if(get_ground_type() == Grounds.Grassland):
		till()
	plant(Entities.Pumpkin)

while num_drones() < max_drones():
	spawn_drone(init_drone(num_drones()))

num = 0
for i in range(pos[max_drones()]):
	move(North)
while True:
	for i in range(siz[max_drones()]):
		for j in range(get_world_size()):
			plant_pumpkin()
			move(East)
		if i != siz[max_drones()] - 1:
			move(North)
	for i in range(siz[max_drones()] - 1):
		move(South)
	num += 1
	if num >= T:
		check_and_harvest()
		num = 0