from mcpi import minecraft, block, vec3
import random
from House import house

mc = minecraft.Minecraft.create()

class environment:
    def __init__(self, env_x = 0, env_z = 0, block_type = block.GRASS.id):
        self.env_x = env_x
        self.env_z = env_z
        self.block_type = block_type
        self.gen_x1 = random.randint(-5000,5000)
        self.gen_z1 = random.randint(-5000,5000)
        self.gen_x2 = self.gen_x1 + env_x
        self.gen_z2 = self.gen_z1 + env_z
        self.houses = []
        self.area = env_x * env_z
        self.reachable_area = []
        
    def default(self, o):
        return o.__dict__
    
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
    
    def get_env(self):
        return (self.env_x,self.env_z)
    
    def get_block(self):
        return self.block_type
    
    def get_gen_x1(self):
        return self.gen_x1
    
    def get_gen_x2(self):
        return self.gen_x2
    
    def get_gen_z1(self):
        return self.gen_z1
    
    def get_gen_z2(self):
        return self.gen_z2
            
    def check_area(self) -> bool:
        area = 0
        for i in self.houses:
            if i.get_type() == "small":
                length = i.get_length()
                width = i.get_width()
                area += length*width
        if area <= self.area:
            return True
        else:
            return False
    
    def emtpy_coords(self,length, width):
        reachable_area = []
        l = 0
        w = 0
        i = 0
        while i <= length and i <= width:
            if len(reachable_area) == (length*width):
                break
            
            if mc.getBlock(0+l, 0, 0+w) == block.AIR.id:
                reachable_area.append((0+l,0,0+w))
                
            i += 1
            l += 1
            w += 1
        for i in reachable_area:
            print(i)
            
    def assign_area(self,length, width, l=0, w=0) -> list:

        if len(self.reachable_area) == (length*width):
            return self.reachable_area
        
        if mc.getBlock(0+l, 0, 0+w) == block.AIR.id:
            self.reachable_area.append((0+l,0,0+w))
        elif mc.getBlock(0+l, 0, 0+w) != block.AIR.id:
            mc.postToChat(f"Trying again with position {0+l,0,0+w}")
            self.assign_area((length+length), (width+width), l+1, w+1)
        
    def create_landscape(self):
        #mc.setBlocks(self.gen_x1, 24, self.gen_z1,self.gen_x2, 24, self.gen_z2, self.block_type)
        #mc.postToChat(f"Blocks set at x: {self.gen_x1} y: {self.gen_z1}")
        #mc.player.setPos(self.gen_x1, 24, self.gen_z1)
        if self.check_area() == True:
            mc.postToChat(f"Placed land at 0,0,0 with size {self.area}")
            mc.setBlocks(0, 0-1, 0, 0+self.env_x, 0-1, 0+self.env_z, self.block_type)
            
            for i in self.houses:
                cur_house = house(self.get_env(), i.get_type())
                start = self.assign_area(cur_house.get_length(), cur_house.get_width())[0]
                end = self.assign_area(cur_house.get_length(), cur_house.get_width())[-1]
                cur_house.create(start, end)
        else:
            mc.postToChat("Area not suitable")
        
    def env_clear(self):
        mc.setBlocks(-20, 0,-20,20,10,20,0)
        mc.setBlocks(-20,-3,-20,20,-1,20,2)