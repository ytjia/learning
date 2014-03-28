#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

"""transfer numbers to corresponding chinese word
@author:    jiayitian
@date:      2013/12/23
"""


import string

CHINESE_DIGIT = ["零", "壹", "贰", "叁", "肆", "伍", "陆", "柒", "捌", "玖"]
CHINESE_UNIT = ["拾", "佰", "仟", "万", "拾", "佰", "仟", "亿", "分", "角"]

def num_to_chinese(number):
    result = ""
    if '.' in number:
        integer_part, decimal_part = number.split('.')
        result = integer_to_chinese(integer_part)
        if result != "":
            result += "圆"
        result += decimal_to_chinese(decimal_part)
    else:
        result = integer_to_chinese(number) 
        if result == "":
            result = CHINESE_DIGIT[0]
        result += "圆整"
    return result

def integer_to_chinese(integer):
    is_zero = False
    str_int = ""
    final_index = len(integer) - 1
    for index in range(final_index, -1, -1):
        digit = int(integer[index])
        if digit == 0:
            if not is_zero:
                is_zero = True
        else:
            if is_zero:
                if str_int != "":
                    str_int = CHINESE_DIGIT[0] + str_int
                is_zero = False
            unit_index = final_index - index - 1
            if unit_index > -1:
                str_int = (CHINESE_DIGIT[digit] 
                    + CHINESE_UNIT[unit_index%8] 
                    + str_int) 
            else:
                str_int = CHINESE_DIGIT[digit] + str_int
    return str_int

def decimal_to_chinese(decimal):
    str_dec = ""
    jiao = decimal[0]
    if jiao != '0':
        str_dec = CHINESE_DIGIT[int(jiao)] + CHINESE_UNIT[-1]
    if len(decimal) > 1 and decimal[1] != '0':
        str_dec += CHINESE_DIGIT[int(decimal[1])] + CHINESE_UNIT[-2]
    return str_dec

if __name__ == '__main__':
    while 1:
        input_num = raw_input("please enter the number to transfer: ")
        print num_to_chinese(input_num)

# unfinished
