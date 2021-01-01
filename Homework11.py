# -*- coding: utf-8 -*-
"""
Created on Fri Jan  1 19:36:01 2021

@author: Hsieh
"""
from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import time
while True:
    chat = mc.events.pollChatPosts()
    
    if len(chat) > 0:
        strChat = str(chat[0])
        length = len(strChat)
        
        
        comma1 = strChat.find(',',0)
        comma2 = strChat.find(',', comma1 + 1)
        
        senderID = int(strChat[comma1 + 1:comma2])
        message = strChat[comma2 +1 +1:length - 1]
        
        playerName = mc.entity.getName(senderID)
        x,y,z = mc.entity.getTilePos(senderID)
        a = a = x
        for o in range(0,100):
            mc.setBlock(x+1,y+3,z,46)
            mc.setBlock(x+2,y+3,z,152)
            time.sleep(0)
            mc.setBlock(x+2,y,z,0)
            x = x + 1
        
        x = x = a
        mc.setSign(x,y,z,63,0,playerName,'',message)
        mc.setSign(x,y+1,z,63,0,"",'hahaha!',)
        time.sleep(0.8)
        mc.postToChat("hahaha!")
        time.sleep(2.5)
        mc.executeCommand('gamemode 0 ' + playerName)
        
        
        mc.exeuteCommand("ban " + playerName)