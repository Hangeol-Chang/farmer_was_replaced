import Initialize
import Flower
import Common

Initialize.initialize()
Flower.create_sunflower_farm()
for i in range(3): # get power at first
	Flower.harvest_all_sunflower()
Common.move_to()
# pet_the_piggy()

# =================
cycle_count = 0

grass_y = [0, 1, 2, 3, 4, 5]
carrot_y = [5, 6, 7, 8]
catus_y = [9, 10, 11]

while True:
	for x in range(get_world_size()):
		for y in range(get_world_size()):
			if get_entity_type() == Entities.Sunflower :
				if Flower.is_flower_ground(get_pos_x(), get_pos_y()):
					pass
				else:
					harvest()
				
			else:
				if can_harvest():
					harvest()

				if x >= 2 and x <= 6 and y >= 0 and y <= 4:
					plant(Entities.Pumpkin)

				elif (x+y)%3 == 0:
					plant(Entities.Tree)

				elif y in grass_y:
					plant(Entities.Grass)
					# if num_items(Items.Fertilizer) > 10:
					# 	use_item(Items.Fertilizer)
				elif y in carrot_y:
					plant(Entities.Carrot)
					if num_items(Items.Fertilizer) > 10:
						use_item(Items.Fertilizer)

				elif y in catus_y:
					plant(Entities.Cactus)
					# if num_items(Items.Fertilizer) > 10:
					# 	use_item(Items.Fertilizer)

				# elif y in pumpkin_y:
				# 	plant(Entities.Pumpkin)
			
				while get_water() <= 0.7 and num_items(Items.Water) > 0:
					use_item(Items.Water)
					
			move(North)
		move(East)
	
	# earn sunflower at 5 cycle
	cycle_count += 1
	if cycle_count >= 3:
		cycle_count = 0
		Flower.harvest_all_sunflower()

	# return to origin
	Common.move_to()