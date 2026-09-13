from Common import move_to, plant_full_field, harvest_full_field

SUNFLOWER_COLLECT_COUNT = 30

def plant_sunflower(size = [0, 0], start_loc = [0, 0]):
	move_to()
	plant_full_field(Entities.Sunflower, size, start_loc)

def _get_sunflower_leaf_counts_and_loc_ordered(size = [0, 0], start_loc = [0, 0]):
	ret = []
	move_to(start_loc)
	for x in range(size[0]):
		for y in range(size[1]):

			added = False
			for i in range(len(ret)):
				if ret[i][0] < measure():
					ret.insert(i, [measure(), x, y])
					added = True
					break
			if added == False:
				ret.append([measure(), x, y])

			move(North)
		while get_pos_y() > 0:
			move(South) 
		move(East)
	while get_pos_x() > 0:
		move(West)
	return ret

def harvest_sunflower(size=[0, 0], start_loc = [0, 0], next_plant_func_single = None, next_plant_size = [0, 0], next_plant_start_loc = [0, 0]):
	move_to(start_loc)
	leafs = _get_sunflower_leaf_counts_and_loc_ordered(size, start_loc)

	for i in range(min(SUNFLOWER_COLLECT_COUNT, len(leafs))):
		leaf = leafs.pop(0)
		harvest_x = leaf[1]
		harvest_y = leaf[2]
		move_to([harvest_x, harvest_y])
		harvest()
		next_plant_func_single(harvest_x, harvest_y)

def plant_sunflower_single(x, y):
	plant(Entities.Sunflower)