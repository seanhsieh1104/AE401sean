# -*- coding: utf-8 -*-
"""9 2020

@author: Hsieh
"""
from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import time

x,y,z = mc.player.getTilePos()
for i in range(0,5):
    mc.spawnEntity(x,y,z,93)
    time.sleep(0.1)