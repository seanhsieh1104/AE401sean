# -*- coding: utf-8 -*-
"""
Created on Sat Oct 31 10:29:14 2020

@author: user
"""

from mcpi.minecraft import Minecraft
mc = Minecraft.create()
 
x,y,z = mc.player.getTilePos()
try:
    a = int(input('enter blockID'))
    mc.setBlock(x,y,z,a)
except:
    print("error!!!")
    mc.postToChat("error!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    
    
    
x,y,z = mc.player.getTilePos()
   
h = int(input('enter x'))
o = int(input('enter y'))
w = int(input('enter z'))
    
mc.setBlocks(x,y,z,x+h,y+o,z+w,20)
mc.setBlocks(x+1,y+1,z+1,x+h-1,y+o-1,z+w+-1,0)
