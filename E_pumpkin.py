from Common import move_to, plant_full_field, harvest_full_field

def plant_pumpkin(size = [0, 0], start_loc = [0, 0]):
	move_to(start_loc)
	plant_full_field(Entities.Pumpkin, size, start_loc)

def check_growth_pumpkin(size = [0, 0], start_loc = [0, 0], prev_lists = []):
	move_to(start_loc)
	max_x = min(get_world_size(), size[0] + start_loc[0])
	max_y = min(get_world_size(), size[1] + start_loc[1])

	if len(prev_lists) == 0:
		broken_pumpkin_lists = []
		for x in range(start_loc[0], max_x):
			for y in range(start_loc[1], max_y):
				if get_entity_type() == Entities.Dead_Pumpkin:
					plant(Entities.Pumpkin)
					broken_pumpkin_lists.append((x, y))

				if get_pos_y() < max_y - 1:
					move_to([x, y+1])
			move_to([min(max_x - 1, x+1), start_loc[1]])
		return broken_pumpkin_lists

	else :
		broken_pumpkin_lists = []
		for x, y in prev_lists:
			move_to([x, y])
			if get_entity_type() == Entities.Dead_Pumpkin:
				plant(Entities.Pumpkin)
				broken_pumpkin_lists.append((x, y))
		return broken_pumpkin_lists

def harvest_pumpkin(size = [0, 0], start_loc = [0, 0]):
	move_to(start_loc)
	broken_pumpkins = check_growth_pumpkin(size, start_loc)
	while len(broken_pumpkins) > 0:
		broken_pumpkins = check_growth_pumpkin(size, start_loc, broken_pumpkins)
	move_to(start_loc)
	harvest()
	return True

def plant_pumpkin_single(x, y):
	plant(Entities.Pumpkin)