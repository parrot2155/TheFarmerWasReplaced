def harv_cact():
#선인장 수확 함수
    while num_items(Items.Pumpkin)<=100000:
        for i in range(get_world_size()):
            for j in range(get_world_size()):
                if can_harvest():
                    harvest()
                if get_ground_type() != Grounds.Soil:
                    till()
                plant(Entities.Cactus)
                if get_water()==0.5:
                    use_item(Items.Water)
                move(North)    
            move(East)