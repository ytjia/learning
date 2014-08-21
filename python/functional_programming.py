# -*- coding: utf-8 -*-

"""
do some verification and excercise
article link: http://coolshell.cn/articles/10822.html
"""

a = 0
b = [0, 1]

def incre(x):
    x.append(2)
    return x

def fuck(fn):
    print "fuck %s!" % fn.__name__[::-1].upper()
 
@fuck
def wfg():
    pass

# if __name__ == '__main__':
#     x = incre(b)
#     print b, x
