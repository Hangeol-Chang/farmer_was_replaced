# tree
from Common import harvest_full_field, move_to, instant_watering

def plant_tree(size = [0, 0], start_loc = [0, 0]):
	move_to(start_loc)

	max_x = min(get_world_size(), size[0] + start_loc[0]) - start_loc[0]
	max_y = min(get_world_size(), size[1] + start_loc[1]) - start_loc[1]

	for x in range(max_x):
		for y in range(max_y):
			if (x+y) % 2 == 0:
				plant(Entities.Tree)
			else:
				plant(Entities.Bush)
			instant_watering()
			move_to([start_loc[0] + x, min(start_loc[1] + y + 1, get_world_size() - 1)])
		move_to([min(start_loc[0] + x + 1, get_world_size() - 1), start_loc[1]])
	
def harvest_tree(size = [0, 0], start_loc = [0, 0], next_plant_func_single = None, next_plant_size = [0, 0], next_plant_start_loc = [0, 0]):
	harvest_full_field(size, start_loc, next_plant_func_single, next_plant_size, next_plant_start_loc, True)

def plant_tree_single(x, y):
	if (x+y) % 2 == 0:  
		plant(Entities.Tree)
	else:
		plant(Entities.Bush)