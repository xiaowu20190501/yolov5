# import os
# from os import listdir, getcwd
# from os.path import join

# wd = getcwd()
# # print(wd)

import os
import sys
from os import getcwd

def listfiles(rootDir, txtfile, label=0):
    wd = getcwd()
    # print(wd)
    ftxtfile = open(txtfile, 'w')
    list_dirs = os.walk(rootDir)
    count = 0
    dircount = 0
    for root,dirs,files in list_dirs:
        for d in dirs:
            print(os.path.join(str(wd) + "/" + root, d))
            dircount += 1
        for f in files:
            print(os.path.join(str(wd) + "/" + root, f))
            # ftxtfile.write(os.path.join(root, f)+ ' ' + str(label) + '\n')
            # ftxtfile.write(os.path.join(str(wd) + "/" + root, f) + '\n')
            ftxtfile.write(os.path.join(root, f) + '\n')
            count += 1
    # print(str(wd) + "/" + rootDir + ' has ' + str(count) + ' files')
    print(rootDir + ' has ' + str(count) + ' files')


listfiles('/home/aiden00/abwu_workspace/coco/labels/val2017', '/home/aiden00/abwu_workspace/coco/val2017_test.txt')