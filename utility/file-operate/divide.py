# -*- coding: utf-8 -*-

"""
酒店运营将用户随机分组
"""
def divide():
    finput = open(r'/Users/ytjia/Downloads/Hotel/725/转新')
    foutput1 = open(r'/Users/ytjia/Downloads/Hotel/725/转新1.txt', 'wb')
    foutput2 = open(r'/Users/ytjia/Downloads/Hotel/725/转新2.txt', 'wb')

    cnt = 0
    for line in finput.readlines():
        record = line.split()
        if cnt % 2 == 0:
            foutput1.write(record[0]+'\n')
        else:
            foutput2.write(record[0]+'\n')
        cnt += 1
        # if cnt > 105000:
        #     foutput4.write(record[0]+'\n')
    finput.close()
    foutput1.close()
    foutput2.close()

def remove_t():
    idset = set()
    finput = open(r'/Users/ytjia/Downloads/Hotel/ttttotal')
    for line in finput.readlines():
        record = line.split()
        idset.add(record[0])
    finput.close()
    finput = open(r'/Users/ytjia/Downloads/Hotel/第6组学生part2')
    foutput = open(r'/Users/ytjia/Downloads/Hotel/newstu2', 'w')
    for line in finput.readlines():
        record = line.split()
        cc = record[0]
        if cc in idset:
            pass
        else:
            foutput.write(cc +'\n')


if __name__ == '__main__':
    divide()
    # remove_t()
