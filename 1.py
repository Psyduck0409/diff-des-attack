#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
import random
import little_des

p_list = [[0x375BD31F6ACDFF31,0x486911026ACDFF31],[0x357418DA013FEC86,0x12549847013FEC86],[0x748502CD38451097,0x3874756438451097],[0x02152633A124F6B6,0x52873E68A124F6B6],[0x52873E68A124F6B6,0x19C26156A124F6B6],[0x19C26156A124F6B6,0xDF2D047AA124F6B6],[0xDF2D047AA124F6B6,0x52873E68A124F6B6],[0xDF2D047AA124F6B6,0x02152633A124F6B6]]
key = 0xd0f88842226d2c
print('[',end='')
for i in p_list: 
    print('[',end='')
    print(hex(little_des.encode(i[0],key,56)),end='')
    print(',',end='')
    print(hex(little_des.encode(i[1],key,56)),end='')
    print(']',end='')
    print(',',end='')
print(']',end='')
