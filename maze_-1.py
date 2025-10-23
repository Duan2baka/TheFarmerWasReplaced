set_world_size(4)

clear()

plant(Entities.Bush)
substance = get_world_size() * 2**(num_unlocked(Unlocks.Mazes) - 1)
print(substance)
use_item(Items.Weird_Substance, substance)