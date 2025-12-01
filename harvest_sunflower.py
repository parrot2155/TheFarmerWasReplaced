def harv_sunf():
#해바라기 수확 함수
    # while num_items(Items.Power)<=10000:
    #     for i in range(get_world_size()):
    #         for j in range(get_world_size()):
    #             if can_harvest():
    #                 harvest()
    #             if get_ground_type() != Grounds.Soil:
    #                 till()
    #             plant(Entities.Sunflower)
    #             # if get_water()<=0.75:
    #             #     use_item(Items.Water)
    #             move(North)    
    #         move(East)
    k = 1
    while True:
        if k%2==1:
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
        else:
            max=15
            while max>=7:
                for i in range(get_world_size()):
                    for j in range(get_world_size()):
                        if measure()==max:
                            if can_harvest():
                                harvest()
                        move(North)    
                    move(East)
                max=max-1
        k=k+1
        
        