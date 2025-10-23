#set_world_size(18)

def func(num):
	if num == 1:
		def run(it = 1, dir = [North, East, South, West], face = 1):
			while True:
				if random() < 0.02:
					tmp = ((random() * 10) / 2.5) // 1
					it = tmp % 4
				if can_move(dir[(it - face) % 4]):
					move(dir[(it - face) % 4])
					it = (it - face) % 4
				else:
					it = (it + face) % 4
				if get_entity_type() == Entities.Treasure:
					harvest()
		return run
	
	if num == 2:
		def run(it = 2, dir = [North, East, South, West], face = 1):
			while True:
				if random() < 0.02:
					tmp = ((random() * 10) / 2.5) // 1
					it = tmp % 4
				if can_move(dir[(it - face) % 4]):
					move(dir[(it - face) % 4])
					it = (it - face) % 4
				else:
					it = (it + face) % 4
				if get_entity_type() == Entities.Treasure:
					harvest()
		return run
			
	if num == 3:
		def run(it = 1, dir = [North, East, South, West], face = -1):
			while True:
				if random() < 0.02:
					tmp = ((random() * 10) / 2.5) // 1
					it = tmp % 4
				if can_move(dir[(it - face) % 4]):
					move(dir[(it - face) % 4])
					it = (it - face) % 4
				else:
					it = (it + face) % 4
				if get_entity_type() == Entities.Treasure:
					harvest()
		return run
			
	if num == 4:
		def run(it = 0, dir = [North, East, South, West], face = -1):
			while True:
				if random() < 0.02:
					tmp = ((random() * 10) / 2.5) // 1
					it = tmp % 4
				if can_move(dir[(it - face) % 4]):
					move(dir[(it - face) % 4])
					it = (it - face) % 4
				else:
					it = (it + face) % 4
				if get_entity_type() == Entities.Treasure:
					harvest()
		return run
			
	if num >= 5:
		def run(it = 0, dir = [North, East, South, West], face = -1):
			change_hat(Hats.Traffic_Cone_Stack)
			while True:
				if get_entity_type() == Entities.Treasure:
					harvest()
				tmp = ((random() * 10) / 2.5) // 1
				if can_move(dir[tmp % 4]):
					move(dir[tmp % 4])
		return run
		
clear()
while True:
	plant(Entities.Bush)
	substance = get_world_size() * 2**(num_unlocked(Unlocks.Mazes) - 1)
	use_item(Items.Weird_Substance, substance)
	while num_drones() < max_drones():
		spawn_drone(func(num_drones() % 4 + 1))
	it = 0
	dir = [North, East, South, West]
	while measure():
		if get_entity_type() == Entities.Treasure:
			harvest()
			
		if can_move(dir[(it + 1) % 4]):
			move(dir[(it + 1) % 4])
			it = (it + 1) % 4
		else:
			it = (it - 1) % 4