# -*- coding: utf-8 -*-

"""divide a set of files to different folders in which there are no more than 200 files.
"""

import os
import sys

FOLDER_CAPACITY = 200

def files_divide(src_dir, dest_dir):
    count = 0
    current_folder = ''

    for item in os.listdir(src_dir):
        abs_item = os.path.join(src_dir, item)
        if os.path.isfile(abs_item):
            count += 1
            if count % FOLDER_CAPACITY == 1:
                current_folder = os.path.join(dest_dir, 
                    str(count / FOLDER_CAPACITY))
                os.mkdir(current_folder)
            open(os.path.join(current_folder, item), 'wb').write(
                open(abs_item, 'rb').read())
        else:
            pass

if __name__ == '__main__':
    files_divide(sys.argv[1], sys.argv[2])
