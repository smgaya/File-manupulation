__author__ = 'mgaya'

import os
import sys
from os.path import basename


replace = [".mp3"]

def r1 (nameoffile) :

    for value in replace:
        #nameoffile = nameoffile.replace(value,"/") 771.22_7F-01708.07
        nameoffile = "-" + nameoffile[:6]

    return nameoffile



def f1 (nameoffile) :

    for value in replace:
        #nameoffile = nameoffile.replace(value,"/")
        nameoffile = "-" +  nameoffile[:-25]

    return nameoffile

def r2 (nameoffile) :

    for value in replace:
        #nameoffile = nameoffile.replace(value,"/")
        nameoffile =  "-" + nameoffile[:6]

    return nameoffile


def f2 (nameoffile) :

    for value in replace:
        #nameoffile = nameoffile.replace(value,"/")
        nameoffile = "-" +  nameoffile[:-25]

    return nameoffile

def r3 (nameoffile) :

    for value in replace:
        #nameoffile = nameoffile.replace(value,"/")
        nameoffile ="-" +  nameoffile[:4]

    return nameoffile


def f3 (nameoffile) :

    for value in replace:
        #nameoffile = nameoffile.replace(value,"/")
        nameoffile = "-" +  nameoffile[:-25]

    return nameoffile

def r4 (nameoffile) :

    for value in replace:
        #nameoffile = nameoffile.replace(value,"/")
        nameoffile ="-" +  nameoffile[:9]

    return nameoffile


def f4 (nameoffile) :

    for value in replace:
        #nameoffile = nameoffile.replace(value,"/")
        nameoffile = "-" + nameoffile[:-25]

    return nameoffile
def r5 (nameoffile) :

    for value in replace:
        #nameoffile = nameoffile.replace(value,"/")
        nameoffile = "-" + nameoffile[:6]

    return nameoffile


def f5 (nameoffile) :

    for value in replace:
        #nameoffile = nameoffile.replace(value,"/")
        nameoffile = "-" + nameoffile[:-25]

    return nameoffile





def repslash (nameoffile) :

    for value in replace:
        nameoffile = nameoffile.replace("/","")
        #nameoffile = nameoffile[:6]

    return nameoffile

def repspace (nameoffile) :

    for value in replace:
        nameoffile = nameoffile.replace(" ","")
        #nameoffile = nameoffile[:6]

    return nameoffile



#program_name = sys.argv[0] 
temp1 = os.walk(sys.argv[1], topdown=True)


for root1, dirs1, files1 in temp1:
    
    getroot = "771.22_7F-07720.01_SFRH-"
    os.rename(root1,getroot)
    

    for i1 in files1:
        folder1 = os.path.join(root1)
        file1 = os.path.join(root1,i1)
        fileName1, fileExtension1 = os.path.splitext(file1)
        name1 = basename(os.path.join(root1,i1))
        newname1 = f1 (name1)
        newname1 = repslash(root1) + newname1 + fileExtension1
        os.rename(file1, os.path.join(root1,newname1))

    for i1 in dirs1:

        dir1 = os.path.join(root1,i1)
        name1 = basename(os.path.join(root1,i1))
        newname1 = r1 (name1)
        newname1 = repslash(root1) + newname1 
        try:
            os.rename(dir1,os.path.join(root1,newname1))   
        except OSError:
            pass

         
        temp2 = os.walk(os.path.join(root1,newname1) ,topdown=True)

        for root2, dirs2, files2 in temp2:
            

            
            for i2 in files2:
                folder2 = os.path.join(root2)
                file2 = os.path.join(root2,i2)
                fileName2, fileExtension2 = os.path.splitext(file2)
                name2 = basename(os.path.join(root2,i2))
                newname2 = f2 (name2)
                newname2 = repslash(os.path.basename(root2)) + newname2 + fileExtension2
                os.rename(file2, os.path.join(root2,newname2))

            for i2 in dirs2:

                dir2 = os.path.join(root2,i2)
                name2 = basename(os.path.join(root2,i2))
                newname2 = r2 (name2)
                newname2 = repslash(os.path.basename(root2)) + newname2
                try:
                    os.rename(dir2,os.path.join(root2,newname2))   
                except OSError:
                    pass 
                


                temp3 = os.walk(os.path.join(root2,newname2) ,topdown=True)

                for root3, dirs3, files3 in temp3:
                    

                    

                    for i3 in files3:
                        folder3 = os.path.join(root3)
                        file3 = os.path.join(root3,i3)
                        fileName3, fileExtension3 = os.path.splitext(file3)
                        name3 = basename(os.path.join(root3,i3))
                        newname3 = f3 (name3)
                        newname3 = repslash(os.path.basename(root3)) + newname3 + fileExtension3
                        os.rename(file3, os.path.join(root3,newname3))

                    for i3 in dirs3:

                        dir3 = os.path.join(root3,i3)
                        name3 = basename(os.path.join(root3,i3))
                        newname3 = r3 (name3)
                        newname3 = repslash(os.path.basename(root3)) + newname3 
                        try:
                            os.rename(dir3,os.path.join(root3,newname3))   
                        except OSError:
                            pass
                        


                        temp4 = os.walk(os.path.join(root3,newname3) ,topdown=True)

                        for root4, dirs4, files4 in temp4:
                            

                            

                            for i4 in files4:
                                folder4 = os.path.join(root4)
                                file4 = os.path.join(root4,i4)
                                fileName4, fileExtension4 = os.path.splitext(file4)
                                name4 = basename(os.path.join(root4,i4))
                                newname4 = f4 (name4)
                                newname4 = repslash(os.path.basename(root4)) + newname4 + fileExtension4
                                os.rename(file4, os.path.join(root4,newname4))

                              
                                
                            for i4 in dirs4:

                                dir4 = os.path.join(root4,i4)
                                name4 = basename(os.path.join(root4,i4))
                                newname4 = r4 (name4)
                                newname4 = repslash(os.path.basename(root4)) + newname4 
                                print(root1+'--'+root2+'--'+root4+'--'+ newname4)
                                try:
                                    os.rename(dir3,os.path.join(root4,newname4))   
                                except OSError:
                                    pass



                                temp5 = os.walk(os.path.join(root4,newname4) ,topdown=True)

                                for root5, dirs5, files5 in temp5:
                            

                            

                                    for i5 in files5:
                                        folder5 = os.path.join(root5)
                                        file5 = os.path.join(root,i5)
                                        fileName5, fileExtension5 = os.path.splitext(file5)
                                        name5 = basename(os.path.join(root5,i5))
                                        newname5 = f5 (name5)
                                        newname5 = repslash(os.path.basename(root5)) + newname5 + fileExtension5
                                        os.rename(file5, os.path.join(root5,newname5))

                                      
                                        
                                    for i5 in dirs5:

                                        dir5 = os.path.join(root5,i5)
                                        name5 = basename(os.path.join(root5,i5))
                                        newname5 = r5 (name5)
                                        newname5 = repslash(os.path.basename(root5)) + newname5 
                                        print(root1+'--'+root2+'--'+root5+'--'+ newname5)
                                        try:
                                            os.rename(dir3,os.path.join(root5,newname5))   
                                        except OSError:
                                            pass

                                  


print "Renaming Complete"
raw_input()
