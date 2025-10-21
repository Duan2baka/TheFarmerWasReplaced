clear()
Hats_list = [Hats.Traffic_Cone_Stack, Hats.Carrot_Hat, Hats.Brown_Hat, Hats.Green_Hat, Hats.Tree_Hat]

def farm(dir, move_dir):
	it = 0
	while True:
		for j in range(get_world_size()):
			check_and_harvest()
			if get_pos_x() < 2:
				if(get_ground_type() == Grounds.Grassland):
					till()
				plant(Entities.Sunflower)
			elif get_pos_y() < 3:
				plant(Entities.Grass)
			elif (get_pos_y() + get_pos_x()) % 2 == 1:
				plant(Entities.Tree)
			else:
				plant_carrot()
			move(move_dir)
		move(dir[it])
		it = 1 - it

def init_drone(num):
	#print(num)
	def run(n = num):
		#change_hat(Hats_list[n % len(Hats_list)])
		if 2 * n < get_world_size():
			for i in range(2 * n):
				move(North)
			farm([North, South], East)
		else:
			for i in range(2 * n - get_world_size() + 2):
				move(East)
			farm([East, West], North)
	return run

def check_and_harvest():
	if can_harvest():
		harvest()
	if get_water() <= 0.75 and num_items(Items.Water) > 0:
		use_item(Items.Water)

def plant_carrot():
	if(get_ground_type() == Grounds.Grassland):
		till()
	plant(Entities.Carrot)

it = 1
while num_drones() < max_drones():
	spawn_drone(init_drone(it))
	it += 1
while True:
	farm([North, South], East)