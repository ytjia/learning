# -*- coding: utf-8 -*-

"""
"""

roomtype_dict = {}

def hotel_roomtype_stat():
    finput = open(r'/Users/ytjia/Downloads/Hotel/酒店房型属性快照20140409')

    for line in finput.readlines():
        record = line.split()
        attr_value = record[4]
        roomtype_list = attr_value.split(',')
        for roomtype in roomtype_list:
            if roomtype in roomtype_dict:
                roomtype_dict[roomtype] += 1
            else:
                roomtype_dict[roomtype] = 1
    finput.close()
    for roomtype in roomtype_dict:
        if roomtype_dict[roomtype] > 100:
            print roomtype + ' : ' + str(roomtype_dict[roomtype])

if __name__ == '__main__':
    hotel_roomtype_stat()
