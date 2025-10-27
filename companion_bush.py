clear()
companion_set = {}
world_size = get_world_size()

def my_plant(entity_type):
	if entity_type in (Entities.Carrot, Entities.Bush, Entities.Tree) and get_ground_type() != Grounds.Soil:
		till()
	if entity_type == Entities.Grass:
		if get_ground_type() == Grounds.Soil:
			till()
	else:
		plant(entity_type)
	if entity_type == Entities.Bush and get_water() < 0.2:
		use_item(Items.Water)

def check():
	harvest()
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
			harvest()
			y = get_pos_y()
			tar = map[y]
			if tar != -1:
				my_plant(tar)
				map[y] = -1
				if y == Entities.Bush:
					res = get_companion()
					if res == None:
						continue
					entity, (tx, ty) = res
					if tx == 0:
						map[ty] = entity
			else:
				my_plant(Entities.Bush)
				res = get_companion()
				if res == None:
					continue
				entity, (tx, ty) = res
				if tx == x:
					map[ty] = entity
	
	return run
while num_drones() < max_drones():
	spawn_drone(func(num_drones))
	move(East)
func(0)()