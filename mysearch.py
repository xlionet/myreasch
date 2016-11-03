#!usr/bin/python
#coding=utf-8

import sys
import os
import re

filter = ['h','cpp']

num = 0
result = []
paths = []

def search(path=None, cont=None):
    if not path or not cont:
        print "err..."
        return

    global num
    findFloder(path, cont)

def findFloder(path, cont):
    arr = path.split('/')
    if not arr[-1].startswith('.'):
        if os.path.isdir(path):
            floderslist = os.listdir(path)
            for f in floderslist:
                findFloder(path+'/'+f, cont)
        elif os.path.isfile(path):
            searchcont(path,cont)

def searchcont(path, cont):
    if path.split('.')[-1].lower() in filter:

        global num
        global result
        global paths

        file = open(path, 'r')
        content = file.readlines()

        file.close()

        for index, x in enumerate(content):
            if cont in x:
                num += 1
                result.append(cont)
                paths.append(path)
                print cont ,'in--->',path,'index--->',index+1

                break
        return

def getTabelList():
    sql_path = r'/home/passi/Desktop/temp/crebas.sql'
    fpsql = open(sql_path, 'r', 1)
    crt_table = r'create table.*'
    class_name_pattern = re.compile(crt_table)

    tables = []
    for line in fpsql:
        temp =  class_name_pattern.findall(line)
        if temp == [] :
            continue

        else:
            flag = False
            str= temp.__str__()
           # print str[14:-4]
            tables.append(str[14:-4])
    fpsql.close()
    return tables

if __name__ == '__main__':
    tables = getTabelList()

    for x, table in enumerate(tables):
       search(r'/home/passi/Desktop/temp/NHO v3.0.3',table)
    result=list(set(result))

    print result.__len__(),result


