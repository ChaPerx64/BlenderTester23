from pathlib import Path
import subprocess
import tempfile
import os


RENDER_TEMPLATE_PATH = Path(__file__).parent / 'render_template.py'


def run_scenario(
    x_resolution: str,
    y_resolution: str,
    output_path: str,
    blender_path: str,
    scenario: dict,
):
    scenario_path = scenario['scenario_path']

    # creating output paths
    render_output_path = Path(output_path) / 'image'
    log_output_path = Path(output_path) / 'render.log'

    # creating a temporary blender script from a script template
    print('Creating a temporary script...')
    render_script = tempfile.NamedTemporaryFile(mode='w+', delete=False)
    render_script.write(f'OUTPUT_PATH=r"{render_output_path}"\n')
    render_script.write(f'X_RESOLUTION={x_resolution}\n')
    render_script.write(f'Y_RESOLUTION={y_resolution}\n')
    with open(RENDER_TEMPLATE_PATH, mode='r') as f:
        render_script.writelines(f)
    render_script.close()

    # calling blender in a subprocess
    print('Calling Blender...')
    with open(log_output_path, mode='w') as logfile:
        subprocess.run(
            f'"{blender_path}" -b -P "{scenario_path}" -P "{render_script.name}"',
            stderr=logfile,
            stdout=logfile,
        )

    # deleteing the temporary file
    print('Removing temporary files...')
    os.remove(render_script.name)
