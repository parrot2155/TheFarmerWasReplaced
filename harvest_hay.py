def harv_hay():
#지푸라기 수확 함수
    while num_items(Items.Hay)<=1000000:
        for i in range(get_world_size()):
            for j in range(get_world_size()):
                if can_harvest():
                    harvest()
                if get_ground_type() != Grounds.Grassland:
                    till()             
                move(North)
            move(East)