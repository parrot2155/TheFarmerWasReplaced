def harv_sunf():
#해바라기 수확 함수
    while num_items(Items.Power)<=100000:
        for i in range(get_world_size()):
            for j in range(get_world_size()):
                if can_harvest():
                    harvest()
                if get_ground_type() != Grounds.Soil:
                    till()
                plant(Entities.Sunflower)
                # if get_water()<=0.75:
                #     use_item(Items.Water)
                move(North)    
            move(East)