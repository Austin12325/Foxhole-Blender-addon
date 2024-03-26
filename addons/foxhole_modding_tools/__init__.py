# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTIBILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

bl_info = {
    "name" : "Foxhole Modding Tools",
    "author" : "Austin, Wolfgang.IX", 
    "description" : "",
    "blender" : (3, 2, 2),
    "version" : (1, 2, 9),
    "location" : "3DView -> N-Panel -> Foxhole Tools",
    "warning" : "",
    "doc_url": "", 
    "tracker_url": "", 
    "category" : "3D View" 
}


import bpy
import bpy.utils.previews
import shutil
import subprocess
import os




def string_to_type(value, to_type, default):
    try:
        value = to_type(value)
    except:
        value = default
    return value


addon_keymaps = {}
_icons = None
class SNA_PT_FOXHOLE_TOOLS_DCC57(bpy.types.Panel):
    bl_label = 'Foxhole Tools'
    bl_idname = 'SNA_PT_FOXHOLE_TOOLS_DCC57'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_context = ''
    bl_category = 'Foxhole'
    bl_order = 0
    bl_ui_units_x=0

    @classmethod
    def poll(cls, context):
        return not (False)

    def draw_header(self, context):
        layout = self.layout

    def draw(self, context):
        layout = self.layout
        box_13F88 = layout.box()
        box_13F88.alert = False
        box_13F88.enabled = True
        box_13F88.active = True
        box_13F88.use_property_split = False
        box_13F88.use_property_decorate = False
        box_13F88.alignment = 'Expand'.upper()
        box_13F88.scale_x = 1.0
        box_13F88.scale_y = 1.0
        box_13F88.operator_context = "INVOKE_DEFAULT" if True else "EXEC_DEFAULT"
        box_13F88.label(text='Warnings', icon_value=2)
        box_DBEC5 = box_13F88.box()
        box_DBEC5.alert = False
        box_DBEC5.enabled = True
        box_DBEC5.active = True
        box_DBEC5.use_property_split = False
        box_DBEC5.use_property_decorate = False
        box_DBEC5.alignment = 'Expand'.upper()
        box_DBEC5.scale_x = 1.0
        box_DBEC5.scale_y = 1.0
        box_DBEC5.operator_context = "INVOKE_DEFAULT" if True else "EXEC_DEFAULT"
        if '00' in str(bpy.context.scene.objects.keys()):
            box_E49EA = box_DBEC5.box()
            box_E49EA.alert = False
            box_E49EA.enabled = True
            box_E49EA.active = True
            box_E49EA.use_property_split = False
            box_E49EA.use_property_decorate = False
            box_E49EA.alignment = 'Expand'.upper()
            box_E49EA.scale_x = 1.0
            box_E49EA.scale_y = 1.0
            box_E49EA.operator_context = "INVOKE_DEFAULT" if True else "EXEC_DEFAULT"
            box_E49EA.label(text='Duplicate objects found ', icon_value=0)
        if (bpy.context.scene.unit_settings.scale_length != 0.009999999776482582):
            box_DBEC5.label(text='Unit scale not matching recommended ', icon_value=0)
            op = box_DBEC5.operator('sna.ausfixunitscale_5db26', text='Fix scale', icon_value=0, emboss=True, depress=False)
        if (bpy.context.area.spaces[0].clip_end != 100000):
            box_DBEC5.label(text='Unit scale not matching recommended ', icon_value=0)
            op = box_DBEC5.operator('sna.ausfixunitscale_5db26', text='Fix scale', icon_value=0, emboss=True, depress=False)
        if (bpy.context.scene.render.fps != 30):
            box_DBEC5.label(text='Framerate not matching recommended', icon_value=0)
            op = box_DBEC5.operator('sna.ausfixframerate_19b08', text='Fix Framerate', icon_value=0, emboss=True, depress=False)


class SNA_OT_Ausfixunitscale_5Db26(bpy.types.Operator):
    bl_idname = "sna.ausfixunitscale_5db26"
    bl_label = "aus.fixunitscale"
    bl_description = "Sets the unit scale to 0.01 to fix export to UE4"
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        return not False

    def execute(self, context):
        start = bpy.context.space_data.clip_start
        end = bpy.context.space_data.clip_end
        bpy.context.scene.unit_settings.system = 'METRIC'
        bpy.context.scene.unit_settings.scale_length = 0.01
        bpy.context.space_data.clip_start = 10
        bpy.context.space_data.clip_end = 100000
        return {"FINISHED"}

    def invoke(self, context, event):
        return self.execute(context)


class SNA_OT_Ausfixframerate_19B08(bpy.types.Operator):
    bl_idname = "sna.ausfixframerate_19b08"
    bl_label = "aus.fixframerate"
    bl_description = "Sets the framerate to 30, and set the base scale to 1.0"
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        return not False

    def execute(self, context):
        exec('bpy.context.scene.render.fps = 30')
        exec('bpy.context.scene.render.fps_base = 1.0')
        return {"FINISHED"}

    def invoke(self, context, event):
        return self.execute(context)


class SNA_OT_Ausexportfbx_C5C51(bpy.types.Operator):
    bl_idname = "sna.ausexportfbx_c5c51"
    bl_label = "aus.exportfbx"
    bl_description = "Export the scene to the set export path, proper export settings are applied."
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        return not False

    def execute(self, context):
        import os
        scene = bpy.context.scene
        projectlen = len(scene['sna_exportpath'].split("\\")[-1])
        project = scene.sna_exportpath
        if scene.sna_exportpath == "F:\Games\Modding\War.uproject":
            self.report({'ERROR'}, "Code stopped, make sure paths are set correctly")
        else: 
            try:
                bpy.context.scene["pskpsaimportpath"]
                if scene.sna_exportpath == "F:\Games\Modding\War.uproject":
                    self.report({'ERROR'}, "Code stopped, make sure paths are set correctly")
                else:
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
            except: 
                scene.sna_final_fbx_path = (project[:-projectlen]+"Content"+"\\"+export)
        if (bpy.context.scene.sna_exportpath == 'F:\Games\Modding\War.uproject'):
            pass
        else:
            bpy.ops.export_scene.fbx('INVOKE_DEFAULT', filepath=bpy.context.scene.sna_final_fbx_path, add_leaf_bones=False, use_armature_deform_only=True)
        return {"FINISHED"}

    def invoke(self, context, event):
        return self.execute(context)


class SNA_OT_Auspakfiles_80B87(bpy.types.Operator):
    bl_idname = "sna.auspakfiles_80b87"
    bl_label = "aus.pakfiles"
    bl_description = "Pack the game files and move them to your game directory. (enable pak chunks if you want to seperate your paks with the chunks you set in engine)"
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        return not False

    def execute(self, context):
        import os
        import glob
        pathlist = []
        uepath = bpy.data.scenes["Scene"].sna_exportpath
        engine_path = bpy.data.scenes["Scene"].sna_unreal_engine_path
        projectlen = len(uepath.split("\\")[-1])
        chunkpath = uepath[:-projectlen] + "Saved\\TmpPackaging\\WindowsNoEditor"
        cookfolder = uepath[:-projectlen] + "Saved\\Cooked\\"
        gamelen = len(bpy.data.scenes["Scene"].sna_game_exe_path.split("\\")[-1])
        gamefolder = bpy.data.scenes["Scene"].sna_game_exe_path[:-gamelen]
        gamefiles = os.path.join(gamefolder, "War\\Content\\Paks")
        sourcefolder = uepath[:-projectlen] + "Saved\\Cooked"
        projectname = uepath.split("\\")[-2]
        number = ("1", "2", "3", "4", "5", "6", "7", "8", "9")
        # for x in uepath.split('\\'):
        #    pathlist.append(x)
        #
        #
        # counter = 0
        ## Checks for spaces in path name, if found replace with a word computers understand
        ## Also re adds the slash which is missing from the drive letter
        ## Old code, but I might want to save it for later
        # for x in pathlist:
        #    if " " in x:
        #        print(pathlist[counter],"isfound")
        #        pathlist[counter] = '"'+x+'"'
        #    if ":" in x:
        #        pathlist[counter] = x+'\\'
        #    counter += 1
        # pathfix = os.path.join(*pathlist).replace("//","\\")
        # Set the export pak of the pak files, instead of them staying in the assets folder, they
        # instead export to the blender exe path
        try:
            # 2.92 and older
            path = bpy.app.binary_path_python
        except AttributeError:
            # 2.93 and later
            import sys
            path = sys.executable
        exportpath = os.path.abspath(path[:-25])

        def packer():
            gamelen = len(bpy.data.scenes["Scene"].sna_game_exe_path.split("\\")[-1])
            bpyfolder = bpy.data.scenes["Scene"].sna_exportpath
            packerpath = os.path.join(os.path.dirname(__file__), "assets", "u4pak.py")
            print("packer here", packerpath)
            modname = "Testmod"
            counter = 0
            # Fix problematic files from packing.
            for folder in os.listdir(sourcefolder):
                print(sourcefolder + "\\" + folder + "\\War")
                if os.path.isdir(exportpath + "\\War"):
                    if os.path.isdir(gamefiles + "\\War"):
                        shutil.rmtree(gamefiles + "\\War")
                    else:
                        pass
                    shutil.move(exportpath + "\\War", gamefiles)
                    shutil.rmtree(gamefiles + "\\War")
                    print("old folder removed")
                else:
                    pass
                # Move the cook folder to the blender directory for packing
                shutil.copytree(
                    sourcefolder + "\\" + folder + "\\" + projectname,
                    exportpath + "\\War",
                    copy_function=shutil.copy,
                )
                print("Cook folder has been moved")
                try:
                    shutil.rmtree(exportpath + "\\War\\Metadata")
                    os.remove(exportpath + "\\War\\AssetRegistry.bin")
                except:
                    pass
                os.system(
                    'python "'
                    + packerpath
                    + '" pack '
                    + "War-WindowsNoEditor_"
                    + modname
                    + str(counter)
                    + ".pak "
                    + "War"
                )
                shutil.move(
                    exportpath + "\\War-WindowsNoEditor_" + modname + str(counter) + ".pak",
                    os.path.join(gamefiles),
                )
                counter += 1
            print("Finished pak")
        # Check game files for old pakfiles and remove them
        for file in os.listdir(gamefiles):
            if file.startswith("War-WindowsNoEditor_Testmod"):
                print(file)
                os.remove(os.path.join(gamefiles, file))
            else:
                print("nope")
        subprocess.run(
            engine_path
            + "\\Engine\\Binaries\\Win64\\UE4Editor-Cmd.exe "
            + '"'
            + uepath
            + '"'
            + " -run=Cook  -TargetPlatform=WindowsNoEditor"
        )
        # Check to see if we want to delete some extra files
        if bpy.data.scenes["Scene"].sna_pak_skeleton_remove == True:
            try:
                os.remove(cookfolder + "WindowsNoEditor\\War\\Content\\Meshes\\Character\\Character_Male_Skeleton.uasset")
                print("Skeleton removed")
                print(cookfolder + "WindowsNoEditor\\War\\Content\\Meshes\\Character\\Character_Male_Skeleton.uasset")
            except:
                print("Skeleton removal failed, no file found")
                print(cookfolder + "WindowsNoEditor\\War\\Content\\Meshes\\Character\\Character_Male_Skeleton.uasset")
        else:
            pass
        print("Removing instance files from "+cookfolder+"\\WindowsNoEditor\\"+"projectname"+"\\**\\*")
        files = glob.glob(cookfolder+"WindowsNoEditor\\"+projectname+"\\**\\*", recursive = True)
        if bpy.data.scenes["Scene"].sna_pak_instance_remove == True:
            for x in files:
                if x.endswith('uasset'):
                    print(os.path.getsize(x))
                    if os.path.getsize(x) < 2000:
                        os.remove(x)
                        print("Removed file"+x+" file too small")
        else: 
            print('No files removed')
        if bpy.data.scenes["Scene"].sna_pak_instance_name == True:
            for x in files:
                if x.endswith('uasset'):
                    print(os.path.getsize(x))
                    if "Instance" in x or "instance" in x:
                        os.remove(x)
                        print("Removed file"+x+" file has instance in name")
                else:
                    print("not found")            
        else:
            print("No files removed")
        # Check if file in the chunk directory ends with a number, if it ends with a number move it to a new folder and run the packer
        if bpy.data.scenes["Scene"].sna_pak_file_toggle == True:
            for file in os.listdir(chunkpath):
                if file.endswith(number, 0, -4):
                    # Using readline()
                    file1 = open(chunkpath + "\\" + file, "r")
                    count = 0
                    while True:
                        count += 1
                        list = []
                        line = file1.readline()
                        # if line is empty
                        # end of file is reached
                        if not line:
                            break
                        list.append(line.split("\\"))
                        length = len(list[0][-1])
                        string = line.strip()[:-length]
                        finalpath = string.replace(
                            "WindowsNoEditor", "WindowsNoEditor" + file[:-4]
                        )
                        destination = (
                            line.replace("WindowsNoEditor", "WindowsNoEditor" + file[:-4])[:-1]
                            + ".uasset"
                        )
                        source = line[:-1] + ".uasset"
                        print(file)
                        if not os.path.isdir(finalpath):
                            os.makedirs(finalpath)
                            print("dirs created")
                        shutil.move(source, destination)
                    file1.close()
                for folder in os.listdir(cookfolder):
                    if bpy.data.scenes["Scene"].sna_pak_skeleton_remove == True:
                        try:
                            os.remove(folder + "\\WindowsNoEditor\\War\\Content\\Meshes\\Character\\Character_Male_Skeleton.uasset")
                            print("Skeleton removed")
                        except:
                            print("Skeleton removal failed, no file found")
                    else:
                        pass
                    print(chunkpath + "\\" + file)
                else:
                    print(file + " doesnt end with number")
            print("finished engine pack")
            # Run the packer
            packer()
            print("packer ran")
        else:
            packer()
        # Remove the old cookfolder in project path
        try:
            shutil.rmtree(cookfolder)
        except:
            print("no old cook")
        return {"FINISHED"}

    def invoke(self, context, event):
        return self.execute(context)


class SNA_OT_Ausfixscale_A8474(bpy.types.Operator):
    bl_idname = "sna.ausfixscale_a8474"
    bl_label = "aus.fixscale"
    bl_description = "Scales the selected object by 100, applies, sets to 0.01"
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        return not False

    def execute(self, context):
        bpy.ops.transform.resize(value=(100, 100, 100))
        bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)
        bpy.ops.transform.resize(value=(0.01, 0.01, 0.01))
        bpy.context.scene.sna_scalecheck = int(bpy.context.scene.sna_scalecheck + 1.0)
        return {"FINISHED"}

    def invoke(self, context, event):
        return context.window_manager.invoke_confirm(self, event)


class SNA_OT_Ausmatimporttxt_C4755(bpy.types.Operator):
    bl_idname = "sna.ausmatimporttxt_c4755"
    bl_label = "aus.matimporttxt"
    bl_description = "Imports the materials prop.txt, based on umodel export path. Import can be found in the text browser"
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        return not False

    def execute(self, context):
        from glob import glob
            #https://b3d.interplanety.org/en/how-to-split-and-join-blender-interface-windows-thruough-the-python-api/
            #https://stackoverflow.com/questions/14798220/how-can-i-search-sub-folders-using-glob-glob-module
        dirpath = bpy.data.scenes["Scene"].sna_umodel_exportpath
        matname = bpy.context.active_object.material_slots[0].name+'.props.txt'
        blendpath = bpy.data.filepath
        #if bpy.context.screen.show_fullscreen == False:                                 # Throw report if the user is in fullscreen mode (can't split window if in fullscreen)
            #for path in glob(dirpath, recursive=True):
        for matslots in bpy.data.materials:                          # Get the name of every material on selected object, search for it in exported file
            for file in glob(dirpath+'/**/*'+matslots.name+'.props.txt',recursive=True):
                bpy.ops.text.open(filepath=file)
                print(file)
            print(matslots.name)
        #else: 
        #    self.report({'INFO'}, 'Please leave fullscreen mode (shift spacebar)')
        #if bpy.context.screen.show_fullscreen == False:
        #    if bpy.context.screen.areas[0].type == "TEXT_EDITOR":
        #        pass
        #    else:                                                                       # Split window and newly created text editor to view the last imported file.
        #        bpy.ops.screen.area_split(direction='VERTICAL', factor=0.75)
        #        bpy.context.screen.areas[-1].type = "TEXT_EDITOR"
        #        
        #        text = bpy.data.texts[-1]
        #        for area in bpy.context.screen.areas:
        #            if area.type == 'TEXT_EDITOR':
        #                area.spaces[0].text = text
        #else: 
        #    self.report({'INFO'}, 'Please leave fullscreen mode (shift spacebar)')
        #bpy.ops.wm.save_as_mainfile(filepath=bpy.data.filepath)
        #print('files imported')
        return {"FINISHED"}

    def invoke(self, context, event):
        return self.execute(context)


class SNA_OT_Austestmodbat_B95Ae(bpy.types.Operator):
    bl_idname = "sna.austestmodbat_b95ae"
    bl_label = "aus.testmodbat"
    bl_description = ""
    bl_options = {"REGISTER", "UNDO"}
    sna_fileindex: bpy.props.StringProperty(name='fileindex', description='', default='', subtype='NONE', maxlen=0)

    @classmethod
    def poll(cls, context):
        return not False

    def execute(self, context):
        import glob
        batpath = bpy.data.scenes["Scene"].sna_batfilepath
        buttonindex = bpy.data.scenes["Scene"].sna_fileindex_public -1 
        indexlist = []
        for x in glob.glob(batpath+"/*.*", recursive=False):
            print(x)
            indexlist.append(x)
        os.startfile(indexlist[buttonindex])
        bpy.context.scene.sna_fileindex_public = string_to_type(self.sna_fileindex, int, 0)
        print('')
        return {"FINISHED"}

    def invoke(self, context, event):
        return self.execute(context)


class SNA_OT_Auslaunchproject_41F46(bpy.types.Operator):
    bl_idname = "sna.auslaunchproject_41f46"
    bl_label = "aus.launchproject"
    bl_description = "Launches the Uproject set in the paths secoin"
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        return not False

    def execute(self, context):
        import os 
        engine_path = bpy.context.scene.sna_exportpath

        defaultpath = ".uproject"
        if engine_path == defaultpath:
            self.report({'ERROR'}, "uproject path not set, make sure paths are set correctly")
        else:
            os.system(engine_path)
        return {"FINISHED"}

    def invoke(self, context, event):
        return self.execute(context)


class SNA_OT_Ausopenprojectfolder_592Ee(bpy.types.Operator):
    bl_idname = "sna.ausopenprojectfolder_592ee"
    bl_label = "aus.openprojectfolder"
    bl_description = ""
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        return not False

    def execute(self, context):
        import os
        projectpath = bpy.context.scene.sna_exportpath
        projectlen = len(projectpath.split('\\')[-1])
        open = 'start '+projectpath[:-projectlen]+'\\content'
        list = []
        os.system(open)
        print(open)
        return {"FINISHED"}

    def invoke(self, context, event):
        return self.execute(context)


class SNA_OT_Ausassignmaterial_Dcea2(bpy.types.Operator):
    bl_idname = "sna.ausassignmaterial_dcea2"
    bl_label = "aus.assignmaterial"
    bl_description = "Imports the textures for the currently selected object/material"
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        return not False

    def execute(self, context):
        from glob import glob
        ### TO DO: ###
        #Get a check for noise mask on import, the line doesn't have a space after the ', so the period isn't there.
        # Did I just fix that lmao?
        dirpath = bpy.data.scenes["Scene"].sna_umodel_exportpath
        matname = bpy.context.object.active_material.name+'.props.txt'
        matnamefull = bpy.context.object.active_material.name_full
        bpy.data.materials[matnamefull].use_nodes = True
        mat = bpy.context.object.active_material
        matlinks = bpy.context.object.active_material.node_tree.links
        nodelist = []
        wordlist = []
        # Remove nodes encase there is left over data for what ever reason.
        for x in mat.node_tree.nodes:
            mat.node_tree.nodes.remove(mat.node_tree.nodes[x.name])
        mat.node_tree.nodes.new('ShaderNodeOutputMaterial')
        mat.node_tree.nodes.new('ShaderNodeBsdfPrincipled')
        # Check if the Foxhole node group is present in the blend file, if not, import from assets folder.
        matoutput = bpy.context.object.active_material.node_tree.nodes['Material Output']
        for group in bpy.data.node_groups:
            nodelist.append(group.name)
        if 'Foxhole' in nodelist:
            print('Foxhole Node group found')
            mat.node_tree.nodes.remove(mat.node_tree.nodes['Principled BSDF'])
            group = mat.node_tree.nodes.new("ShaderNodeGroup")
            group.node_tree = bpy.data.node_groups['Foxhole']
            matlinks.new(bpy.context.object.active_material.node_tree.nodes[1].outputs[0], matoutput.inputs[0])
        else:
            print('Foxhole Node group not found, importing...')
            mat.node_tree.nodes.remove(mat.node_tree.nodes['Principled BSDF'])
            bpy.context.scene.sna_nodegroup_check = 1
            before_data = list(bpy.data.node_groups)
            bpy.ops.wm.link(directory=os.path.join(os.path.dirname(__file__), 'assets', 'Foxhole_Library.blend') + r'\NodeTree', filename='Foxhole', link=True, instance_object_data=True)
            new_data = list(filter(lambda d: not d in before_data, list(bpy.data.node_groups)))
            appended_525CF = None if not new_data else new_data[0]
            group = mat.node_tree.nodes.new("ShaderNodeGroup")
            group.node_tree = bpy.data.node_groups['Foxhole']
            matlinks.new(bpy.context.object.active_material.node_tree.nodes[1].outputs[0], matoutput.inputs[0])
        try: 
            bpy.data.texts[matnamefull].name_full
            print('Props.txt found, skipping import')
        except:
                #https://b3d.interplanety.org/en/how-to-split-and-join-blender-interface-windows-thruough-the-python-api/
                #https://stackoverflow.com/questions/14798220/how-can-i-search-sub-folders-using-glob-glob-module                           
        # Get the name of active material, search for it in exported files (based on Umodel export path)
            for file in glob(dirpath+'/**/*'+mat.name+'.props.txt',recursive=True):
                bpy.ops.text.open(filepath=file)
                print('it should import',file)
                bpy.ops.file.make_paths_absolute()
        txtfile = bpy.data.texts[matname].filepath
        linenumber = 0
        with open(txtfile, 'r') as file:
                content = file.readlines()
                for lines in content:
                    #if "ParameterValue = Texture2D'/War/Content/Textures" in lines:
                    if "ParameterValue = Texture2D'/War/Content/Textures" in lines: #/War/Content/Textures
                        wordlist.append(linenumber)
                        test = lines.split('.')
                    if "ParameterValue = Texture2D'/War/Content/Blueprint" in lines:
                        wordlist.append(linenumber)
                        test = lines.split('.')
                    else:
                        pass
                    linenumber += 1
        listcounter = 0
        print(wordlist[listcounter])
        namelen = len(bpy.context.object.active_material.name)
        texlines = []
        nodes = [bpy.context.object.active_material.node_tree.nodes]
        imgnode = 2
        # Handles the node creation and linking
        for text in wordlist:
            print('Line index -1',test)
            texpath = content[text].replace("ParameterValue = Texture2D'/War/Content/", "", text).strip(' ')
            image = ((texpath.split('.')[-1][:-2]))
            filepath = (dirpath+texpath.split(image)[0].replace("/", "\\")+image+".png")
            mat = bpy.context.object.active_material
            matlinks = bpy.context.object.active_material.node_tree.links
            imagefix = (image+'.png')
            bpy.context.object.active_material.node_tree.nodes.new('ShaderNodeTexImage')
            bpy.ops.image.open(filepath=filepath)
            bpy.context.object.material_slots[mat.name_full].material.node_tree.nodes[imgnode].image = bpy.data.images[imagefix]
            imgnode += 1
            print(imgnode,'imgnodeprint')
        nodecount = 2
        for x in wordlist:
            Imgtex1 = bpy.context.object.active_material.node_tree.nodes[nodecount]
            foxhole = bpy.context.object.active_material.node_tree.nodes['Group']
            matlinks = bpy.context.object.active_material.node_tree.links
            print(nodes)
            img = bpy.context.object.active_material.node_tree.nodes[nodecount].image.name_full
            print(f"WORKING WITH: {mat.node_tree.nodes[nodecount].image.name}")
            if mat.node_tree.nodes[nodecount].image.name.split(".")[0].lower().endswith("a"):
                matlinks.new(bpy.context.object.active_material.node_tree.nodes[nodecount].outputs[0], foxhole.inputs[0])
                print(nodecount,'A')
            elif mat.node_tree.nodes[nodecount].image.name.split(".")[0].lower().endswith("m"):
                matlinks.new(bpy.context.object.active_material.node_tree.nodes[nodecount].outputs[0], foxhole.inputs[1])
                bpy.data.images[img].colorspace_settings.name = 'Non-Color'
                print(nodecount,'M')
            elif mat.node_tree.nodes[nodecount].image.name.split(".")[0].lower().endswith("n"):
                matlinks.new(bpy.context.object.active_material.node_tree.nodes[nodecount].outputs[0], foxhole.inputs[4])
                bpy.data.images[img].colorspace_settings.name = 'Non-Color'
                print(nodecount,'N')
            else:
                print('finished')
                print(nodecount)
            nodecount += 1
        ### Cleans out any text file whos suffix matches 0-9, used to clear extra text imports  ###    
        #dupe = ["0","1","2","3","4","5","6","7","8","9"]
        #for text in bpy.data.texts:
        #    if(any([(text.name).endswith(n) for n in dupe])):
        #        print("Duplicate found: ",text.name," Deleting...")
        #        bpy.data.texts[text.name_full].user_clear()
        #    else: 
        #        print("Keeping file ",text.name)
        #    self.report({'WARNING'}, 'Please save and re-open the blend file')
        return {"FINISHED"}

    def invoke(self, context, event):
        return self.execute(context)


class SNA_PT_FOXHOLE_PATHS_6B807(bpy.types.Panel):
    bl_label = 'Foxhole Paths'
    bl_idname = 'SNA_PT_FOXHOLE_PATHS_6B807'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_context = ''
    bl_order = 0
    bl_options = {'DEFAULT_CLOSED'}
    bl_parent_id = 'SNA_PT_FOXHOLE_TOOLS_DCC57'
    bl_ui_units_x=0

    @classmethod
    def poll(cls, context):
        return not (False)

    def draw_header(self, context):
        layout = self.layout

    def draw(self, context):
        layout = self.layout
        box_C89CE = layout.box()
        box_C89CE.alert = False
        box_C89CE.enabled = True
        box_C89CE.active = True
        box_C89CE.use_property_split = True
        box_C89CE.use_property_decorate = False
        box_C89CE.alignment = 'Expand'.upper()
        box_C89CE.scale_x = 1.0
        box_C89CE.scale_y = 1.0
        box_C89CE.operator_context = "INVOKE_DEFAULT" if True else "EXEC_DEFAULT"
        box_C89CE.prop(bpy.context.scene, 'sna_exportpath', text='Uproject Path', icon_value=0, emboss=True)
        box_C89CE.prop(bpy.context.scene, 'sna_batfilepath', text='Bat file path', icon_value=0, emboss=True)
        box_C89CE.prop(bpy.context.scene, 'sna_umodel_exportpath', text='Umodel Export', icon_value=0, emboss=True)
        box_C89CE.prop(bpy.context.scene, 'sna_game_exe_path', text='Game executable', icon_value=0, emboss=True)
        box_C89CE.prop(bpy.context.scene, 'sna_unreal_engine_path', text='UE engine path', icon_value=0, emboss=True)


class SNA_PT_FOXHOLE_TOOLS_91868(bpy.types.Panel):
    bl_label = 'Foxhole Tools'
    bl_idname = 'SNA_PT_FOXHOLE_TOOLS_91868'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_context = ''
    bl_order = 0
    bl_options = {'DEFAULT_CLOSED'}
    bl_parent_id = 'SNA_PT_FOXHOLE_TOOLS_DCC57'
    bl_ui_units_x=0

    @classmethod
    def poll(cls, context):
        return not (False)

    def draw_header(self, context):
        layout = self.layout

    def draw(self, context):
        layout = self.layout
        layout.label(text='Misc', icon_value=230)
        box_8EA46 = layout.box()
        box_8EA46.alert = False
        box_8EA46.enabled = True
        box_8EA46.active = True
        box_8EA46.use_property_split = False
        box_8EA46.use_property_decorate = False
        box_8EA46.alignment = 'Expand'.upper()
        box_8EA46.scale_x = 1.0
        box_8EA46.scale_y = 1.0
        box_8EA46.operator_context = "INVOKE_DEFAULT" if True else "EXEC_DEFAULT"
        col_A9246 = box_8EA46.column(heading='', align=False)
        col_A9246.alert = False
        col_A9246.enabled = True
        col_A9246.active = True
        col_A9246.use_property_split = False
        col_A9246.use_property_decorate = False
        col_A9246.scale_x = 1.0
        col_A9246.scale_y = 1.0
        col_A9246.alignment = 'Expand'.upper()
        col_A9246.operator_context = "INVOKE_DEFAULT" if True else "EXEC_DEFAULT"
        op = col_A9246.operator('sna.ausfixscale_a8474', text='Fix Scale', icon_value=618, emboss=True, depress=False)
        op = col_A9246.operator('sna.ausassignmaterial_dcea2', text='Import Textures', icon_value=79, emboss=True, depress=False)


class SNA_PT_EXPORTING_9A43F(bpy.types.Panel):
    bl_label = 'Exporting'
    bl_idname = 'SNA_PT_EXPORTING_9A43F'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_context = ''
    bl_order = 0
    bl_options = {'DEFAULT_CLOSED'}
    bl_parent_id = 'SNA_PT_FOXHOLE_TOOLS_DCC57'
    bl_ui_units_x=0

    @classmethod
    def poll(cls, context):
        return not (False)

    def draw_header(self, context):
        layout = self.layout

    def draw(self, context):
        layout = self.layout
        box_4B114 = layout.box()
        box_4B114.alert = False
        box_4B114.enabled = True
        box_4B114.active = True
        box_4B114.use_property_split = False
        box_4B114.use_property_decorate = False
        box_4B114.alignment = 'Expand'.upper()
        box_4B114.scale_x = 1.0
        box_4B114.scale_y = 1.0
        box_4B114.operator_context = "INVOKE_DEFAULT" if True else "EXEC_DEFAULT"
        box_4B114.label(text='Export tools', icon_value=0)
        op = box_4B114.operator('sna.ausexportfbx_c5c51', text='Export FBX ->', icon_value=0, emboss=True, depress=False)


class SNA_PT_OTHER_TOOLS_FCD44(bpy.types.Panel):
    bl_label = 'Other Tools'
    bl_idname = 'SNA_PT_OTHER_TOOLS_FCD44'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_context = ''
    bl_order = 0
    bl_options = {'DEFAULT_CLOSED'}
    bl_parent_id = 'SNA_PT_FOXHOLE_TOOLS_DCC57'
    bl_ui_units_x=0

    @classmethod
    def poll(cls, context):
        return not (False)

    def draw_header(self, context):
        layout = self.layout

    def draw(self, context):
        layout = self.layout
        box_918B7 = layout.box()
        box_918B7.alert = False
        box_918B7.enabled = True
        box_918B7.active = True
        box_918B7.use_property_split = False
        box_918B7.use_property_decorate = False
        box_918B7.alignment = 'Expand'.upper()
        box_918B7.scale_x = 1.0
        box_918B7.scale_y = 1.0
        box_918B7.operator_context = "INVOKE_DEFAULT" if True else "EXEC_DEFAULT"
        box_918B7.label(text='Engine tools', icon_value=0)
        op = box_918B7.operator('sna.auslaunchproject_41f46', text='Launch engine', icon_value=0, emboss=True, depress=False)
        op = box_918B7.operator('sna.ausopenprojectfolder_592ee', text='Open project folder', icon_value=0, emboss=True, depress=False)
        col_8DD56 = box_918B7.column(heading='', align=False)
        col_8DD56.alert = False
        col_8DD56.enabled = True
        col_8DD56.active = True
        col_8DD56.use_property_split = False
        col_8DD56.use_property_decorate = False
        col_8DD56.scale_x = 1.0
        col_8DD56.scale_y = 1.0
        col_8DD56.alignment = 'Expand'.upper()
        col_8DD56.operator_context = "INVOKE_DEFAULT" if True else "EXEC_DEFAULT"
        col_8DD56.prop(bpy.context.scene, 'sna_pak_file_toggle', text='Pak using chunks', icon_value=0, emboss=True)
        col_00ED5 = col_8DD56.column(heading='', align=False)
        col_00ED5.alert = False
        col_00ED5.enabled = True
        col_00ED5.active = True
        col_00ED5.use_property_split = False
        col_00ED5.use_property_decorate = False
        col_00ED5.scale_x = 1.0
        col_00ED5.scale_y = 1.0
        col_00ED5.alignment = 'Expand'.upper()
        col_00ED5.operator_context = "INVOKE_DEFAULT" if True else "EXEC_DEFAULT"
        col_00ED5.prop(bpy.context.scene, 'sna_pak_skeleton_remove', text='Remove skeleton', icon_value=0, emboss=True)
        col_00ED5.prop(bpy.context.scene, 'sna_pak_instance_remove', text='Remove instances using size', icon_value=0, emboss=True)
        col_00ED5.prop(bpy.context.scene, 'sna_pak_instance_name', text='Remove Instances using name', icon_value=0, emboss=True)
        op = col_8DD56.operator('sna.auspakfiles_80b87', text='Pak game files', icon_value=0, emboss=True, depress=False)
        box_918B7.label(text='Bat Files', icon_value=0)
        if 'F:\Games\Modding\Foxhole' in bpy.context.scene.sna_batfilepath:
            box_918B7.label(text='No bat files found', icon_value=0)
        else:
            col_3DAF3 = box_918B7.column(heading='', align=False)
            col_3DAF3.alert = False
            col_3DAF3.enabled = True
            col_3DAF3.active = True
            col_3DAF3.use_property_split = False
            col_3DAF3.use_property_decorate = False
            col_3DAF3.scale_x = 1.0
            col_3DAF3.scale_y = 1.0
            col_3DAF3.alignment = 'Expand'.upper()
            col_3DAF3.operator_context = "INVOKE_DEFAULT" if True else "EXEC_DEFAULT"
            for i_1FC86 in range(len([f for f in os.listdir(bpy.context.scene.sna_batfilepath) if os.path.isfile(os.path.join(bpy.context.scene.sna_batfilepath, f))])):
                if '.bat' in [f for f in os.listdir(bpy.context.scene.sna_batfilepath) if os.path.isfile(os.path.join(bpy.context.scene.sna_batfilepath, f))][i_1FC86]:
                    op = col_3DAF3.operator('sna.austestmodbat_b95ae', text=[f for f in os.listdir(bpy.context.scene.sna_batfilepath) if os.path.isfile(os.path.join(bpy.context.scene.sna_batfilepath, f))][i_1FC86], icon_value=0, emboss=True, depress=False)
                    op.sna_fileindex = str(i_1FC86)


def register():
    global _icons
    _icons = bpy.utils.previews.new()
    bpy.types.Scene.sna_exportpath = bpy.props.StringProperty(name='exportpath', description='', default='F:\Games\Modding\War.uproject', subtype='FILE_PATH', maxlen=0)
    bpy.types.Scene.sna_scalecheck = bpy.props.IntProperty(name='scalecheck', description='', default=1, subtype='NONE')
    bpy.types.Scene.sna_batfilepath = bpy.props.StringProperty(name='batfilepath', description='', default='F:\\Games\\Modding\\Foxhole-Automation-Scripts-master\\', subtype='DIR_PATH', maxlen=0)
    bpy.types.Scene.sna_fileindex_public = bpy.props.IntProperty(name='fileindex_public', description='', default=0, subtype='NONE')
    bpy.types.Scene.sna_umodel_exportpath = bpy.props.StringProperty(name='Umodel_exportpath', description='', default='F:\\Games\\Modding\\umodel_win32\\UmodelExport\\', subtype='DIR_PATH', maxlen=0)
    bpy.types.Scene.sna_nodegroup_check = bpy.props.IntProperty(name='nodegroup_check', description='', default=0, subtype='NONE')
    bpy.types.Scene.sna_final_fbx_path = bpy.props.StringProperty(name='final_fbx_path', description='', default='C:\\', subtype='NONE', maxlen=0)
    bpy.types.Scene.sna_game_exe_path = bpy.props.StringProperty(name='game_exe_path', description='', default='C:\Program Files (x86)\Steam\steamapps\common\Foxhole\War.exe', subtype='FILE_PATH', maxlen=0)
    bpy.types.Scene.sna_unreal_engine_path = bpy.props.StringProperty(name='unreal_engine_path', description='', default='F:\\Games\\epic\\UE_4.24', subtype='DIR_PATH', maxlen=0)
    bpy.types.Scene.sna_pak_file_toggle = bpy.props.BoolProperty(name='pak_file_toggle', description='Pack the mod files using chunks you assigned in engine', default=False)
    bpy.types.Scene.sna_pak_instance_remove = bpy.props.BoolProperty(name='pak_instance_remove', description='Removed uasssets based on file size (File size is smaller than 2.5kb)', default=False)
    bpy.types.Scene.sna_pak_skeleton_remove = bpy.props.BoolProperty(name='pak_skeleton_remove', description='Remove the skeleton in "\Meshes\Character\Character_Male_Skeleton"', default=False)
    bpy.types.Scene.sna_pak_instance_name = bpy.props.BoolProperty(name='pak_instance_name', description='Removed the uassets files if "Instance" is found in its file name', default=False)
    bpy.utils.register_class(SNA_PT_FOXHOLE_TOOLS_DCC57)
    bpy.utils.register_class(SNA_OT_Ausfixunitscale_5Db26)
    bpy.utils.register_class(SNA_OT_Ausfixframerate_19B08)
    bpy.utils.register_class(SNA_OT_Ausexportfbx_C5C51)
    bpy.utils.register_class(SNA_OT_Auspakfiles_80B87)
    bpy.utils.register_class(SNA_OT_Ausfixscale_A8474)
    bpy.utils.register_class(SNA_OT_Ausmatimporttxt_C4755)
    bpy.utils.register_class(SNA_OT_Austestmodbat_B95Ae)
    bpy.utils.register_class(SNA_OT_Auslaunchproject_41F46)
    bpy.utils.register_class(SNA_OT_Ausopenprojectfolder_592Ee)
    bpy.utils.register_class(SNA_OT_Ausassignmaterial_Dcea2)
    bpy.utils.register_class(SNA_PT_FOXHOLE_PATHS_6B807)
    bpy.utils.register_class(SNA_PT_FOXHOLE_TOOLS_91868)
    bpy.utils.register_class(SNA_PT_EXPORTING_9A43F)
    bpy.utils.register_class(SNA_PT_OTHER_TOOLS_FCD44)


def unregister():
    global _icons
    bpy.utils.previews.remove(_icons)
    wm = bpy.context.window_manager
    kc = wm.keyconfigs.addon
    for km, kmi in addon_keymaps.values():
        km.keymap_items.remove(kmi)
    addon_keymaps.clear()
    del bpy.types.Scene.sna_pak_instance_name
    del bpy.types.Scene.sna_pak_skeleton_remove
    del bpy.types.Scene.sna_pak_instance_remove
    del bpy.types.Scene.sna_pak_file_toggle
    del bpy.types.Scene.sna_unreal_engine_path
    del bpy.types.Scene.sna_game_exe_path
    del bpy.types.Scene.sna_final_fbx_path
    del bpy.types.Scene.sna_nodegroup_check
    del bpy.types.Scene.sna_umodel_exportpath
    del bpy.types.Scene.sna_fileindex_public
    del bpy.types.Scene.sna_batfilepath
    del bpy.types.Scene.sna_scalecheck
    del bpy.types.Scene.sna_exportpath
    bpy.utils.unregister_class(SNA_PT_FOXHOLE_TOOLS_DCC57)
    bpy.utils.unregister_class(SNA_OT_Ausfixunitscale_5Db26)
    bpy.utils.unregister_class(SNA_OT_Ausfixframerate_19B08)
    bpy.utils.unregister_class(SNA_OT_Ausexportfbx_C5C51)
    bpy.utils.unregister_class(SNA_OT_Auspakfiles_80B87)
    bpy.utils.unregister_class(SNA_OT_Ausfixscale_A8474)
    bpy.utils.unregister_class(SNA_OT_Ausmatimporttxt_C4755)
    bpy.utils.unregister_class(SNA_OT_Austestmodbat_B95Ae)
    bpy.utils.unregister_class(SNA_OT_Auslaunchproject_41F46)
    bpy.utils.unregister_class(SNA_OT_Ausopenprojectfolder_592Ee)
    bpy.utils.unregister_class(SNA_OT_Ausassignmaterial_Dcea2)
    bpy.utils.unregister_class(SNA_PT_FOXHOLE_PATHS_6B807)
    bpy.utils.unregister_class(SNA_PT_FOXHOLE_TOOLS_91868)
    bpy.utils.unregister_class(SNA_PT_EXPORTING_9A43F)
    bpy.utils.unregister_class(SNA_PT_OTHER_TOOLS_FCD44)
