import os
import datetime
import sys


#program_name = sys.argv[0] 
temp = os.walk(sys.argv[1], topdown=True)
for root, dirs, files in temp:
    for i in files:
        folder = os.path.join(root)
        file = os.path.join(root,i)
        file_modified = datetime.datetime.fromtimestamp(os.path.getmtime(file))
        #print (file)
        #exit()
        if file.endswith(".pdf"):
            #if (datetime.datetime.now() - file_modified < datetime.timedelta(days=1276)) and (datetime.datetime.now() - file_modified > datetime.timedelta(days=181)):
            #    os.remove(file)
            #    print(os.path.join(root, file))
            print(file_modified)
        else:
            os.remove(file)
