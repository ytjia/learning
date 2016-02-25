# -*- coding: utf-8 -*- 

"""
"""

def cal_hold_time():
    array = [[159310567000, 2023791, 0, 'mob'], 
    [129436448956, 565259, 0, 'www'],
    [14177828533, 152465, 1, 'mob'],
    [6834787148, 19915, 1, 'www']
    ]

    new_array = [[159310567000, 2023791, 0, 'mob'],
    [129436448956, 565259, 0, 'www'],
    [14177828533, 152465, 1, 'mob'],
    [6834787148, 19915, 1, 'www']
    ]

    for item in new_array:
        hold_time = float(item[0]) / 3600 / item[1]
        print item[2], item[3]
        print hold_time

if __name__ == '__main__':
    cal_hold_time()