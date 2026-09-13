from Common import move_to

def initialize():
	while get_pos_x() > 0:
		move(West)
	while get_pos_y() > 0:
		move(South)
	
	# till all terrain
	for x in range(get_world_size()):
		for y in range(get_world_size()):
			harvest()
			if get_ground_type() == Grounds.Grassland:
				till()
			else:
				pass
			move(North)
		move(East)

def clean_north(col = 2):
	for x in range(col):
		for y in range(get_world_size()):
			harvest()
			if get_ground_type() == Grounds.Grassland:
				till()
			move(North)
		move(East)

clear_col = 3

def initialize_multi():
	move_to()
	for x in range(0, get_world_size(), clear_col):
		spawn_drone(clean_north, clear_col)
		for i in range(clear_col):
			move(East)

	move_to()
	while num_drones() > 1:
		do_a_flip()
	return