# -*- coding: utf-8 -*-
"""
Created on Sat Sep 19 10:44:47 2020

@author: user
"""

from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import time

mc.postToChat("i am watching you")

while True:
    
    time.sleep(0.1)
    x,y,z=mc.player.getTilePos()
    mc.postToChat("X:"+ str(x) + "Y:" + str(y) + "Z:" + str(z))
    

x=9487
y=99
z=9487

mc.player.setTilePos(x,y,z)
time.sleep(1)
x=x+1
mc.player.setTilePos(x,y,z)
time.sleep(1)
x=x+1
mc.player.setTilePos(x,y,z)
time.sleep(1)
x=x+1
     

