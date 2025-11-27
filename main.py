import harvest_log
import harvest_hay
import harvest_carrot

while True:
    if num_items(Items.Hay)<=1000:
        harvest_hay.harv_hay()
          
    change_hat(Hats.Brown_Hat)
    harvest_log.harv_wood()

    change_hat(Hats.Green_Hat)
    harvest_carrot.harv_carrot()
