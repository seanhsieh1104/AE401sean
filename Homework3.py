# -*- coding: utf-8 -*-
"""
Created on Sat Oct 17 21:21:26 2020

@author: user
"""
from mcpi.minecraft import Minecraft
mc = Minecraft.create()

x,y,z = mc.player.getTilePos()
mc.setBlocks(x+30,y+30,z+30,x-30,y-30,z-30,20)
mc.setBlocks(x+29,y+29,z+29,x-29,y-29,z-29,0)