def harv_wood():
#나무 수확 함수
    while num_items(Items.Wood)<=500:
        for i in range(get_world_size()):
            for j in range(get_world_size()):
                if can_harvest():
                    harvest()
                if get_ground_type() != Grounds.Grassland:
                    till()
                plant(Entities.Bush)             
                move(North)
            move(East)
    

# for i in range(get_world_size()):
#     for j in range(get_world_size()):
#         if can_harvest():
#             harvest()
#         if get_ground_type() != Grounds.Grassland:
#             till()
#         plant(Entities.Bush)
#         move(North)
        