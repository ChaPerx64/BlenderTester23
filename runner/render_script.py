# this code will be appended to a temporary script where
# variables OUTPUT_PATH, X_RESOLUTION, Y_RESOLUTION will be defined

import bpy
import os

render = bpy.data.scenes["Scene"].render
render.filepath = os.environ['OUTPUT_PATH']
render.resolution_x = int(os.environ['X_RESOLUTION'])
render.resolution_y = int(os.environ['Y_RESOLUTION'])
bpy.ops.render.render(write_still=True)
