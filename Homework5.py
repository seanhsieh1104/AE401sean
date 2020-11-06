# -*- coding: utf-8 -*-
"""
Created on Sat Nov  7 06:23:29 2020

@author: user
"""

from mcpi.minecraft import Minecraft
mc = Minecraft.create()
 
x,y,z = mc.player.getTilePos()
try:
    b = int(input("do you want to build a house?if you don't want to build a house please press the red square"))
except:
    print(';-;')
    mc.postToChat(';-;')
    exit()
try:
    a = int(input('enter blockID'))
    mc.setBlock(x,y,z,a)
except:
    print("error!!!")
    mc.postToChat("error!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")

   
h = int(input('enter x'))
o = int(input('enter y'))
w = int(input('enter z'))
    
mc.setBlocks(x,y,z,x+h,y+o,z+w,20)
mc.setBlocks(x+1,y+1,z+1,x+h-1,y+o-1,z+w+-1,0)