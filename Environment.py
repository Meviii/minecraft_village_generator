from tracemalloc import start
from mcpi import minecraft, block
import random
from House import house
import time

mc = minecraft.Minecraft.create()

class environment:
    def __init__(self, env_x = 0, env_z = 0, block_type = block.GRASS.id):
        self.env_x = env_x
        self.env_z = env_z
        self.block_type = block_type
        self.houses = []
        self.area = env_x * env_z
        
        self.gen_x_start = 0
        self.gen_z_start = 0
        self.gen_y_start = 0
        
        self.env_y = mc.getHeight(self.gen_x_start, self.gen_z_start)
        
        self.gen_x_end = self.env_x + 0
        self.gen_z_end =  self.env_z + 0
        self.gen_y_end = self.gen_y_start + 0
        
    def default(self, o):
        return o.__dict__
    
    def get_gen_start_coord(self):
        return (self.gen_x_start,self.gen_y_start,self.gen_z_start)
        
    def get_gen_end_coord(self):
        return (self.gen_x_end,self.gen_y_end,self.gen_z_end)
    
    def add_house(self, hse) -> house:
        self.houses.append(hse)
    
    def set_env(self, env_x, env_z):
        self.env_x = env_x
        self.env_z = env_z
    
    def set_block_type(self, block_type):
        self.block_type = block_type
            
    def get_house_list(self):
        ret = []
        for i in self.houses:
            ret.append(i.get_type())
        return ret
    
    def get_house_objects(self):
        return self.houses
    
    def get_env(self):
        return (self.env_x,self.env_y,self.env_z)
    
    def get_block(self):
        return self.block_type
    
    def house_generation(self):
        area = int(self.area / 10)
        final = []
        cur_area = 0
        
        if (self.env_x <= 15 >= self.env_z):
            area = int(self.area / 6)
        
        if self.houses == []:
            print("No houses in env.houses")
            return False
        
        #for i in range(len(self.get_house_objects())):
                
        while cur_area <= area:
            x = random.randint(0,len(self.get_house_objects())-1)
            house_dim = self.houses[x].get_length() * self.houses[x].get_width()
            
            final.append(self.houses[x])
            cur_area += house_dim
                
        return final
    
    def create_houses(self):
        if self.house_generation == []:
            print("house_generation is empty")
            return False
        
        for i in self.house_generation():    
            start_coord = ((self.gen_x_start),(self.gen_y_start),(self.gen_z_start))
            end_coord = (self.gen_x_start+(int(i.get_length() + 2)),self.gen_y_end,self.gen_z_start + (int(i.get_width() + 2)))
            
            if self.plot_check(start_coord, end_coord) != None:
                avail_start, avail_end = self.plot_check(start_coord, end_coord)
                if i.get_type() in i.get_house_types() and i.get_type() == "small1":
                    i.create_small_one(avail_start, avail_end)
                elif i.get_type() in i.get_house_types() and i.get_type() == "small2":
                    i.create_small_two(avail_start, avail_end)
                elif i.get_type() in i.get_house_types() and i.get_type() == "medium1":
                    i.create_medium_one(avail_start, avail_end)
            else:
                continue
        print("Generation Complete")
            
    def plot_check(self, start_coord, end_coord):
        x_start, y_start, z_start = start_coord
        x_end, y_end, z_end = end_coord
        
        gen_end_x,gen_end_y,gen_end_z = self.get_gen_end_coord()
        gen_start_x,gen_start_y,gen_start_z = self.get_gen_start_coord()
        
        rdm_num = self.get_random(gen_start_x,gen_end_x - int((gen_end_x/1.5))) # for random x
        rdm_num_2 = self.get_random(gen_start_z,gen_end_z - int((gen_end_x/1.5))) # for random z

        block_map = list(mc.getBlocks((start_coord),(end_coord)))
        neighbour_map = list(mc.getBlocks((x_start-2, y_start, z_start-2),(x_end+2, y_end, z_end+2)))

        if block_map.count(0) == len(block_map) and neighbour_map.count(0) == len(neighbour_map):
            print(f"Start: {start_coord} : {self.get_gen_start_coord()}")
            print(f"End: {end_coord} : {self.get_gen_end_coord()}")
            
            if (x_end <= gen_end_x) and (z_end <= gen_end_z) and (x_start >= gen_start_x) and (z_start >= gen_start_z):
                print(f"Set at {start_coord, end_coord}")
                return (start_coord, end_coord)
            else:
                return self.plot_check((x_start - rdm_num, y_start, z_start - rdm_num_2), (x_end - rdm_num, y_end, z_end - rdm_num_2))
        else:
            if (x_end > gen_end_x or z_end > gen_end_z) and (x_start > gen_start_x and z_start > gen_start_z): # if both are grater than max land
                if x_end > gen_end_x and z_end <= gen_end_z: # if x is greater but z is not
                    if z_start < gen_start_z: # if z is < gen_start_z but x is not
                        return self.plot_check((x_start - rdm_num, y_start, z_start + rdm_num_2), (x_end - rdm_num, y_end, z_end + rdm_num_2))
                    else:
                        return self.plot_check((x_start - rdm_num, y_start, z_start), (x_end - rdm_num, y_end, z_end))
                elif z_end > gen_end_z and x_end <= gen_end_x:
                    if x_start < gen_start_x:
                        return self.plot_check((x_start + rdm_num, y_start, z_start - rdm_num_2), (x_end + rdm_num, y_end, z_end - rdm_num_2))
                    else:
                        return self.plot_check((x_start, y_start, z_start - rdm_num_2), (x_end, y_end, z_end - rdm_num_2))
                else:
                    print("Test")
                    return None
            elif (x_end <= gen_end_x and z_end <= gen_end_z): # house_end x,z <= land_end x,z
                if (x_end + rdm_num > gen_end_x and z_end + rdm_num_2 > gen_end_z):
                    rdm_num = self.get_random(gen_start_x,gen_end_x - int(gen_end_x/2))
                    rdm_num_2 = self.get_random(gen_start_z,gen_end_z - int(gen_end_x/2))
                    print(rdm_num, rdm_num_2)
                    return self.plot_check((x_start - rdm_num, y_start, z_start - rdm_num_2), (x_end - rdm_num, y_end, z_end - rdm_num_2))
                elif (x_end + rdm_num > gen_end_x and z_end + rdm_num_2 <= gen_end_z):
                    return self.plot_check((x_start - rdm_num, y_start, z_start), (x_end - rdm_num, y_end, z_end))
                elif (x_end + rdm_num <= gen_end_x and z_end + rdm_num_2 > gen_end_z):
                    return self.plot_check((x_start, y_start, z_start - rdm_num_2), (x_end, y_end, z_end - rdm_num_2))
                elif (x_end + rdm_num <= gen_end_x and z_end + rdm_num_2 <= gen_end_z):
                    return self.plot_check((x_start+rdm_num,y_start,z_start+rdm_num_2),(x_end+rdm_num, y_end,z_end+rdm_num_2))
                else:
                    return self.plot_check((x_start-rdm_num,y_start,z_start-rdm_num_2),(x_end-rdm_num, y_end,z_end-rdm_num_2))
            elif (x_end <= gen_end_x and z_end >= gen_end_z): # house_end x <= land_end x, house_end z >= land_end z
                return self.plot_check((x_start,y_start,z_start - rdm_num_2),(x_end, y_end,z_end - rdm_num_2))
            elif (x_end >= gen_end_x and z_end <= gen_end_z): # house_end z <= land_end z, house_end x >= land_end x
                return self.plot_check((x_start - rdm_num,y_start,z_start),(x_end - rdm_num, y_end,z_end))
            else:
                return None
                         
    def create_landscape(self):
        
        mc.postToChat(f"Placed land at {self.get_gen_end_coord()[0], self.get_gen_end_coord()[1],self.get_gen_end_coord()[2]} with size {self.area}")
        mc.setBlocks(0, -1, 0, 0+self.env_x, 0-1, 0+self.env_z, self.block_type)
        
    def env_clear(self):
        
        mc.setBlocks(-200, 0,-200,200,10,200,0)
        mc.setBlocks(-200,-3,-200,200,-1,200,block.STONE_BRICK.id)
    
    def get_random(self, min, max):
        return random.randint(min, max)