from Common import *

def plant_grass(size = [0, 0], start_loc = [0, 0]):
	move_to()
	plant_full_field(Entities.Grass, size, start_loc)

def harvest_grass(size = [0, 0], start_loc = [0, 0], next_plant_func_single = None, next_plant_size = [0, 0], next_plant_start_loc = [0, 0]):
	move_to()
	harvest_full_field(size, start_loc, next_plant_func_single, next_plant_size, next_plant_start_loc, True)

def plant_grass_single(x, y):
	plant(Entities.Grass)