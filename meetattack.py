#!/usr/bin/env python
# -*- coding: utf-8 -*-
import s_des

def s_des_meet_attack(p,c,p1,c1): 
    res=[]
    mid_list=[]
    max = 1<<10
    for i in range(max): 
        mid = s_des.encode(p,i)
        mid_list.append(mid)
    for i in range(max): 
        mid = s_des.decode(c,i)
        if mid in mid_list: 
            key = mid_list.index(mid) 
            if s_des.encode(p1,key) == s_des.decode(c1,i):
                res.append([key,i])
    return res

if __name__ == '__main__':
    p=int(input('p: '),2)
    c=int(input('c: '),2)
    p1=int(input('p1: '),2)
    c1=int(input('c1: '),2)
    print(s_des_meet_attack(p,c,p1,c1))
