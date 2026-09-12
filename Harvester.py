import Flower

def run():
	for x in range(get_world_size()):
		for y in range(get_world_size()):
			if get_entity_type() == Entities.Sunflower :
				if Flower.is_flower_ground(get_pos_x(), get_pos_y()):
					pass
				else:
					harvest()
					
			else:
				pass