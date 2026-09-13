# cactus order
from Common import *

def harvest_cactus_order(size = [0, 0], start_loc = [0, 0]):
	move_to(start_loc)
	max_x = min(get_world_size(), size[0] + start_loc[0])
	max_y = min(get_world_size(), size[1] + start_loc[1])

	

	cactuss = []
	for x in range(start_loc[0], max_x):
		cactuss.append([])
		for y in range(start_loc[1], max_y):
			cactuss[x-start_loc[0]].append(measure())

			if get_pos_y() < max_y - 1:
				move_to([x, y+1])
		move_to([min(max_x - 1, x+1), start_loc[1]])

	pass