import bpy
import os
scene = bpy.context.scene

if scene.sna_exportpath == "F:\Games\Modding\War.uproject":
    self.report({'ERROR'}, "Code stopped, make sure paths are set correctly")
    
else:
    
    projectlen = len(scene['sna_exportpath'].split("\\")[-1])
    project = scene.sna_exportpath


    filepath = (scene['pskpsaimportpath'].split(scene.sna_umodel_exportpath))
    list = scene['pskpsaimportpath'].split("\\")
    remove = len(list[-1])
    export = filepath[-1][:-remove]


    scene.sna_final_fbx_path = (project[:-projectlen]+"Content"+"\\"+export)

    try:
        os.makedirs(scene.sna_final_fbx_path)
    except:
        pass
        print('code continued, path exists')
    
    
    
    
