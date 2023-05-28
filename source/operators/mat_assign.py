import bpy
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
    bpy.ops.wm.append(directory=os.path.join(os.path.dirname(__file__), 'assets', 'Foxhole_Library.blend') + r'\NodeTree', filename='Foxhole', link=False)
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
        content = list(map(lambda x: x.replace("ParameterValue = Texture2D'/War/Content/", "ParameterValue = Texture2D'"), file.readlines()))
        for lines in content:
            if "ParameterValue = Texture2D'Textures" in lines:
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
    texpath = content[text].replace("ParameterValue = Texture2D'", "", text).strip(' ')
    image = ((texpath.split('.')[-1][:-2]))
    filepath = (dirpath+texpath.split(image)[0].replace("/", "\\")+image+".tga")
    mat = bpy.context.object.active_material
    matlinks = bpy.context.object.active_material.node_tree.links
    imagefix = (image+'.tga')


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
