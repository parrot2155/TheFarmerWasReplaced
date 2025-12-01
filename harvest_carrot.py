def harv_carrot():
#당근 수확 함수
    while num_items(Items.Carrot)<=100000 or num_items(Items.Wood)<=10000:
        for i in range(get_world_size()):
            for j in range(get_world_size()):
                if can_harvest():
                    harvest()
                if get_ground_type() != Grounds.Soil:
                    till()
                plant(Entities.Carrot)
                # if get_water()<=0.75:
                #     use_item(Items.Water)
                move(North)    
            move(East)