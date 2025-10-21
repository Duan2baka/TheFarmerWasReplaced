def check():
	if get_entity_type() == Entities.Treasure:
		harvest()
		return True
	return False
clear()
while True:
	#clear()
	
	plant(Entities.Bush)
	substance = get_world_size() * 2**(num_unlocked(Unlocks.Mazes) - 1)
	use_item(Items.Weird_Substance, substance)
	
	it1 = 1
	dir1 = [North, East, South, West]

	it2 = 2
	dir2 = [North, East, South, West]

	it3 = 3
	dir3 = [North, East, South, West]
	
	def solve1():
		print("1")
		if(get_entity_type() == Entities.Treasure):
			harvest()
			return
			
		global it1
		global dir1
		while True:
			if can_move(dir1[(it1 - 1) % 4]):
				move(dir1[(it1 - 1) % 4])
				it1 = (it1 - 1) % 4
			else:
				it1 = (it1 + 1) % 4
			if(get_entity_type() == Entities.Treasure):
				harvest()
				return
	
	def solve2():
		print("2")
		if(get_entity_type() == Entities.Treasure):
			harvest()
			return

		global it2
		global dir2
		while True:
			if can_move(dir2[(it2 - 1) % 4]):
				move(dir2[(it2 - 1) % 4])
				it2 = (it2 - 1) % 4
			else:
				it2 = (it2 + 1) % 4
			if(get_entity_type() == Entities.Treasure):
				harvest()
				return

	def solve3():
		print("3")
		if(get_entity_type() == Entities.Treasure):
			harvest()
			return
		
		global it3
		global dir3
		while True:
			if can_move(dir3[(it3 + 1) % 4]):
				move(dir3[(it3 + 1) % 4])
				it3 = (it3 + 1) % 4
			else:
				it3 = (it3 - 1) % 4
			if(get_entity_type() == Entities.Treasure):
				harvest()
				return
	spawn_drone(solve1)
	spawn_drone(solve2)
	spawn_drone(solve3)
	it = 0
	dir = [North, East, South, West]
	while measure():
		if(check()):
			break
		if can_move(dir[(it + 1) % 4]):
			move(dir[(it + 1) % 4])
			it = (it + 1) % 4
		else:
			it = (it - 1) % 4
		if(check()):
			break