# -*- coding: utf-8 -*-
"""
Created on Fri Dec 11 19:27:30 2020

@author: Hsieh
"""
from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import time
import random

while True:    
    x,y,z = mc.player.getTilePos()
    
    a = mc.getBlock(x-1,y-1,z)
    b = mc.getBlock(x+1,y-1,z)
    c = mc.getBlock(x,y-1,z-1)
    d = mc.getBlock(x,y-1,z+1)
    
    if a == 8 or a == 9 or b == 8 or b == 9 or c == 8 or c == 9 or d == 8 or d == 9:
        mc.setBlocks(x+1,y-1,z+1,x-1,y-1,z-1,166)
    hits = mc.events.pollBlockHits()
    
    if len(hits) > 0:
        hit = hits[0]
        x,y,z = hit.pos.x, hit.pos.y, hit.pos.z
        block = mc.getBlock(x,y,z)
        if block == 324:
                mc.setBlock(x,y,z,38)

    
    
    a = mc.getBlock(x-1,y-1,z)
    b = mc.getBlock(x+1,y-1,z)
    c = mc.getBlock(x,y-1,z-1)
    d = mc.getBlock(x,y-1,z+1)
    
    if a == 8 or a == 9 or b == 8 or b == 9 or c == 8 or c == 9 or d == 8 or d == 9:
        mc.setBlocks(x+1,y-1,z+1,x-1,y-1,z-1,166)
        
        