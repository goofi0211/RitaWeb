#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#a test for traverse directory

__author__ = 'AlbertS'

import os
import os.path

f = open('outline.txt','w')

def dfs_showdir(path, depth):
    if depth == 0:
        print("root:[" + path + "]")
        temp="root:[" + path + "]"+'\n'
        f.write(temp)
    for item in os.listdir(path):
        if '.git' not in item:
            print("|      " * depth + "|--" + item)
            temp="|      " * depth + "|--" + item+'\n'
            f.write(temp)
            newitem = path +'/'+ item
            if os.path.isdir(newitem):
                dfs_showdir(newitem, depth +1)

if __name__ == '__main__':
    dfs_showdir('.', 0)
    f.close()