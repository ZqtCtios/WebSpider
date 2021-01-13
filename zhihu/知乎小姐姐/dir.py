import os
import shutil
def rename():
    i=1
    for x in os.listdir():
        if os.path.isdir(x):
            j=1
            for y in os.listdir(x):
                filename='{}/{}'.format(x,y)
                refilename='{}/{}'.format(x,str(j)+os.path.splitext(y)[1])
                os.rename(filename,refilename)
                j+=1
            try:
                os.rename(x,str(i))
                i+=1   
            except:
                pass


def move(mpath):
    for x in os.listdir():
        if os.path.isdir(x):
            for y in os.listdir(x):
                filename='{}/{}'.format(x,y)
                refilename='{}/{}'.format(mpath,y)
                shutil.move(filename,refilename)      
				
rename()