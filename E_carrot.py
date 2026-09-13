# carrot
from Common import move_to, plant_full_field, harvest_full_field
	
def plant_carrot(size = [0, 0], start_loc = [0, 0]):
	move_to(start_loc)
	plant_full_field(Entities.Carrot, size, start_loc)

def harvest_carrot(
		size = [0, 0], start_loc = [0, 0], 
		next_plant_func_single = None, 
		next_plant_size = [0, 0], 
		next_plant_start_loc = [0, 0]
	):
	move_to(start_loc)
	harvest_full_field(size, start_loc, next_plant_func_single, next_plant_size, next_plant_start_loc)

def plant_carrot_single(x, y):
	plant(Entities.Carrot)