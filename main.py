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
	"grass" : {
		"size" : [0, 0],
		"start_loc" : [0, 0],
		"repeat" : 1,
		"plant_func" : E_grass.plant_grass,
		"harvest_func" : E_grass.harvest_grass,
		"plant_func_single" : E_grass.plant_grass_single,
	},
	"sunflower" : {
		"size" : [5, 5],
		"start_loc" : [0, 0],
		"repeat" : 1,
		"plant_func" : E_sunflower.plant_sunflower,
		"harvest_func" : E_sunflower.harvest_sunflower,
		"plant_func_single" : E_sunflower.plant_sunflower_single,
	},
	"tree" : {
		"size" : [0, 0],
		"start_loc" : [0, 0],
		"repeat" : 1,
		"plant_func" : E_tree.plant_tree,
		"harvest_func" : E_tree.harvest_tree,
		"plant_func_single" : E_tree.plant_tree_single,
	},
	"carrot" : {
		"size" : [0, 0],
		"start_loc" : [0, 0],
		"repeat" : 1,
		"plant_func" : E_carrot.plant_carrot,
		"harvest_func" : E_carrot.harvest_carrot,
		"plant_func_single" : E_carrot.plant_carrot_single,
	},
	"pumpkin" : {
		"size" : [0, 0],
		"start_loc" : [0, 0],
		"repeat" : 1,
		"plant_func" : E_pumpkin.plant_pumpkin,
		"harvest_func" : E_pumpkin.harvest_pumpkin,
		"plant_func_single" : E_pumpkin.plant_pumpkin_single,
	}
}


keys = []
for key in repeater:
	keys.append(key)

while True:
	for i in range(len(keys)):
		key = keys[i]
		val = repeater[key]

		for j in range(val["repeat"]):
			size = val["size"]
			if size == [0, 0]:
				size = [get_world_size(), get_world_size()]

			
			next_val = repeater[keys[(i+1)%len(keys)]]
			next_size = next_val["size"]
			if next_size == [0, 0]:
				next_size = size			
			if next_val["plant_func_single"]:
				val["harvest_func"](size, val["start_loc"], next_val["plant_func_single"], next_size, next_val["start_loc"])
			else:
				val["harvest_func"](size, val["start_loc"])
				next_val["plant_func"](size, next_val["start_loc"])