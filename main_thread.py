# threading main

from Common import move_to
from Initialize import initialize, initialize_multi
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
initialize_multi()

tasks = {
	"sunflower" : {
		"plant_func" : E_sunflower.plant_sunflower,
		"harvest_func" : E_sunflower.harvest_sunflower,
	},
	"grass" : {
		# "plant_func" : E_grass.plant_grass,
		"plant_func" : None,
		"harvest_func" : E_grass.harvest_grass,
	},
	"tree" : {
		# "plant_func" : E_tree.plant_tree,
		"plant_func" : None,
		"harvest_func" : E_tree.harvest_tree,
	},
	"cactus" : {
		# "plant_func" : E_cactus.plant_cactus,
		"plant_func" : None,
		"harvest_func" : E_cactus.harvest_cactus,
	},
	"carrot" : {
		# "plant_func" : E_carrot.plant_carrot,
		"plant_func" : None,
		"harvest_func" : E_carrot.harvest_carrot,
	},
	"pumpkin" : {
		"plant_func" : E_pumpkin.plant_pumpkin,
		"harvest_func" : E_pumpkin.harvest_pumpkin,
	},
	"maze" : {
		"plant_func" : E_maze.make_maze,
		# "harvest_func" : E_maze.solve_maze,
		"harvest_func" : E_maze.dormamu_i_came_to_bargain,
	}
}

threads = {
	"sunflower" : 0,
	"grass" : 3,
	"tree" : 2,
	"cactus" : 2,
	"carrot" : 3,
	"pumpkin" : 2,
	# "maze" : 3
}

spawnd = {
	"sunflower" : 0,
	"grass" : 0,
	"tree" : 0,
	"cactus" : 0,
	"carrot" : 0,
	"pumpkin" : 0,
	# "maze" : 0
}

def drone_thread(tasks, start_loc = [0, 0], size = [8, 8]):
	while True:
		if tasks["plant_func"] != None:
			tasks["plant_func"](size, start_loc)
		tasks["harvest_func"](size, start_loc)

drone_count = 1

spawn_clear_count = 0
while spawn_clear_count < len(threads):
	for key in threads:
		if threads[key] > spawnd[key]:
			start_loc = [drone_count%4 * 8, drone_count//4 * 8]
			drone_count += 1
			spawn_drone(drone_thread, tasks[key], start_loc, [8, 8])
			spawnd[key] += 1

		if spawnd[key] == threads[key]:
			spawn_clear_count += 1


for i in range(3):
	start_loc = [drone_count%4 * 8, drone_count//4 * 8]
	drone_count += 1
	spawn_drone(drone_thread, tasks["maze"], start_loc, [8, 8])

drone_thread(tasks["sunflower"], [0, 0], [8, 8])