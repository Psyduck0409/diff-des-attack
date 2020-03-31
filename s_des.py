#!/usr/bin/env python
# -*- coding: utf-8 -*-

def encode(p,k,flag = 0):
    p,k=rev8(p),rev10(k)
    init = [[1,5,2,0],[3,7,4,6]]
    init_inv = [3,0,2,4,6,1,7,5]
    key = key_create(k,flag)
    l=[]
    r=[]
    for i in range(4): 
        l.append(bin_judge(p,init[0][i]))
        r.append(bin_judge(p,init[1][i]))

    for i in range(2):
        l,r = f(l,r,key[i])
    res = r+l 
    ans = 0
    for i in range(8): 
        ans = ans<<1
        ans = ans + res[init_inv[i]]
    return ans

def decode(c,k): 
    return encode(c,k,1)

def key_create(k,flag): 
    k1 = [0,6,8,3,7,2,9,5]
    k2 = [7,2,5,4,9,1,8,0]
    kk=[]
    tmp=[]
    for i in range(8):
        tmp.append(bin_judge(k,k1[i]))
    kk.append(tmp)
    tmp=[]
    for i in range(8):
        tmp.append(bin_judge(k,k2[i]))
    kk.append(tmp)
    if flag: 
        return kk[::-1]
    return kk

def f(l,r,k): 
    EP = [3,0,1,2,1,2,3,0]
    tmp = []
    for i in range(8):
        tmp.append(r[EP[i]]^k[i])
    tmp = s_des_sbox(tmp)
    tmpp=[tmp[1],tmp[3],tmp[2],tmp[0]]
    return r,plus(l,tmpp)

def s_des_sbox(tmp): 
    s = [
            [
                [1,0,3,2],
                [3,2,1,0],
                [0,2,1,3],
                [3,1,0,2]
            ],
            
            [
                [0,1,2,3],
                [2,0,1,3],
                [3,2,1,0],
                [2,1,0,3]
            ]
    ]

    ans=[]
    row = (tmp[4]<<1)+tmp[7]
    col = tmp[6]+(tmp[5]<<1)
    res = s[1][row][col]
    for i in range(2):
        ans.insert(0,res&1)
        res = res>>1
    row = (tmp[0]<<1)+tmp[3]
    col = tmp[2]+(tmp[1]<<1)
    res = s[0][row][col]
    for i in range(2):
        ans.insert(0,res&1)
        res = res>>1
    return ans

def bin_judge(k,i):
    return (k>>(i))&1

def plus(a,b):
    tmp=[]
    l=len(a)
    for i in range(l):
        tmp.append(a[i]^b[i])
    return tmp

def rev10(n):
    bit="{:0>10b}".format(n)
    return int(bit[::-1],2)

def rev8(n):
    bit="{:0>8b}".format(n)
    return int(bit[::-1],2)

if __name__ == '__main__':
    p=int(input(),2)
    k=int(input(),2)
    k2=int(input(),2)
    print(bin(encode(encode(p,k),k2)))
