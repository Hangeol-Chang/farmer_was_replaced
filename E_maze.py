# maze2
from Common import *

def make_maze(size = [0, 0], start_loc = [0, 0]):
	move_to([start_loc[0] + size[0]/2, start_loc[1] + size[1]/2])
	plant(Entities.Bush)
	substance = size[0] * 2**(num_unlocked(Unlocks.Mazes) - 1)
	substance = min(num_items(Items.Weird_Substance), substance)
	use_item(Items.Weird_Substance, substance)
	

dirs = [North, East, South, West]

def loop(x, y, target_x, target_y, visited):
	if x == target_x and y == target_y:
		return [x, y]

	if (x, y) in visited:
		return [-1, -1]
	visited.add((x, y))
	
	for i in range(len(dirs)):
		if can_move(dirs[i]):
			move(dirs[i])
			if loop(get_pos_x(), get_pos_y(), target_x, target_y, visited) != [-1, -1]:
				return [x, y]
			move(dirs[(i+2)% 4]) 
	return [-1, -1]

def after_maze(size = [0, 0], start_loc = [0, 0]):
	move_to(start_loc)
	max_x = min(get_world_size(), size[0] + start_loc[0])
	max_y = min(get_world_size(), size[1] + start_loc[1])

	for x in range(start_loc[0], max_x):
		for y in range(start_loc[1], max_y):
			harvest()
			till()
			if get_pos_y() < max_y - 1:
				move_to([x, y+1])
		move_to([min(max_x - 1, x+1), start_loc[1]])

def solve_maze(size = [0, 0], start_loc = [0, 0]):
	# move_to(start_loc)
	target_x, target_y = measure()
	visited = set()    
	loop(get_pos_x(), get_pos_y(), target_x, target_y, visited)
	harvest()

	after_maze(size, start_loc)

# reuse maze
def dormamu_i_came_to_bargain(size = [0, 0], start_loc = [0, 0]):
	# move_to(start_loc)
	loop_count = 0
	while loop_count < 299:

		target_x, target_y = measure()
		loop_count += 1
		visited = set()
		loop(get_pos_x(), get_pos_y(), target_x, target_y, visited)

		substance = size[0] * 2**(num_unlocked(Unlocks.Mazes) - 1)
		substance = min(num_items(Items.Weird_Substance), substance)
		use_item(Items.Weird_Substance, substance)

	after_maze(size, start_loc)