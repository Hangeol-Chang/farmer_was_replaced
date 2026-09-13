# water
import Common

E_WATER_THREADHOLD = 0.8

def watering(size = [0, 0], start_loc = [0, 0]):
	Common.move_to()

	for x in range(size[0]):
		for y in range(size[1]):
			if num_items(Items.Water) > 0:
				if get_water() < E_WATER_THREADHOLD:
					use_item(Items.Water)
			else :
				return False
			move(North)
		move(East)