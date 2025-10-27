clear()
companion_set = {}
world_size = get_world_size()

def my_plant(entity_type):
	if entity_type in (Entities.Carrot, Entities.Bush, Entities.Tree) and get_ground_type() != Grounds.Soil:
		till()
	if entity_type == Entities.Grass and get_ground_type() == Grounds.Soil:
		till()
	if entity_type == Entities.Tree and (get_pos_x() + get_pos_y()) %2 == 0:
		return
	plant(entity_type)
	if entity_type == Entities.Tree and get_water() < 0.2:
		use_item(Items.Water)

def func(num):
	def run(n = num):
		global world_size
		map = []
		x = get_pos_x()
		for i in range(world_size):
			map.append(-1)
		while True:
			move(North)
			if not can_harvest():
				continue
			y = get_pos_y()
			tar = map[y]
			#if get_entity_type() == Entities.Tree:
			#	while can_harvest() == False:
			#		use_item(Items.Fertilizer)
			#	use_item(Items.Weird_Substance)
			while harvest() == False:
				continue
			if tar != -1:
				my_plant(tar)
				map[y] = -1
				if y == Entities.Tree and (x + y) % 2 == 1:
					res = get_companion()
					if res == None:
						continue
					entity, (tx, ty) = res
					if tx == 0:
						map[ty] = entity
			elif (x + y) % 2 == 1:
				my_plant(Entities.Tree)
				res = get_companion()
				if res == None:
					continue
				entity, (tx, ty) = res
				if tx == x:
					map[ty] = entity
			else:
				my_plant(Entities.Bush)
				
	
	return run
while num_drones() < max_drones():
	spawn_drone(func(num_drones))
	move(East)
func(0)()