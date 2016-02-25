# -*- coding: utf-8 -*-

"""
@author:    jiayitian
@date:      2014/01/13
"""

DATE = '131201_140112'
def remove_duplicate():
    finput = open(
        r'/Users/ytjia/Downloads/Hotel/deal_visit_shanghai_local_%s' % DATE)
    foutput = open(
        r'/Users/ytjia/WorkSpace/hotelpromotion/userid/deal_visit_shanghai_local_%s'
         % DATE, 'w')
    userid_set = set()
    
    for line in finput.readlines():
        record = line.split()
        userid_set.add(record[0])
    for userid in userid_set:
        foutput.write(userid + '\n')

if __name__ == '__main__':
    remove_duplicate()
