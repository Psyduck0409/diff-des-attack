#!/usr/bin/env python
# -*- coding: utf-8 -*-

def encode(p,key,num=64,flag=0):
    key=rev(key)#duanxu
    p=rev(p)
    #p init 2*32
    des_init=[
        [57, 49, 41, 33, 25, 17, 9, 1, 59, 51, 43, 35, 27, 19, 11, 3, 61, 53, 45, 37, 29, 21, 13, 5, 63, 55, 47, 39, 31, 23, 15, 7],
        [56, 48, 40, 32, 24, 16, 8, 0, 58, 50, 42, 34, 26, 18, 10, 2, 60, 52, 44, 36, 28, 20, 12, 4, 62, 54, 46, 38, 30, 22, 14, 6]
    ]

    #init_inv 2*32
    des_init_inv = [
        [39, 7, 47, 15, 55, 23, 63, 31, 38, 6, 46, 14, 54, 22, 62, 30, 37, 5, 45, 13, 53, 21, 61, 29, 36, 4, 44, 12, 52, 20, 60, 28],
        [35, 3, 43, 11, 51, 19, 59, 27, 34, 2, 42, 10, 50, 18, 58, 26, 33, 1, 41, 9, 49, 17, 57, 25, 32, 0, 40, 8, 48, 16, 56, 24]
    ]
    k = key_create(key,flag,num) ##keys 
    p_list = bin2list(p,64)
    l=[]
    r=[]
    for i in des_init[0]: 
        l.append(p_list[i])
    for i in des_init[1]: 
        r.append(p_list[i])
    for i in range(16): 
        l,r = en(l,r,k,i) # encode
    c_list = r+l 
    c_list1=[]
    for i in range(64):
        c_list1.append(c_list[des_init_inv[i//32][i%32]])
    c = list2int(c_list1)
    return c

def decode(c,key,num=64):
    return encode(c,key,num,1)

def en(l,r,k,i):
    tmp = plus(my_e(r),k[i])
    tmp = my_s(tmp)
    tmp = my_p(tmp)
    return r,plus(tmp,l)

def plus(a,b):
    tmp=[]
    l=len(a)
    for i in range(l):
        tmp.append(a[i]^b[i])
    return tmp

def my_e(r): 
    # Ri_extend
    des_E=[31, 0, 1, 2, 3, 4, 3, 4, 5, 6, 7, 8, 7, 8, 9, 10, 11, 12, 11, 12, 13, 14, 
           15, 16, 15, 16, 17, 18, 19, 20, 19, 20, 21, 22, 23, 24, 23, 24, 25, 26, 27, 28, 27, 28, 29, 30, 31, 0]
    tmp=[]
    for i in range(48): 
        tmp.append(r[des_E[i]])
    return tmp

def my_s(r): 
    # Sandbox
    des_s=[
        [
            [14,4,13,1,2,15,11,8,3,10,6,12,5,9,0,7],
            [0,15,7,4,14,2,13,1,10,6,12,11,9,5,3,8],
            [4,1,14,8,13,6,2,11,15,12,9,7,3,10,5,0],
            [15,12,8,2,4,9,1,7,5,11,3,14,10,0,6,13]
        ],

        [
            [15,1,8,14,6,11,3,4,9,7,2,13,12,0,5,10],
            [3,13,4,7,15,2,8,14,12,0,1,10,6,9,11,5],
            [0,14,7,11,10,4,13,1,5,8,12,6,9,3,2,15],
            [13,8,10,1,3,15,4,2,11,6,7,12,0,5,14,9]
        ],

        [
            [10,0,9,14,6,3,15,5,1,13,12,7,11,4,2,8],
            [13,7,0,9,3,4,6,10,2,8,5,14,12,11,15,1],
            [13,6,4,9,8,15,3,0,11,1,2,12,5,10,14,7],
            [1,10,13,0,6,9,8,7,4,15,14,3,11,5,2,12]
        ],

        [
            [7,13,14,3,0,6,9,10,1,2,8,5,11,12,4,15],
            [13,8,11,5,6,15,0,3,4,7,2,12,1,10,14,9],
            [10,6,9,0,12,11,7,13,15,1,3,14,5,2,8,4],
            [3,15,0,6,10,1,13,8,9,4,5,11,12,7,2,14]
        ],

        [
            [2,12,4,1,7,10,11,6,8,5,3,15,13,0,14,9],
            [14,11,2,12,4,7,13,1,5,0,15,10,3,9,8,6],
            [4,2,1,11,10,13,7,8,15,9,12,5,6,3,0,14],
            [11,8,12,7,1,14,2,13,6,15,0,9,10,4,5,3]
        ],

        [
            [12,1,10,15,9,2,6,8,0,13,3,4,14,7,5,11],
            [10,15,4,2,7,12,9,5,6,1,13,14,0,11,3,8],
            [9,14,15,5,2,8,12,3,7,0,4,10,1,13,11,6],
            [4,3,2,12,9,5,15,10,11,14,1,7,6,0,8,13]
        ],

        [
            [4,11,2,14,15,0,8,13,3,12,9,7,5,10,6,1],
            [13,0,11,7,4,9,1,10,14,3,5,12,2,15,8,6],
            [1,4,11,13,12,3,7,14,10,15,6,8,0,5,9,2],
            [6,11,13,8,1,4,10,7,9,5,0,15,14,2,3,12]
        ],

        [
            [13,2,8,4,6,15,11,1,10,9,3,14,5,0,12,7],
            [1,15,13,8,10,3,7,4,12,5,6,11,0,14,9,2],
            [7,11,4,1,9,12,14,2,0,6,10,13,15,3,5,8],
            [2,1,14,7,4,10,8,13,15,12,9,0,3,5,6,11]
        ]
    ]
    r_new=[]

    for i in range(8):
        row = r[i*6+5]+2*r[i*6]
        col = 8*r[i*6+1]+r[i*6+2]*4+r[i*6+3]*2+r[i*6+4]
        tmp = des_s[i][row][col]
        temp=[]
        for j in range(4): 
            temp.insert(0,tmp&1)
            tmp=tmp>>1
        r_new.extend(temp)
    return r_new

def my_p(r):
    # P
    des_P = [15, 6, 19, 20, 28, 11, 27, 16, 0, 14, 22, 25, 4, 17, 30, 9, 
             1, 7, 23, 13, 31, 26, 2, 8, 18, 12, 29, 5, 21, 10, 3, 24]
    tmp=[]
    for i in range(32):
        tmp.append(r[des_P[i]])
    return tmp


def key_create(k,flag,num=64): 
    #key 64 to 56
    des_transform = [
        [56, 48, 40, 32, 24, 16, 8, 0, 57, 49, 41, 33, 25, 17, 9, 1, 58, 50, 42, 34, 26, 18, 10, 2, 59, 51, 43, 35],
        [62, 54, 46, 38, 30, 22, 14, 6, 61, 53, 45, 37, 29, 21, 13, 5, 60, 52, 44, 36, 28, 20, 12, 4, 27, 19, 11, 3]
    ]

    #keyn 56 to 48
    des_permuted=[13, 16, 10, 23, 0, 4, 2, 27, 14, 5, 20, 9, 22, 18, 11, 3, 25, 7, 15, 6, 26, 19, 12, 1, 
                  40, 51, 30, 36, 46, 54, 29, 39, 50, 44, 32, 47, 43, 48, 38, 55, 33, 52, 45, 41, 49, 35, 28, 31]

    #rotations
    des_rotations = [1,1,2,2,2,2,2,2,1,2,2,2,2,2,2,1]

    #let us create the keys
    keys56 = []
    keys48 = []
    key = []
    tmp = []
    if num == 64:
        for i in des_transform:
            tmp=[]
            for j in i: 
                tmp.append(bin_judge(k,j))
            keys56.append(tmp)
    else: 
        for i in range(2):
            for j in range(28):
                tmp.append(bin_judge(k,j+28*i))
            keys56.append(tmp)
    for i in range(16):
        keys56[0]=left_move(des_rotations[i],keys56[0])
        keys56[1]=left_move(des_rotations[i],keys56[1])
        key=[]
        for j in range(48): 
            key.append(keys56[des_permuted[j]//28][des_permuted[j] % 28])
        keys48.append(key)
    if flag: 
        return keys48[::-1]
    return keys48


def left_move(a,A):
    return A[a:]+A[:a]


def bin_judge(k,i):
    return (k>>(i))&1

def list2int(x):
    l = len(x)
    tmp=0
    for i in x:
        tmp = tmp<<1
        tmp += i
    return tmp

def bin2list(x,times):
    tmp=[]
    for i in range(times):
        tmp.append(x&1)
        x=x>>1
    return tmp

def rev(n):
    bit="{:0>64b}".format(n)
    return int(bit[::-1],2)

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
