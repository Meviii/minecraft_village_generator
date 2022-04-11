from mcpi import minecraft, block, vec3
import random
import Environment as environment

mc = minecraft.Minecraft.create()
class house:
    def __init__(self, environment, type, decor = False):
        self.env = environment
        self.decor = decor
        self.cur_houses = []
        
        if type == "small1":
            self.length = 5
            self.width = 5
            self.type = type
            self.cur_houses.append(type)
        elif type == "small2":
            self.length = 4
            self.width = 5
            self.type = type
            self.cur_houses.append(type)
        elif type == "medium1":
            self.length = 7
            self.width = 11
            self.type = type
            self.cur_houses.append(type)
        
    def default(self, o):
        return o.__dict__
    
    def set_decor(self, decor) -> bool:
        self.decor = decor
    
    def set_env(self, env) -> environment:
        self.env = env
    
    def get_house_types(self) -> list:
        return self.cur_houses
    
    def get_type(self):
        return self.type
    
    def get_env(self):
        return self.env
    
    def get_length(self):
        return self.length
    
    def get_width(self):
        return self.width
    
    def create_small_one(self,start_coord, end_coord):
        width = 5
        height = 3
        depth = 5
        x = start_coord[0]
        y = start_coord[1]
        z = start_coord[2]
        
        # Outline and hollow
        mc.setBlocks(x, y, z+3, x+width, y+height, z+3+depth, block.WOOD_PLANKS.id)
        mc.setBlocks(x, y, z+3, x, y+3, z+3, block.WOOD.id)
        mc.setBlocks(x+5, y, z+3, x+5, y+3, z+3, block.WOOD.id)
        mc.setBlocks(x, y, z+8, x, y+3, z+8, block.WOOD.id)
        mc.setBlocks(x+5, y, z+8, x+5, y+3, z+8, block.WOOD.id)
        mc.setBlocks(x+1, y, z+4, x+width-1, y+height-1, z+2+depth, block.AIR.id)
        
        
        # Floor
        mc.setBlocks(x, y-1, z+3, x+width, y-1, z+3+depth, block.COBBLESTONE.id)
        
        # Add a Door.
        #mc.setBlocks(x+1, y, z+3,x+1, y+1, z+3,block.AIR.id)
        #mc.setBlocks(x+1, y, z+3,x+1, y+1, z+3,block.DOOR_WOOD.id)
        #mc.setBlock(x+1, y, z+3, block.DOOR_WOOD.id, 0)
        #mc.setBlock(x+1, y+1, z+3, block.DOOR_WOOD.id, 8)
        mc.setBlock(x+1, y+1, z+3, 0)
        mc.setBlock(x+1, y+0, z+3, 0)
        
        # Add Windows.
        mc.setBlocks(x+3, y+1, z+3, x+4, y+2, z+3, block.GLASS.id)
        mc.setBlocks(x+2, y+1, z+3+depth, x+3, y+2, z+3+depth, block.GLASS.id)
        
        mc.setBlocks(x, y+1, z+5, x, y+2, z+6, block.GLASS.id)
        mc.setBlocks(x+width, y+1, z+5, x+width, y+2, z+6, block.GLASS.id)

        # Bed
        #mc.setBlock(x+4, y, z+6, block.BED.id, 0)
        #mc.setBlock(x+4, y, z+7, block.BED.id, 8)

        # Add a Roof.
        for i in range(int(width/2) + 1):
            mc.setBlocks(x+i, y+height+i, z+3, x+i, y+height+i, z+3+depth, block.STAIRS_WOOD.id, 0)
            mc.setBlocks(x+width-i, y+height+i, z+3, x+width-i, y+height+i, z+3+depth, block.STAIRS_WOOD.id, 1)

            if (int(width/2) - i > 0):
                mc.setBlocks(x+1+i, y+height+i, z+3, x+width-i-1, y+height+i, z+3, block.WOOD_PLANKS.id, 0)
                mc.setBlocks(x+1+i, y+height+i, z+3+depth, x+width-i-1, y+height+i, z+3+depth, block.WOOD_PLANKS.id, 2)
        
        mc.postToChat(f"Small1 house created at {start_coord, end_coord}")
        print("House created")
        
    def create_small_two(self, start_coord, end_coord):
        width = 4
        height = 4
        length = 4
        x = start_coord[0]
        y = start_coord[1]
        z = start_coord[2]
        
        # Outline and hollow
        mc.setBlocks(x, y, z+3, x+width, y+height, z+3+length, block.WOOD_PLANKS.id)
        
        mc.setBlocks(x+1, y, z+4, x+width-1, y+height-1, z+2+length, block.AIR.id)
        
        # Floor
        mc.setBlocks(x, y-1, z+3, x+width, y, z+3+length, block.COBBLESTONE.id)
        
        mc.setBlocks(x, y, z+3, x, y+3, z+3, block.WOOD.id)
        mc.setBlocks(x+4, y, z+3, x+4, y+3, z+3, block.WOOD.id)
        mc.setBlocks(x, y, z+7, x, y+3, z+7, block.WOOD.id)
        mc.setBlocks(x+4, y, z+7, x+4, y+3, z+7, block.WOOD.id)
        
        # Add a Door.
        #mc.setBlocks(x+1, y, z+3,x+1, y+1, z+3,block.AIR.id)
        #mc.setBlocks(x+1, y, z+3,x+1, y+1, z+3,block.DOOR_WOOD.id)
        #mc.setBlock(x+1, y, z+3, block.DOOR_WOOD.id, 0)
        #mc.setBlock(x+1, y+1, z+3, block.DOOR_WOOD.id, 8)
        mc.setBlock(x+2, y+2, z+3, 0)
        mc.setBlock(x+2, y+1, z+3, 0)

        
        # Bed
        #mc.setBlock(x+4, y, z+6, block.BED.id, 0)
        #mc.setBlock(x+4, y, z+7, block.BED.id, 8)

        # Add stairs
        mc.setBlock(x+2, y, z+2, block.STAIRS_COBBLESTONE.id, 2)
        # Decoration
        mc.setBlock(x+3, y, z+2, block.GRASS.id)
        mc.setBlock(x+1, y, z+2, block.GRASS.id)
        mc.setBlock(x+3,y+1,z+2,block.FLOWER_CYAN.id)
        mc.setBlock(x+1,y+1,z+2,block.FLOWER_CYAN.id)
        
        # Add a Roof.
        for i in range(int(width/2) + 1):
            mc.setBlocks(x+i, y+height+i, z+2, x+i, y+height+i, z+4+length, block.STAIRS_WOOD.id, 0)
            mc.setBlocks(x+width-i, y+height+i, z+2, x+width-i, y+height+i, z+4+length, block.STAIRS_WOOD.id, 1)

            if (int(width/2) - i > 0):
                mc.setBlocks(x+1+i, y+height+i, z+3, x+width-i-1, y+height+i, z+3, block.WOOD_PLANKS.id, 2)
                mc.setBlocks(x+1+i, y+height+i, z+3+length, x+width-i-1, y+height+i, z+3+length, block.WOOD_PLANKS.id, 2)
        
        # Fix roof
        mc.setBlocks(x+2, y+6, z+2, x+2, y+6, z+8, block.WOODEN_SLAB.id)
        
        mc.postToChat(f"Small2 house created at {start_coord, end_coord}")
        print("House created")

    def create_medium_one(self, start_coord, end_coord):
        width = 5 # 10 + 5 farm
        height = 4
        length = 6
        x = start_coord[0]
        y = start_coord[1]
        z = start_coord[2]
        
        # Outline and hollow
        mc.setBlocks(x, y, z+3, x+width, y+height, z+3+length, block.WOOD_PLANKS.id)
        
        mc.setBlocks(x+1, y, z+4, x+width-1, y+height-1, z+2+length, block.AIR.id)
        
        # Floor
        mc.setBlocks(x, y-1, z+3, x+width, y, z+3+length, block.COBBLESTONE.id)
        
        mc.setBlocks(x, y, z+3, x, y+3, z+3, block.WOOD.id)
        mc.setBlocks(x+5, y, z+3, x+5, y+3, z+3, block.WOOD.id)
        mc.setBlocks(x, y, z+9, x, y+3, z+9, block.WOOD.id)
        mc.setBlocks(x+5, y, z+9, x+5, y+3, z+9, block.WOOD.id)
        
        # Add a Door.
        #mc.setBlocks(x+1, y, z+3,x+1, y+1, z+3,block.AIR.id)
        #mc.setBlocks(x+1, y, z+3,x+1, y+1, z+3,block.DOOR_WOOD.id)
        #mc.setBlock(x+1, y, z+3, block.DOOR_WOOD.id, 0)
        #mc.setBlock(x+1, y+1, z+3, block.DOOR_WOOD.id, 8)
        mc.setBlock(x+2, y+2, z+3, 0)
        mc.setBlock(x+2, y+1, z+3, 0)
        mc.setBlock(x+3, y+2, z+3, 0)
        mc.setBlock(x+3, y+1, z+3, 0)

        
        # Bed
        #mc.setBlock(x+4, y, z+6, block.BED.id, 0)
        #mc.setBlock(x+4, y, z+7, block.BED.id, 8)

        # Add stairs
        mc.setBlock(x+2, y, z+2, block.STAIRS_COBBLESTONE.id, 2)
        mc.setBlock(x+3, y, z+2, block.STAIRS_COBBLESTONE.id, 2)
        # Decoration
        mc.setBlock(x+4, y, z+2, block.GRASS.id)
        mc.setBlock(x+1, y, z+2, block.GRASS.id)
        mc.setBlock(x+4,y+1,z+2,block.FLOWER_YELLOW.id)
        mc.setBlock(x+1,y+1,z+2,block.FLOWER_YELLOW.id)
        
        # Add a Roof.
        for i in range(int(width/2) + 1):
            mc.setBlocks(x+i, y+height+i, z+2, x+i, y+height+i, z+4+length, block.STAIRS_WOOD.id, 0)
            mc.setBlocks(x+width-i, y+height+i, z+2, x+width-i, y+height+i, z+4+length, block.STAIRS_WOOD.id, 1)

            if (int(width/2) - i > 0):
                mc.setBlocks(x+1+i, y+height+i, z+3, x+width-i-1, y+height+i, z+3, block.WOOD_PLANKS.id, 2)
                mc.setBlocks(x+1+i, y+height+i, z+3+length, x+width-i-1, y+height+i, z+3+length, block.WOOD_PLANKS.id, 2)
        
        # Fix roof
        mc.setBlocks(x+2, y+6, z+2, x+2, y+6, z+10, block.WOODEN_SLAB.id)
        mc.setBlocks(x+3, y+6, z+2, x+3, y+6, z+10, block.WOODEN_SLAB.id)
        
        # Fix bug on roof
        mc.setBlocks(x+3, y+11, z+2, x+3, y+11, z+10, 0)
        
        # Create Farm
        mc.setBlocks(x+3, y+1, z+7, x+6, y+2, z+7, 0) # Door, inner
        mc.setBlocks(x+10, y, z+4, x+6, y, z+8, block.WOOD.id) # farm land
        
        mc.setBlocks(x+10, y+1, z+4, x+6, y+1, z+8, block.FENCE.id) # add fences
        mc.setBlocks(x+9, y+1, z+5, x+6, y+1, z+7, 0) # remove inner fences
        mc.setBlocks(x+9, y, z+5, x+6, y, z+7, block.GRASS.id) # replace inner farm land
        mc.setBlocks(x+8, y+1, z+5, x+7, y+1, z+6, block.MELON.id)
        
        
        mc.postToChat(f"Medium1 house created at {start_coord, end_coord}")
        print("House created")