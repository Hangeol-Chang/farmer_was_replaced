def return_to_origin():
	while get_pos_x() > 0:
		move(West)
	while get_pos_y() > 0:
		move(South)

def initialize():
	while get_pos_x() > 0:
		move(West)
	while get_pos_y() > 0:
		move(South)
	
	# till all terrain
	for x in range(get_world_size()):
		for y in range(get_world_size()):
			if get_ground_type() == Grounds.Grassland:
				till()
			else:
				pass
			move(North)
		move(East)
		