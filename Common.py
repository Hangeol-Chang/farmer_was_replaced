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
	max_x = min(get_world_size(), size[0] + start_loc[0]) - start_loc[0]
	max_y = min(get_world_size(), size[1] + start_loc[1]) - start_loc[1]

	for x in range(max_x):
		for y in range(max_y):
			if can_harvest():
				harvest()
			plant(entity)
			instant_watering()
			move_to([start_loc[0] + x, min(start_loc[1] + y + 1, get_world_size() - 1)])
		move_to([min(start_loc[0] + x + 1, get_world_size() - 1), start_loc[1]])

def harvest_full_field(size = [0, 0], start_loc = [0, 0], single_plant_func = None, next_plant_size = [0, 0], next_plant_start_loc = [0, 0], use_fertilizer = False):
	move_to(start_loc)
	max_x = min(get_world_size(), size[0] + start_loc[0]) - start_loc[0]
	max_y = min(get_world_size(), size[1] + start_loc[1]) - start_loc[1]

	for x in range(size[0]):
		for y in range(size[1]):
			if can_harvest():
				if use_fertilizer and num_items(Items.Fertilizer) > 1 and (x+y) % 4 ==0:
					use_item(Items.Fertilizer)
					use_item(Items.Fertilizer)
				harvest()

			if single_plant_func:
				current_x = start_loc[0] + x
				current_y = start_loc[1] + y
				target_x_min = next_plant_start_loc[0]
				target_x_max = next_plant_start_loc[0] + next_plant_size[0]
				target_y_min = next_plant_start_loc[1]
				target_y_max = next_plant_start_loc[1] + next_plant_size[1]
				if  target_x_min <= current_x < target_x_max and target_y_min <= current_y < target_y_max:
					single_plant_func(x, y)

			move_to([start_loc[0] + x, min(start_loc[1] + y + 1, get_world_size() - 1)])
		move_to([min(start_loc[0] + x + 1, get_world_size() - 1), start_loc[1]])

def harvest_and_plant(single_plant_func, size = [0, 0], start_loc = [0, 0]):
	move_to(start_loc)
	max_x = min(get_world_size(), size[0] + start_loc[0]) - start_loc[0]
	max_y = min(get_world_size(), size[1] + start_loc[1]) - start_loc[1]

	if size == [0, 0]:
		size = [get_world_size(), get_world_size()]
	for x in range(size[0]):
		for y in range(size[1]):
			if can_harvest():
				harvest()
			single_plant_func(x, y)
			instant_watering()
			move_to([start_loc[0] + x, min(start_loc[1] + y + 1, get_world_size() - 1)])
		move_to([min(start_loc[0] + x + 1, get_world_size() - 1), start_loc[1]])