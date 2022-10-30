import bpy
from glob import glob
    #https://b3d.interplanety.org/en/how-to-split-and-join-blender-interface-windows-thruough-the-python-api/
    #https://stackoverflow.com/questions/14798220/how-can-i-search-sub-folders-using-glob-glob-module
dirpath = bpy.data.scenes["Scene"].sna_umodel_exportpath
matname = bpy.context.active_object.material_slots[0].name+'.props.txt'
new_area = bpy.context.screen.areas[-1]


if bpy.context.screen.show_fullscreen == False:
    #for path in glob(dirpath, recursive=True):
    for matslots in bpy.context.object.material_slots:
        for file in glob(dirpath+'/**/*'+matslots.name+'.props.txt',recursive=True):
            bpy.ops.text.open(filepath=file)
            print(file)
        
        print(matslots.name)
else: 
    self.report({'INFO'}, 'Please leave fullscreen mode (shift spacebar)')




if bpy.context.window_manager.windows[-1].screen.areas[-1].type == "TEXT_EDITOR":
    pass
else: 
    bpy.ops.screen.area_split(direction='VERTICAL', factor=0.75)
    bpy.context.window_manager.windows[-1].screen.areas[-1].type = "TEXT_EDITOR"



bpy.ops.wm.save_as_mainfile(filepath=bpy.data.filepath)
print('files imported')
