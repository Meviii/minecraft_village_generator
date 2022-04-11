from mcpi import minecraft,block
from Environment import environment
from House import house
import time

mc = minecraft.Minecraft.create()

def main():


    # TO DO: x_end, z_end still go past gen_end_x, gen_end_z
    
    env = environment(30, 30, block.GRASS.id)
    hse_one = house(env, "small1")
    hse_two = house(env, "small2")
    hse_three = house(env, "medium1")
    env.add_house(hse_one)
    env.add_house(hse_two)
    env.add_house(hse_three)

    env.env_clear()
    time.sleep(0.5)
    env.create_landscape()
    time.sleep(0.5)
    env.create_houses()
    
    #print(env.test((0,0,0),(5,0,5)))
    #hse.create_small_one((20,0,20), (25,0,25))
    #hse_two.create_small_two((20,0,20), (25,0,25))
    #hse_two.create_medium_one((20,0,20), (25,0,25))
if __name__ == '__main__':
    main()
