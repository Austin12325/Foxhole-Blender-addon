import bpy
import glob
import os

batpath = bpy.data.scenes["Scene"].sna_batfilepath
buttonindex = bpy.data.scenes["Scene"].sna_fileindex_public -1 

indexlist = []

for x in glob.glob(batpath+"/*.*", recursive=False):
    print(x)
    indexlist.append(x)
        
os.startfile(indexlist[buttonindex])
