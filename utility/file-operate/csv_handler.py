# -*- coding: utf-8 -*-

"""
"""

import csv

def csv_handler():
    foutput = open(r'dealid29.txt', 'wb')
    with open( '/Users/ytjia/Downloads/29yuan.csv', 'rb') as finput:
        reader = [row for row in csv.reader(finput.read().splitlines())]
        for row in reader:
            item = row[0]
            foutput.write(item + ',')
    finput.close()
    foutput.close()
        
if __name__ == '__main__':
    csv_handler()
