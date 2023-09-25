import bpy
import math


# removing the default cube
bpy.data.objects.remove(bpy.data.objects["Cube"])

# creating arbitrary primitives
bpy.ops.mesh.primitive_cube_add(
    location=(1, 2.5, 1),
    size=1,
)
bpy.ops.mesh.primitive_ico_sphere_add(location=(0, 0, 0))
bpy.ops.mesh.primitive_cone_add(
    location=(-1, -2.5, -1),
    depth=1,
    radius1=0.5,
)
bpy.ops.mesh.primitive_torus_add(
    location=(0, 0, 0),
    rotation=(math.radians(25), math.radians(25), math.radians(75)),
    major_radius=2.5,
    minor_radius=0.4,
    major_segments=256,
    minor_segments=256,
)
bpy.ops.mesh.primitive_plane_add(
    location=(0, 0, -2),
    size=20,
)

# Apply matrial to the Cube
mat_reddish = bpy.data.materials.new('Reddish')
mat_reddish.diffuse_color = (1.0, 0.151, 0.132, 1.0)
bpy.data.objects["Cube"].data.materials.append(mat_reddish)

# Apply matrial to the Cone
mat_blueish = bpy.data.materials.new('Blueish')
mat_blueish.diffuse_color = (0.090, 0.422, 1.0, 1.0)
bpy.data.objects["Cone"].data.materials.append(mat_blueish)

# Apply matrial to the Icosphere
mat_choko = bpy.data.materials.new('Chokolatey')
mat_choko.diffuse_color = (0.311, 0.061, 0., 1.0)
bpy.data.objects["Icosphere"].data.materials.append(mat_choko)

# Apply matrial to the Torus
mat_rubbery = bpy.data.materials.new('Rubbery')
mat_rubbery.diffuse_color = (0.05, 0.05, 0.05, 1.0)
mat_rubbery.roughness = 0.35
mat_rubbery.specular_intensity = 1.0
bpy.data.objects["Torus"].data.materials.append(mat_rubbery)

# Apply matrial to the Plane
mat_greenish = bpy.data.materials.new('Greenish')
mat_greenish.diffuse_color = (0.029, 0.8, 0.048, 1.0)
bpy.data.objects["Plane"].data.materials.append(mat_greenish)

# change position and brightness of the default Light
bpy.data.objects["Light"].location = (10., -7.5, 10.)
bpy.data.lights["Light"].energy = 3000.

# Create a new light type
light_wide = bpy.data.lights.new(name="Backlight_Wide", type='SPOT')
light_wide.energy = 10000.0
light_wide.spot_size = math.radians(50)

# Create a spotlight object
backlight_r = bpy.data.objects.new(name="Backlight_R", object_data=light_wide)
backlight_r.location = (-2.0, 8.0, -0.5)
backlight_r.rotation_euler = (
    math.radians(-97), math.radians(12), math.radians(15))

# Link the spotlight object to the active scene
bpy.context.collection.objects.link(backlight_r)

# Create another light type
light_narrow = bpy.data.lights.new(name="Backlight_Narrow", type='SPOT')
light_narrow.energy = 10000.0
light_narrow.spot_size = math.radians(35)

# Create another spotlight object
backlight_l = bpy.data.objects.new(
    name="Backlight_L", object_data=light_narrow)
backlight_l.location = (-6.5, -9.5, 7)
backlight_l.rotation_euler = (
    math.radians(42.4), math.radians(-47), math.radians(4.81))

bpy.context.collection.objects.link(backlight_l)
