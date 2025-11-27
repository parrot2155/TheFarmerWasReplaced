import harvest_log
import harvest_hay

while True:
	if num_items(Items.Hay)<=1000:
		harvest_hay.harv_hay()
          
	if num_items(Items.Wood)<=500:
		change_hat(Hats.Brown_Hat)
		while num_items(Items.Wood)<=500:
			harvest_log.harv_wood()

	while num_items(Items.Wood)>=500:
		change_hat(Hats.Green_Hat)
		for i in range(get_world_size()):
			for j in range(get_world_size()):
				if can_harvest():
					harvest()
				if get_ground_type() != Grounds.Soil:
					till()
				plant(Entities.Carrot)
				move(North)    
			move(East)
 

# while True:
#     for i in range(get_world_size()):
#         for j in range(get_world_size()):
#             if get_ground_type() == Grounds.Soil:
#                 till()
#             if can_harvest():
#                 harvest()
#                 plant(Entities.Bush)
#             move(North)
#         move(East)

# clear() #나무 수확 함수
# while True:
#     for i in range(get_world_size()):
#         for j in range(get_world_size()):
#             if can_harvest():
#                 harvest()
#             if num_items(Items.Wood)<=2:
#                 if get_ground_type() != Grounds.Grassland:
#                     till()
#             if get_ground_type() == Grounds.Soil:
#                 plant(Entities.Carrot)
#             if get_ground_type() == Grounds.Grassland:
#                 plant(Entities.Tree)
#             move(North)
#         move(East)
