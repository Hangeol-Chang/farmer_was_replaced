# if flower > 10 -> get max leaf flower
	
flower_boundary = [2, 5]
	
def create_sunflower_farm():
	for x in range(flower_boundary[0]):
		for y in range(flower_boundary[1]):
			harvest()
			plant(Entities.Sunflower)
			move(North)
		while get_pos_y() > 0:
			move(South) 
		move(East)
	while get_pos_x() > 0:
		move(West)
	
def _get_sunflower_leaf_counts():
	ret = [[], []]
	for x in range(flower_boundary[0]):
		for y in range(flower_boundary[1]):
			ret[x].append(measure())
			move(North)
		while get_pos_y() > 0:
			move(South) 
		move(East)
	while get_pos_x() > 0:
		move(West)
	return ret
	
def harvest_sunflower():
	# goto 0, 0
	while get_pos_x() > 0:
		move(West)
	while get_pos_y() > 0:
		move(South)
	
	leafs = _get_sunflower_leaf_counts()
	harvest_loc = [0, 0] # x, y
	
	maxleaf = 0
	x = 0
	for ite in leafs:
		y = 0
		for leaf in ite:
			if leaf > maxleaf :
				harvest_loc = [x, y]
				maxleaf = leaf
			y += 1
		x += 1
	# move to harvest loc
	while get_pos_x() < harvest_loc[0] :
		move(East)
	while get_pos_y() < harvest_loc[1] :
		move(North)
	
	if can_harvest() == False:
		use_item(Items.Fertilizer)
	harvest()
	plant(Entities.Sunflower)
	
	# reset sunflower ground when maxLeaf < 10
	if maxleaf < 10:
		create_sunflower_farm()

def _get_sunflower_leaf_counts_and_loc():
	ret = []
	for x in range(flower_boundary[0]):
		for y in range(flower_boundary[1]):
			ret.append([measure(), x, y])
			move(North)
		while get_pos_y() > 0:
			move(South) 
		move(East)
	while get_pos_x() > 0:
		move(West)
	return ret

def _get_sunflower_leaf_counts_and_loc_ordered():
	ret = []
	for x in range(flower_boundary[0]):
		for y in range(flower_boundary[1]):

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


def harvest_all_sunflower():
	# goto 0, 0
	while get_pos_x() > 0:
		move(West)
	while get_pos_y() > 0:
		move(South)
	
	leafs = _get_sunflower_leaf_counts_and_loc_ordered()

	for i in range(10):
		leaf = leafs.pop(0)
		harvest_x = leaf[1]
		harvest_y = leaf[2]
		while get_pos_x() < harvest_x :
			move(East)
		while get_pos_x() > harvest_x :
			move(West)
		while get_pos_y() < harvest_y :
			move(North)
		while get_pos_y() > harvest_y :
			move(South)
			
		while can_harvest() == False:
			if num_items(Items.Fertilizer) > 0:
				use_item(Items.Fertilizer)
			else:
				pass

		harvest()
		plant(Entities.Sunflower)

		while get_water() <= 0.7 and num_items(Items.Water) > 0:
			use_item(Items.Water)

		added = False
		for j in range(len(leafs)):
			if leafs[j][0] < measure():
				leafs.insert(j, [measure(), harvest_x, harvest_y])
				added = True
				break
		if added == False:
			leafs.append([measure(), harvest_x, harvest_y])

def is_flower_ground(x, y):
	if x < flower_boundary[0] and y < flower_boundary[1] :
		return True
	return False
	