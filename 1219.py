# -*- coding: utf-8 -*-
"""
Created on Sat Dec 19 10:05:31 2020

@author: Hsieh
"""

from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import random


for i in range(0,10):
    r = random.randrange(0,16)
    x,y,z = mc.player.getTilePos()
    mc.setBlock(x,y,z,35,r)
    x = x + i
    
    for j in range(0,10):
        r = random.randrange(0,10)
        z = z + 1
        mc.setBlock(x,y,z,35,r)
        

mc.setBlock(x,y,z,0)




r = random.randrange(0,16)
print(r)
while True:
    hits = mc.events.pollBlockHits()
    
    if len(hits) > 0:
        hit = hits[0]
        
        block =  mc.getBlockWithData(hit.pos)
        data = block.data
        
        if data == r:
            mc.postToChat("Congratulation!")
            mc.setBlock(hit.pos,57)
            break
        elif data < r:
            mc.postToChat("Bigger data")
        elif data > r:
            mc.postToChat("smallar data")
            
            
            
from random import randrange
from time import time

def LinearSearch():
    sTime = time()
    r = randrange(0,100000)
    print(r)
    for i in range(100000):
        if r == i:
            print("找到答案了!是" + str(i))
            print("線尋法用了" + str(time() - sTime) + "秒")
            break
LinearSearch()      