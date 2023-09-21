from pathlib import Path
import subprocess
import sys


def test_1(
    blender_path: str | None = None,
    output_path: str | None = None,
    x_resolution: int | None = None,
    y_resolution: int | None = None,
):
    script_path = Path(__file__).parent.joinpath('blender_scenario_1.py')
    subprocess.call(f'"{blender_path}" -b -P "{script_path}"')


if False:
    blender_path = Path(
        "D:/Workfolder/Workfolder_Coding/Blender testing 1/blender-engine/blender.exe")
    script_path = Path(__file__).parent.joinpath('blender_scenario_1.py')
    output_path = Path(__file__).parent.joinpath('test_')
    command = f'"{blender_path}" -b -P "{script_path}" -o "{output_path}" -f +0'
    print(str(command))


test_1(
    blender_path=Path(
        "D:/Workfolder/Workfolder_Coding/Blender testing 1/blender-engine/blender.exe"
    ),
    output_path=Path(__file__).parent.joinpath('test_'),
    x_resolution=1920,
    y_resolution=1080,
)
