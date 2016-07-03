__author__ = 'mgaya'

import os
import sys
from os.path import basename


#replace = [".mp3"]

def rena (nameoffile) :

    for value in replace:
            nameoffile = nameoffile.replace(value," ")

    for y in range(1900,2015):
            if str(y) in nameoffile:
                nameoffile = nameoffile.replace(str(y)," ")

    return nameoffile

# Set the directory you want to start from
#rootDir = '.'



#program_name = sys.argv[0] 
temp = os.walk(sys.argv[1], topdown=True)
for dirName, subdirList, fileList in  temp:
    #getin = raw_input('>>')
    getin = "music"
    #rootname = dirName.replace(getin,dirName)
    dirName =  os.rename(dirName,getin)
    for subdir in subdirList:
        subdir = os.rename(subdir,os.path.join(dirName) + "subdir[:6])
        print('\t%s' % subdir)
        exit()


        


