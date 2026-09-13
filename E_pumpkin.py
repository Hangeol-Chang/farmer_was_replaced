from Common import move_to, plant_full_field, harvest_full_field

def plant_pumpkin(size = [0, 0], start_loc = [0, 0]):
	move_to(start_loc)
	plant_full_field(Entities.Pumpkin, size, start_loc)

def check_growth_pumpkin(size = [0, 0], start_loc = [0, 0], prev_lists = []):
	move_to(start_loc)
	max_x = min(get_world_size(), size[0] + start_loc[0]) - start_loc[0]
	max_y = min(get_world_size(), size[1] + start_loc[1]) - start_loc[1]


	if len(prev_lists) == 0:
		broken_pumpkin_lists = []
		for x in range(max_x):
			for y in range(max_y):
				if get_entity_type() == Entities.Dead_Pumpkin:
					plant(Entities.Pumpkin)
					broken_pumpkin_lists.append((start_loc[0] + x, start_loc[1] + y))
				move_to([start_loc[0] + x, min(start_loc[1] + y + 1, get_world_size() - 1)])
			move_to([min(start_loc[0] + x + 1, get_world_size() - 1), start_loc[1]])
		return broken_pumpkin_lists
	else :
		for x, y in prev_lists:
			broken_pumpkin_lists = []
			move_to([x, y])
			if get_entity_type() == Entities.Dead_Pumpkin:
				plant(Entities.Pumpkin)
				broken_pumpkin_lists.append((x, y))
		return broken_pumpkin_lists

def harvest_pumpkin(size = [0, 0], start_loc = [0, 0], next_plant_func_single = None, next_plant_size = [0, 0], next_plant_start_loc = [0, 0]):
	move_to(start_loc)
	broken_pumpkins = check_growth_pumpkin(size, start_loc)
	while len(broken_pumpkins) > 0:
		broken_pumpkins = check_growth_pumpkin(size, start_loc, broken_pumpkins)
	move_to(start_loc)
	harvest()
	return True

def plant_pumpkin_single(x, y):
	plant(Entities.Pumpkin)