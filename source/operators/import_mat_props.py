import bpy
from glob import glob
    #https://b3d.interplanety.org/en/how-to-split-and-join-blender-interface-windows-thruough-the-python-api/
    #https://stackoverflow.com/questions/14798220/how-can-i-search-sub-folders-using-glob-glob-module
dirpath = bpy.data.scenes["Scene"].sna_umodel_exportpath
matname = bpy.context.active_object.material_slots[0].name+'.props.txt'
blendpath = bpy.data.filepath


if bpy.context.screen.show_fullscreen == False:                                 # Throw report if the user is in fullscreen mode (can't split window if in fullscreen)
    #for path in glob(dirpath, recursive=True):
    for matslots in bpy.context.object.material_slots:                          # Get the name of every material on selected object, search for it in exported file
        for file in glob(dirpath+'/**/*'+matslots.name+'.props.txt',recursive=True):
            bpy.ops.text.open(filepath=file)
            print(file)
        
        print(matslots.name)
else: 
    self.report({'INFO'}, 'Please leave fullscreen mode (shift spacebar)')



if bpy.context.screen.show_fullscreen == False:
    if bpy.context.screen.areas[0].type == "TEXT_EDITOR":
        pass
    else:                                                                       # Split window and newly created text editor to view the last imported file.
        bpy.ops.screen.area_split(direction='VERTICAL', factor=0.75)
        bpy.context.screen.areas[-1].type = "TEXT_EDITOR"
        
        text = bpy.data.texts[-1]
        for area in bpy.context.screen.areas:
            if area.type == 'TEXT_EDITOR':
                area.spaces[0].text = text
else: 
    self.report({'INFO'}, 'Please leave fullscreen mode (shift spacebar)')

bpy.ops.wm.save_as_mainfile(filepath=bpy.data.filepath)
print('files imported')
