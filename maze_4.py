set_world_size(8)

def move_to(x, y):
	# print(x,y)
	while get_pos_x() != x:
		move(East)
	while get_pos_y() != y:
		move(North)

def func(num, sub):
	def run(n = num, substance = sub):
		move_to(num // 8, num - num // 8 * 8)
		flag = False
		while True:
			if flag or num_drones() == max_drones():
				flag = True
				if get_entity_type() == Entities.Treasure:
					use_item(Items.Weird_Substance, substance)
					if get_entity_type() == Entities.Treasure:
						harvest()
						plant(Entities.Bush)
						use_item(Items.Weird_Substance, substance)
				if measure() == None:
					plant(Entities.Bush)
					use_item(Items.Weird_Substance, substance)
			
	return run
	
clear()
substance = 4 * 2 ** (num_unlocked(Unlocks.Mazes) - 1)
while True:
	while num_drones() < max_drones():
		spawn_drone(func(num_drones(), substance))
	func(0, substance)()