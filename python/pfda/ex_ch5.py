# -*- coding: utf-8 -*-

""" pandas excersie.
@author:    jiayitian
@date:      2014/02/17
"""

from pandas import Series, DataFrame
import pandas as pd

def ip_handler():
    ip_table = pd.read_table(r'/Users/ytjia/Downloads/education_ip.txt', 
        names=['begin', 'end', 'count'], skiprows=1, skip_footer=1)
    print ip_table[:5]
    print ip_table[-5:]

if __name__ == '__main__':
    ip_handler()
