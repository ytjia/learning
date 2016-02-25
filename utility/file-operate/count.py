# -*- coding: utf-8 -*-

"""
统计根据地理位置提取的学生群体中，微博用户数量、微博信息显示为学生数量。
"""
def count_stu():
    finput = open(r'/Users/ytjia/Downloads/multi_univ')
    total = 0
    weibo_stu = 0
    occu = 0
    for line in finput.readlines():
        record = line.split()
        if record[-1] == '1':
            weibo_stu += 1
        if record[-1] != '-1':
            occu += 1
        total += 1
    print weibo_stu
    print occu
    print total
    finput.close()


if __name__ == '__main__':
    count_stu()
