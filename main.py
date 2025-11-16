while True:
	for i in range(get_world_size()):
		for j in range(get_world_size()):
			if can_harvest():
				harvest()
				if num_items(Items.Wood)<=2:
					if get_ground_type() != Grounds.Grassland:
						till()
			if get_ground_type() == Grounds.Soil:
				plant(Entities.Carrot)
			if get_ground_type() == Grounds.Grassland:
				plant(Entities.Bush)
			move(North)
		move(East)

# clear()
# while True:
# 	for i in range(get_world_size()):
# 		for j in range(get_world_size()):
# 			till()
# 			move(North)
# 		move(East)
 
 
# while True:
# 	for i in range(get_world_size()):
# 		for j in range(get_world_size()):
# 			if get_ground_type() == Grounds.Soil:
# 				till()
# 			if can_harvest():
# 				harvest()
# 				plant(Entities.Bush)
# 			move(North)
# 		move(East)
