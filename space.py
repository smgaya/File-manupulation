#!/usr/bin/env python3
import os
import shutil
import sys

for root, dirs, files in os.walk(sys.argv[1], topdown=False):
    for f in files:
        if f.startswith(" "):
            shutil.move(root+"/"+f, root+"/"+f.strip())
    for dr in dirs:
        if dr.startswith(" "):
            shutil.move(root+"/"+dr, root+"/"+dr.strip())