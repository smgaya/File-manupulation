__author__ = 'siddiqui'

import os
import sys
from os.path import basename


replace = [".pdf"]


temp = os.walk(sys.argv[1], topdown=False)


for root, dirs, files in temp:
    for i in files:
        folder = os.path.join(root)
        file = os.path.join(root,i)
        fileName, fileExtension = os.path.splitext(file)
        name = basename(os.path.join(root,i))
        #newname = rena (name)
        #print('\t%s' % fileExtension)
        #exit()
        if file.endswith(".pdf"):
            print(os.path.join(root, file))

    
#TODO truncate white space
#TODO add more rippers
print "Renaming Complete"
raw_input()


import os
import shutil

srcfile = 'a/long/long/path/to/file.py'
dstroot = '/home/myhome/new_folder'


assert not os.path.isabs(srcfile)
dstdir =  os.path.join(dstroot, os.path.dirname(srcfile))

os.makedirs(dstdir) # create all directories, raise an error if it already exists
shutil.copy(srcfile, dstdir)