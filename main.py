clear()
def check_and_harvest(sunflower):
	if can_harvest():
		if(get_entity_type() != Entities.Sunflower or measure() >= sunflower):
			harvest()
	if get_water() <= 0.75 and num_items(Items.Water) > 0:
		use_item(Items.Water)
def plant_carrot():
	if(get_ground_type() == Grounds.Grassland):
		till()
	plant(Entities.Carrot)
def plant_pumpkin():
	if(get_ground_type() == Grounds.Grassland):
		till()
	plant(Entities.Pumpkin)
	# use_item(Items.Weird_Substance)
	#if i == 5 and j == 5:
	#	harvest()
		
while True:
	max_power = -1
	for i in range(get_world_size()):
		for j in range(get_world_size()):
			check_and_harvest(max_power)
			if i < 8 and j < 8:
				plant_pumpkin()
			elif (i + j) % 2 == 1:
				if (i < 11 and i > 1) or num_items(Items.Carrot) < 2:
					plant(Entities.Tree)
				else:
					if(get_ground_type() == Grounds.Grassland):
						till()
					plant(Entities.Sunflower)
					res = measure()
					if res > max_power:
						max_power = res
			else:
				if i < 10:
					plant_carrot()
			move(East)
		move(North)