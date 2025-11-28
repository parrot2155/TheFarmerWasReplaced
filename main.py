import harvest_log
import harvest_hay
import harvest_carrot
import harvest_pumkin
import harvest_sunflower
import harvest_cactus

while True:

    harvest_hay.harv_hay()
          
    change_hat(Hats.Brown_Hat)
    harvest_log.harv_wood()

    change_hat(Hats.Green_Hat)
    harvest_carrot.harv_carrot()

    change_hat(Hats.Pumpkin_Hat)
    harvest_pumkin.harv_pumpkin()

    change_hat(Hats.Sunflower_Hat)
    harvest_sunflower.harv_sunf()

    change_hat(Hats.Cactus_Hat)
    harvest_cactus.harv_cact()

    unlock(Unlocks.Auto_Unlock)