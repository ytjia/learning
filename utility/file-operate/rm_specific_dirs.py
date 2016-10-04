#!/usr/bin/env python
# coding=utf-8

"""
删除指定目录下各文件夹内指定名称的目录
"""

import os
import sys

def rm_specific_dir(top, dir_name):
    for root, dirs, files in os.walk(top, topdown=False):
        for name in dirs:
            if name == dir_name:
                os.rmdir(os.path.join(root, name))


if __name__ == '__main__':
    rm_specific_dir(sys.argv[1], sys.argv[2])

