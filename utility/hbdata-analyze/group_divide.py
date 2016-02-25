# -*- coding: utf-8 -*-

"""
运营活动将用户随机分组

Args:
    source_addr: a path string of the file to be divided.
    group_num: a number tells how many groups are needed.
    target_name: a name string of the produced file. 
"""

import os

def rand_divide(source_addr, group_num, target_name):
    if not os.path.exists(target_name):
        os.mkdir(target_name)
    os.chdir(target_name)
    finput = open(source_addr)
    content = {}
    for i in range(0, group_num):
        content[i] = []
    
    cnt = 0
    for line in finput.readlines():
        record = line.split()
        content[cnt % group_num].append(record[0]+'\n')
        cnt += 1
    finput.close()
    for i in range(0, group_num ):
        foutput = open(target_name+str(i+1), 'wb')
        for line in content[i]:
            foutput.write(line)
        foutput.close()
    return 0

if __name__ == '__main__':
    s_addr = raw_input('Enter the source_addr:')
    g_numb = raw_input('Enter the group_num:')
    t_name = raw_input('Enter the target_name:')
    rand_divide(s_addr, int(g_numb), t_name)
