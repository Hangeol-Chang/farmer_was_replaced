def move_to(start_loc = [0, 0]):
	while get_pos_x() > start_loc[0]: 
		move(West)
	while get_pos_x() < start_loc[0]: 
		move(East)
	while get_pos_y() > start_loc[1]: 
		move(South)
	while get_pos_y() < start_loc[1]: 
		move(North)

def instant_watering():
	if num_items(Items.Water) > 0:
		if get_water() < 0.3:
			while get_water() < 0.8 and num_items(Items.Water) > 0:
				use_item(Items.Water)
	return

def plant_full_field(entity, size = [0, 0], start_loc = [0, 0]):
	move_to(start_loc)
	max_x = min(get_world_size(), size[0] + start_loc[0])
	max_y = min(get_world_size(), size[1] + start_loc[1])

	for x in range(start_loc[0], max_x):
		for y in range(start_loc[1], max_y):
			if can_harvest():
				harvest()
			plant(entity)
			instant_watering()

			if get_pos_y() < max_y - 1:
				move_to([x, y+1])
		move_to([min(max_x - 1, x+1), start_loc[1]])

def harvest_full_field(entity, size = [0, 0], start_loc = [0, 0], use_fertilizer = False):
	move_to(start_loc)
	max_x = min(get_world_size(), size[0] + start_loc[0])
	max_y = min(get_world_size(), size[1] + start_loc[1])

	for x in range(start_loc[0], max_x):
		for y in range(start_loc[1], max_y):
			if can_harvest():
				if use_fertilizer and num_items(Items.Fertilizer) > 1 and (x+y) % 4 ==0:
					use_item(Items.Fertilizer)
					use_item(Items.Fertilizer)
				harvest()
			plant(entity)

			if get_pos_y() < max_y - 1:
				move_to([x, y+1])
		move_to([min(max_x - 1, x+1), start_loc[1]])

def harvest_and_plant(single_plant_func, size = [0, 0], start_loc = [0, 0]):
	move_to(start_loc)
	max_x = min(get_world_size(), size[0] + start_loc[0])
	max_y = min(get_world_size(), size[1] + start_loc[1])

	if size == [0, 0]:
		size = [get_world_size(), get_world_size()]
	for x in range(start_loc[0], max_x):
		for y in range(start_loc[1], max_y):
			if can_harvest():
				harvest()
			single_plant_func(x, y)
			instant_watering()

			if get_pos_y() < max_y - 1:
				move_to([x, y+1])
		move_to([min(max_x - 1, x+1), start_loc[1]])