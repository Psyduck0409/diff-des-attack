#!/usr/bin/env python
# -*- coding: utf-8 -*-
import des

def encode(p,key):
    key1=key>>64
    key2=key-(key1<<64)
    return des.encode(des.decode(des.encode(p,key1),key2),key1)

def decode(p,key): 
    key1=key>>64
    key2=key-(key1<<64)
    return des.decode(des.encode(des.decode(p,key1),key2),key1)

if __name__ == '__main__': 
    while 1:
        chos = input('1: encode, 0: decode -> ')
        if chos == '1': 
            a,k = input('p ,k -> ').split()
            a,k = int(a,16),int(k,16)
            print(hex(encode(a,k)))
        else: 
            a,k = input('c ,k -> ').split()
            a,k = int(a,16),int(k,16)
            print(hex(decode(a,k)))
