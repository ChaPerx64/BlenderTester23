import bpy
import math
from pathlib import Path


def create_objects():
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


def render_image(
        out_path: str | Path,
        x_resolution: int,
        y_resolution: int,
):
    out_path = Path(out_path)
    if not out_path.is_file:
        raise FileNotFoundError('Incorrect input: out_path is not a filepath')
    render = bpy.data.scenes["Scene"].render
    render.filepath = str(out_path)
    print(f"Image should be saved here: {out_path}")
    render.resolution_x = int(x_resolution)
    render.resolution_y = int(y_resolution)
    bpy.ops.render.render(write_still=True)


bpy.data.objects.remove(bpy.data.objects["Cube"])
create_objects()

# append file with the following before sending it to Blender
#
render_image(
    Path("D:/Workfolder/Workfolder_Coding/Blender testing 1/tests/test_1/img"),
    1920,
    1080,
)
