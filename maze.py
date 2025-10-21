def check():
	if get_entity_type() == Entities.Treasure:
		harvest()
		return True
	return False

def solve():
	it = 0
	dir = [North, East, South, West]
	while True:
		if can_move(dir[(it + 1) % 4]):
			move(dir[(it + 1) % 4])
			it = (it + 1) % 4
		else:
			it = (it - 1) % 4
		if(check()):
			return
				
while True:
	clear()
	plant(Entities.Bush)
	substance = get_world_size() * 2**(num_unlocked(Unlocks.Mazes) - 1)
	use_item(Items.Weird_Substance, substance)
	solve()
