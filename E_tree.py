# tree
from Common import harvest_full_field, move_to, instant_watering

def plant_tree(size = [0, 0], start_loc = [0, 0]):
	move_to(start_loc)
	max_x = min(get_world_size(), size[0] + start_loc[0])
	max_y = min(get_world_size(), size[1] + start_loc[1])

	for x in range(start_loc[0], max_x):
		for y in range(start_loc[1], max_y):
			if (x+y) % 2 == 0:
				plant(Entities.Tree)
			else:
				plant(Entities.Bush)
			instant_watering()
			
			if get_pos_y() < max_y - 1:
				move_to([x, y+1])
		move_to([min(max_x - 1, x+1), start_loc[1]])

def harvest_tree(size = [0, 0], start_loc = [0, 0]):
	harvest_full_field(size, start_loc, True)

def plant_tree_single(x, y):
	if (x+y) % 2 == 0:  
		plant(Entities.Tree)
	else:
		plant(Entities.Bush)