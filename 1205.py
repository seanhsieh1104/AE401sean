# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.

"""
from mcpi.minecraft import Minecraft
mc = Minecraft.create()

def buildPyramid(x,y,z,base):
    height = (base//2) + 1
    
    for i in range(height):
        x1 = x + i
        y1 = y + i
        z1 = z + i
        
        x2 = x + base - i
        z2 = z + base - i
        
        mc.setBlocks(x1,y1,z1,x2,y,z2,46)
        mc.setBlocks(x-2,y,z,152)
        
x,y,z = mc.player.getTilePos()
base = int(input("enter base"))
buildPyramid(x, y, z,base)


line1 = []
line2 = []
line3 = []

x,y,z = mc.player.getTilePos()

for i in range(1,4):
    line1.append(1*i)
for i in range(1,4):
    line2.append(2*i)
for i in range(1,4):
    line3.append(3*i)

mc.setSign(x,y,z,63,0,[str(line1),str(line2),str(line3)])
mc.setBlock(x+1,y,z,46)
mc.setBlock(x+2,y,z,77)



x,y,z = mc.player.getTilePos()
number = 1
for i in range(8):
    for j in range(number):
        mc.spawnEntity(x,y,z,200)
        
    number = number * 2
        
    mc.postToChat("已生成" + str(number) + "隻")