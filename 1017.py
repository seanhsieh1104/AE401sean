# -*- coding: utf-8 -*-
"""
Created on Sat Oct 17 10:36:53 2020

@author: user
"""

from mcpi.minecraft import Minecraft
mc = Minecraft.create()



x,y,z = mc.player.getTilePos()
mc.setBlock(x,y-1,z,152)
mc.setBlock(x,y,z,46)
mc.setBlock(x,y+1,z,152)
mc.setBlock(x,y+2,z,46)
mc.setBlock(x,y+3,z,152)
mc.setBlock(x,y+4,z,46)
mc.setBlock(x,y+5,z,152)
mc.setBlock(x,y+6,z,46)
mc.setBlock(x,y+7,z,152)
mc.setBlock(x,y+8,z,46)
mc.setBlock(x,y+9,z,152)
mc.setBlock(x,y+10,z,46)
mc.setBlock(x,y+11,z,152)
mc.setBlock(x,y+12,z,46)
mc.setBlock(x,y+13,z,152)



from mcpi.minecraft import Minecraft
mc = Minecraft.create()

x,y,z = mc.player.getTilePos()
mc.setBlock(x-1,y,z,152)
mc.setBlock(x+1,y,z,152)
mc.setBlock(x,y,z-1,152)
mc.setBlock(x,y,z+1,152)
mc.setBlock(x-1,y,z-1,152)
mc.setBlock(x+1,y,z-1,152)
mc.setBlock(x-1,y,z+1,152)
mc.setBlock(x+1,y,z+1,152)

from mcpi.minecraft import Minecraft
mc = Minecraft.create()

x,y,z = mc.player.getTilePos()
mc.setBlocks(x+30,y+30,z+30,x-30,y-30,z-30,416)

