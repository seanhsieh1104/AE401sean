# -*- coding: utf-8 -*-
"""
Created on Sat Oct 24 10:46:43 2020

@author: user
"""

from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import time
 
while True:
    x,y,z = mc.player.getTilePos()
    
    a = mc.getBlock(x-1,y-1,z)
    b = mc.getBlock(x+1,y-1,z)
    c = mc.getBlock(x,y-1,z-1)
    d = mc.getBlock(x,y-1,z+1)
    
    if a == 8 or a == 0 or b == 8 or b == 0 or c == 8 or c == 0 or d == 8 or d == 0:
        mc.setBlocks(x+1,y-1,z+1,x-1,y-1,z-1,166)
        
while True:
    x,y,z = mc.player.getTilePos()
    mc.setBlock(x,y,z,368)
    time.sleep(0.2)
    
    
a = 0
x,y,z = mc.player.getTilePos()
while a < 87:
    mc.setBlocks(x+10,y-1,z,x-10,y-10,z,0)
    z=z+1
    a=a+1
    time.sleep(1)
    
    
    
while True:
    x,y,z = mc.player.getTilePos()
    mc.setBlock(x,y+5,z,19)
    mc.setBlock(x,y+6,z,8)
    time.sleep(2)