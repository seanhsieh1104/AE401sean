# -*- coding: utf-8 -*-
"""
Created on Fri Oct 30 20:52:58 2020

@author: user
"""

from mcpi.minecraft import Minecraft
mc = Minecraft.create()

while True:
    x,y,z = mc.player.getTilePos()
    
    a = mc.getBlock(x-1,y-1,z)
    b = mc.getBlock(x+1,y-1,z)
    c = mc.getBlock(x,y-1,z-1)
    d = mc.getBlock(x,y-1,z+1)
    
    if a == 2 or a == 2 or b == 2 or b == 2 or c == 2 or c == 2 or d == 2 or d == 2:
        a = 0
        mc.setBlock(x,y,z,38,a)
        