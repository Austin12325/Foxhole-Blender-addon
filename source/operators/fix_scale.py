import bpy
    bpy.ops.transform.resize(value=(100, 100, 100))
    bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)
    bpy.ops.transform.resize(value=(0.01, 0.01, 0.01))
