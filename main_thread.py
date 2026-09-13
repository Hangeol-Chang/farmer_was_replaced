# threading main

from Common import move_to
from Initialize import initialize
import E_carrot
import E_pumpkin
import E_sunflower
import E_grass
import E_tree
import E_water
import E_maze
import E_cactus

clear()
harvest()
initialize()

tasks_1 = {
	"sunflower" : {
		"size" : [6, 6],
		"start_loc" : [0, 0],
		"repeat" : 6,
		"plant_func" : E_sunflower.plant_sunflower,
		"harvest_func" : E_sunflower.harvest_sunflower,
	},
	"grass" : {
		"size" : [11, 11],
		"start_loc" : [0, 0],
		"repeat" : 1,
		"plant_func" : E_grass.plant_grass,
		"harvest_func" : E_grass.harvest_grass,
	},
	"tree" : {
		"size" : [11, 11],
		"start_loc" : [0, 0],
		"repeat" : 1,
		"plant_func" : E_tree.plant_tree,
		"harvest_func" : E_tree.harvest_tree,
	}
}

tasks_2 = {
    "carrot" : {
		"size" : [11, 11],
		"start_loc" : [11, 0],
		"repeat" : 3,
		"plant_func" : E_carrot.plant_carrot,
		"harvest_func" : E_carrot.harvest_carrot,
	},
    "pumpkin" : {
		"size" : [11, 11],
		"start_loc" : [11, 0],
		"repeat" : 1,
		"plant_func" : E_pumpkin.plant_pumpkin,
		"harvest_func" : E_pumpkin.harvest_pumpkin,
	},
    "cactus" : {
		"size" : [11, 11],
		"start_loc" : [11, 0],
		"repeat" : 1,
		"plant_func" : E_cactus.plant_cactus,
		"harvest_func" : E_cactus.harvest_cactus,
	},
}

tasks_3 = {
	"pumpkin" : {
		"size" : [11, 11],
		"start_loc" : [0, 11],
		"repeat" : 1,
		"plant_func" : E_pumpkin.plant_pumpkin,
		"harvest_func" : E_pumpkin.harvest_pumpkin,
	},
}

tasks_4 = {
	"maze" : {
		"size" : [11, 11],
		"start_loc" : [11, 11],
		"repeat" : 1,
		"plant_func" : E_maze.make_maze,
		"harvest_func" : E_maze.solve_maze,
	}
}

def drone_thread(tasks):
	keys = []
	for key in tasks:
		keys.append(key)

	while True:
		for i in range(len(keys)):
			key = keys[i]
			val = tasks[key]

			for j in range(val["repeat"]):
				size = val["size"]
				if size == [0, 0]:
					size = [get_world_size(), get_world_size()]

				val["plant_func"](size, val["start_loc"])
				val["harvest_func"](size, val["start_loc"])


def drone1_thread():
	drone_thread(tasks_1)
	pass

def drone2_thread():
	drone_thread(tasks_2)
	pass

def drone3_thread():
    drone_thread(tasks_3)
    pass

def drone4_thread():
    drone_thread(tasks_4)
    pass

spawn_drone(drone2_thread)
spawn_drone(drone3_thread)
spawn_drone(drone4_thread)
drone1_thread()