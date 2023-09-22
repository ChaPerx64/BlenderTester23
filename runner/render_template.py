import bpy


render = bpy.data.scenes["Scene"].render
render.filepath = OUTPUT_PATH
render.resolution_x = X_RESOLUTION
render.resolution_y = Y_RESOLUTION
bpy.ops.render.render(write_still=True)
