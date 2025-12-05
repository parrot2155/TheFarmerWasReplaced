def harv_pumpkin():
#호박 수확 함수
    # while num_items(Items.Carrot)>=1000:
    #     for i in range(get_world_size()):
    #         for i in range(get_world_size()):
    #             for j in range(get_world_size()):
    #                 if can_harvest():
    #                     harvest()
    #                 if get_ground_type() != Grounds.Soil:
    #                     till()
    #                 plant(Entities.Pumpkin)
    #                 move(North)    
    #             move(East)
    i=0 #심기 한번 뽑기 한번
    while num_items(Items.Pumpkin)<=200000:
        i=i+1
        if i%2 == 0:
            for j in range(get_world_size()):
                for j in range(get_world_size()):
                    if can_harvest():
                        harvest()
                    if get_ground_type() != Grounds.Soil:
                        till()
                    plant(Entities.Pumpkin)
                    # if get_water()<=0.75:
                    #     use_item(Items.Water)
                    move(North)
                move(East)
        else:
            for j in range(get_world_size()):
                for j in range(get_world_size()):
                    if get_entity_type()==Entities.Dead_Pumpkin:
                        if can_harvest():
                            harvest()
                    if get_ground_type() != Grounds.Soil:
                        till()
                    plant(Entities.Pumpkin)
                    # if get_water()<=0.75:
                    #     use_item(Items.Water)
                    move(North)
                move(East)
    