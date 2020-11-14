# -*- coding: utf-8 -*-
"""
Created on Sat Nov 14 10:21:55 2020

@author: user
"""

from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import time
import random
while True:
    hits = mc.events.pollBlockHits()
    
    if len(hits) > 0:
        hit = hits[0]
        x,y,z = hit.pos.x, hit.pos.y, hit.pos.z
        block = mc.getBlock(x,y,z)
        if block == 1:
                mc.setBlock(x,y,z,46)
                mc.setBlock(x+1,y,z,76)


x,y,z = mc.player.getTilePos()
mc.setSign(x,y,z,63,0,'h','i',':)',';-;')
    
i = 0   
while i < 10:
    pos = mc.player.getPos()
    i = i + 1
    x = pos.x + random.uniform(-20,20)
    y = pos.y + random.uniform(3,0)
    z = pos.z + random.uniform(-20,20)
    
    mc.spawnEntity(x,y,z,20)
    time.sleep(0.2)
    
