from Common import *

def plant_grass(size = [0, 0], start_loc = [0, 0]):
	move_to(start_loc)
	plant_full_field(Entities.Grass, size, start_loc)

def harvest_grass(size = [0, 0], start_loc = [0, 0]):
	move_to(start_loc)
	harvest_full_field(Entities.Grass, size, start_loc, True)

def plant_grass_single(x, y):
	plant(Entities.Grass)