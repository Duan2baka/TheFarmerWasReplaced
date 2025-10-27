clear()

# first 5 hay to unlock "while"

while num_items(Items.Hay) < 5:
	harvest()

unlock(Unlocks.Loops) 

# 20 hay to unlock "speed 1"

while num_items(Items.Hay) < 20:
	harvest()

unlock(Unlocks.Speed)

# 30 hay to unlock "expand 1"

while num_items(Items.Hay) < 30:
	harvest()

unlock(Unlocks.Expand)

# 100 hay to unlock "grass 1"

while num_items(Items.Hay) < 100:
	move(North)
	harvest()

unlock(Unlocks.Grass)

# 50 hay to unlock "Bush(plant)"

while num_items(Items.Hay) < 50:
	harvest()
	move(North)

unlock(Unlocks.Plant)

# 20 wood to unlock "speed 2"

while num_items(Items.Wood) < 20:
	harvest()
	plant(Entities.Bush)
	move(North)

unlock(Unlocks.Speed)


# 20 wood to unlock "expand 2"

while num_items(Items.Wood) < 20:
	harvest()
	plant(Entities.Bush)
	move(North)

unlock(Unlocks.Expand)

world_size = get_world_size()

# 50 wood to unlock "water 1"

while num_items(Items.Wood) < 20:
	for i in range(world_size):
		harvest()
		plant(Entities.Bush)
		move(East)
	harvest()
	plant(Entities.Bush)
	move(North)

unlock(Unlocks.Watering)

def water_plant(entity):
	if get_water() < 0.2:
		use_item(Item.Water)
	return plant(entity)
	


# 50 wood to unlock "carrot 1"


while True:
	continue