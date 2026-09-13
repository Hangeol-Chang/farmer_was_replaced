from Common import move_to, plant_full_field, harvest_full_field

SUNFLOWER_COLLECT_COUNT = 30

def plant_sunflower(size = [0, 0], start_loc = [0, 0]):
	move_to()
	plant_full_field(Entities.Sunflower, size, start_loc)

def _get_sunflower_leaf_counts_and_loc_ordered(size = [0, 0], start_loc = [0, 0]):
	ret = []
	move_to(start_loc)

	max_x = min(get_world_size(), start_loc[0] + size[0])
	max_y = min(get_world_size(), start_loc[1] + size[1])

	for x in range(start_loc[0], max_x):
		for y in range(start_loc[1], max_y):
			added = False
			for i in range(len(ret)):
				if ret[i][0] < measure():
					ret.insert(i, [measure(), x, y])
					added = True
					break
			if added == False:
				ret.append([measure(), x, y])

			move_to([x, min(y + 1, get_world_size() - 1)])
		move_to([min(x + 1, get_world_size() - 1), start_loc[1]])
	move_to(start_loc)
	return ret

def harvest_sunflower(size=[0, 0], start_loc = [0, 0]):
	move_to(start_loc)
	leafs = _get_sunflower_leaf_counts_and_loc_ordered(size, start_loc)

	for i in range(min(SUNFLOWER_COLLECT_COUNT, len(leafs))):
		leaf = leafs.pop(0)
		harvest_x = leaf[1]
		harvest_y = leaf[2]
		move_to([harvest_x, harvest_y])
		harvest()

def plant_sunflower_single(x, y):
	plant(Entities.Sunflower)