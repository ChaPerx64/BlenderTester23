# this code will be appended to a temporary script where
# variables OUTPUT_PATH, X_RESOLUTION, Y_RESOLUTION will be defined

import bpy

bpy.context.scene.render.engine = 'CYCLES'
render = bpy.data.scenes["Scene"].render
render.filepath = OUTPUT_PATH
render.resolution_x = X_RESOLUTION
render.resolution_y = Y_RESOLUTION
bpy.ops.render.render(write_still=True)
