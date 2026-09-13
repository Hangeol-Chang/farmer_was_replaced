from Common import move_to
import E_carrot
import E_pumpkin
from Initialize import initialize
import E_sunflower
import E_grass
import E_tree
import E_water

# initialize()

repeater = {
	"pumpkin" : {
		"size" : [6, 6],
		"start_loc" : [0, 0],
		"repeat" : 1,
		"plant_func" : E_pumpkin.plant_pumpkin,
		"harvest_func" : E_pumpkin.harvest_pumpkin,
		"plant_func_single" : None,
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
				
			# harvesting
			next_val = repeater[keys[(i+1)%len(keys)]]
			if next_val["plant_func_single"]:
				val["harvest_func"](size, val["start_loc"], next_val["plant_func_single"])
			else:
				val["harvest_func"](size, val["start_loc"])
				next_val["plant_func"](size, next_val["start_loc"])