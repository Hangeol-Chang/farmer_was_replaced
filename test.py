from Common import move_to
from Initialize import initialize
import E_maze

# harvest()
# initialize()

clear()

repeater = {
	"maze" : {
		"size" : [5, 5],
		"start_loc" : [5, 5],
		"repeat" : 1,
		"plant_func" : E_maze.make_maze,
		# "harvest_func" : E_maze.solve_maze,
		"harvest_func" : E_maze.dormamu_i_came_to_bargain,
	}
}


keys = []
for key in repeater:
	keys.append(key)

while True:
	for i in range(len(keys)):
		key = keys[i]
		val = repeater[key]

		for i in range(val["repeat"]):
			size = val["size"]
			if size == [0, 0]:
				size = [get_world_size(), get_world_size()]

			val["plant_func"](size, val["start_loc"])
			val["harvest_func"](size, val["start_loc"])