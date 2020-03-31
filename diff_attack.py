#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

def diff_attack(p1,c1,p2,c2,bool_exc): 
    #init
    p1_str = "{:0>64b}".format(p1)
    p2_str = "{:0>64b}".format(p2)
    c1_str = "{:0>64b}".format(c1)
    c2_str = "{:0>64b}".format(c2)
    l0 = int(p1_str[0:32],2)
    r0 = int(p1_str[32:64],2)
    l3 = int(c1_str[0:32],2)
    r3 = int(c1_str[32:64],2)

    l0_ = int(p2_str[0:32],2)
    r0_ = int(p2_str[32:64],2)
    l3_ = int(c2_str[0:32],2)
    r3_ = int(c2_str[32:64],2)

    e_l3 = f_e(l3)
    e_l3_ = f_e(l3_)
    in_xor = e_l3^e_l3_
    out_xor = f_p_inv(r3^r3_^l0^l0_)

    fp = open('diff_excel.json','r')
    IN = json.load(fp)
    in_list = IN[0][in_choose(in_xor,0)][out_choose(out_xor,0)]

    for i in range(8): 
        in_list = IN[i][in_choose(in_xor,i)][out_choose(out_xor,i)]
        for j in in_list: 
            key_tmp = j^in_choose(e_l3,i)
            bool_exc[i][key_tmp] += 1

    key48 = ''
    for i in range(8): 
        key48 = key48 + '{:0>6b}'.format(f_max(bool_exc[i]))
    return int(key48,2)

def f_e(r): 
    # Ri_extend
    r= rev32(r)
    des_E=[31, 0, 1, 2, 3, 4, 3, 4, 5, 6, 7, 8, 7, 8, 9, 10, 11, 12, 11, 12, 13, 14, 
           15, 16, 15, 16, 17, 18, 19, 20, 19, 20, 21, 22, 23, 24, 23, 24, 25, 26, 27, 28, 27, 28, 29, 30, 31, 0]
    tmp=''
    for i in range(48): 
        tmp = tmp + str(bin_judge(r,des_E[i]))
    return int(tmp,2)

def f_p_inv(x): 
    x = rev32(x)
    p_inv = [8, 16, 22, 30, 12, 27, 1, 17, 23, 15, 29, 5, 25, 19, 9, 0, 
             7, 13, 24, 2, 3, 28, 10, 18, 31, 11, 21, 6, 4, 26, 14,20]
    tmp=''
    for i in range(32): 
        tmp = tmp + str(bin_judge(x,p_inv[i]))
    return int(tmp,2)

def rev32(n):
    bit="{:0>32b}".format(n)
    return int(bit[::-1],2)

def in_choose(n,i): 
    tmp="{:0>48b}".format(n)
    return int(tmp[i*6:i*6+6],2)

def out_choose(n,i): 
    tmp="{:0>32b}".format(n)
    return int(tmp[i*4:i*4+4],2)

def f_max(l): 
    max = -1
    index = -1
    for i in range(len(l)): 
        if l[i] > max: 
            max = l[i]
            index = i 
    return index

def bin_judge(k,i):
    return (k>>(i))&1

if __name__ == '__main__':
    p1,c1,p2,c2=input('p1,c1,p2,c2 -> ').split()
    p1,c1,p2,c2 = int(p1,16),int(c1,16),int(p2,16),int(c2,16)
    bool_exc = [[0 for i in range(128)]for i in range(8)]
    print(hex(diff_attack(p1,c1,p2,c2,bool_exc)))
