#!/usr/bin/env python
# -*- coding: utf-8 -*-
import little_des as des
import diff_attack as attack

def diff_hack(p_list,c_list): 
    key_bool = {}
    keys=[]
    bool_exc = [[0 for i in range(128)]for i in range(8)]
    for (pp,cc) in zip(p_list,c_list): 
        p1 = pp[0]
        c1 = cc[0]
        p2 = pp[1]
        c2 = cc[1]
        key = attack.diff_attack(p1,c1,p2,c2,bool_exc)
    s_max = [0 for i in range(8)]
    for i in range(8): 
        max_tmp = -1
        for j in bool_exc[i]:
            if j>max_tmp: 
                max_tmp = j
        s_max[i] = max_tmp
    s_max_elem = [[]for i in range(8)]
    for i in range(8):
        index = 0
        for j in bool_exc[i]:
            if j == s_max[i]: 
                s_max_elem[i].append(index)
            index +=1

    for i0 in s_max_elem[0]: 
        for i1 in s_max_elem[1]: 
            for i2 in s_max_elem[2]: 
                for i3 in s_max_elem[3]: 
                    for i4 in s_max_elem[4]: 
                        for i5 in s_max_elem[5]: 
                            for i6 in s_max_elem[6]: 
                                for i7 in s_max_elem[7]: 
                                    key_str = '{:0>6b}'.format(i0)+'{:0>6b}'.format(i1)+'{:0>6b}'.format(i2)+'{:0>6b}'.format(i3)+'{:0>6b}'.format(i4)+'{:0>6b}'.format(i5)+'{:0>6b}'.format(i6)+'{:0>6b}'.format(i7)
                                    key = int(key_str,2)
                                    keys.append(key)
    for i in keys:
        explode(i,key_bool)

    res = f_max(key_bool)
    return res


def left_move(a,A):
    return A[a:]+A[:a]

def bin_judge(k,i):
    return (k>>(i))&1

def explode(key,key_bool):
    des_per_inv = [4, 23, 6, 15, 5, 9, 19, 17, -1, 11, 2, 14, 22, 0, 
                  8, 18, 1, -1, 13, 21, 10, -1, 12, 3, -1, 16, 20, 7, 
                  46, 30, 26, 47, 34, 40, -1, 45, 27, -1, 38, 31, 24, 43, 
                  -1, 36, 33, 42, 28, 35, 37, 44, 32, 25, 41, -1, 29, 39] 
    p_str=''
    for j in des_per_inv: 
        if j!=-1: 
            p_str = p_str+str(bin_judge(key,47-j))
        else: 
            p_str = p_str+'x'
    l_tmp = left_move(24,p_str[0:28])
    r_tmp = left_move(24,p_str[28:56])
    key = l_tmp+r_tmp 
    for i in range(1<<8): 
        i_str = '{:0>8b}'.format(i)
        index = 0
        key_g=''
        for j in range(56):
            if key[j] == 'x': 
                key_g = key_g+ i_str[index]
                index = index +1 
            else: 
                key_g = key_g+key[j]
        this_key = int(key_g,2)
        for (pp,cc) in zip(p_list,c_list): 
            for (p,c) in zip(pp,cc): 
                if des.encode(p,this_key,56) == c:
                    if this_key in key_bool.keys():
                        key_bool[this_key] +=1
                    else: 
                        key_bool[this_key] = 1

def f_max(x): 
    max = -1
    index = -1
    for k,v in x.items(): 
        if v>max: 
            max = v
            index = k
    return index


if __name__ == '__main__':
    p_list = [[0x375BD31F6ACDFF31,0x486911026ACDFF31],[0x357418DA013FEC86,0x12549847013FEC86],[0x748502CD38451097,0x3874756438451097],[0x02152633A124F6B6,0x52873E68A124F6B6],[0x52873E68A124F6B6,0x19C26156A124F6B6],[0x19C26156A124F6B6,0xDF2D047AA124F6B6],[0xDF2D047AA124F6B6,0x52873E68A124F6B6],[0xDF2D047AA124F6B6,0x02152633A124F6B6]]
    c_list = [[0x7d9aefbf2479b043,0x9cff22a4855ffb67],[0x34a4097c3639a9f7,0x274069bf45c63d96],[0x465ec3d02b29239,0x1acaa1a647de5696],[0xaa6b7f98bcfc6d92,0x295822edd97d94a9],[0x295822edd97d94a9,0xd090b9d6abc68491],[0xd090b9d6abc68491,0x8cce692006d01968],[0x8cce692006d01968,0x295822edd97d94a9],[0x8cce692006d01968,0xaa6b7f98bcfc6d92]]
    print(hex(diff_hack(p_list,c_list)))
