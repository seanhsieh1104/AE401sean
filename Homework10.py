# -*- coding: utf-8 -*-
"""
Created on Sat Dec 12 11:34:32 2020

@author: Hsieh
"""

from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import time
import random
x,y,z = mc.player.getTilePos()

for i in range(50):
    r = random.randrange(1,5)
    b = random.randrange(1,4)
    c = random.randrange(1,2)
    d = random.randrange(1,500)
    color = random.randint(1,16)
    mc.setBlocks(x,y-2,z,x+10,y-2,z-10,166)

    if r == 1:
        mc.setBlocks(x,y,z,x+b,y,z,d,color)
        mc.setBlocks(x,y,z,x+b,y+1,z,1,color)
        z = z + c  
        x = x - c
    elif r == 2:
        mc.setBlocks(x,y-1,z,x,y,z+b,d,color)
        mc.setBlocks(x,y-1,z,x-b,y-1,z,1,color)
        z = z - c
        x = x + c
    elif r == 3:
        mc.setBlocks(x,y-1,z,x-b,y,z,d,color)
        mc.setBlocks(x,y-1,z,x,y-1,z-b,d,color)
        x = x - c
        z = z + c
    elif r == 4:
        mc.setBlocks(x,y-1,z,x,y,z-b,d,color)
        mc.setBlocks(x,y-1,z,x,y-1,z+b,d,color)