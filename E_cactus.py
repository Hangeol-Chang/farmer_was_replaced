# catus
from Common import *

# TODO : make sort algo

def plant_cactus(size = [0, 0], start_loc = [0, 0]):
	move_to(start_loc)
	plant_full_field(Entities.Cactus, size, start_loc)

def harvest_cactus(size = [0, 0], start_loc = [0, 0]):
	move_to(start_loc)
	harvest_full_field(size, start_loc)