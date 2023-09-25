from pathlib import Path
import subprocess
import tempfile
import os


RENDER_TEMPLATE_PATH = Path(__file__).parent / 'render_template.py'
SCENARIO_DIR_PATH = Path().cwd() / 'scenarios'


def run_scenario(
    x_resolution: str,
    y_resolution: str,
    output_path: str,
    blender_path: str,
    scenario_path: str,
):

    # creating output paths
    render_output_path = Path(output_path) / scenario_path / 'image'
    log_output_path = Path(output_path) / scenario_path / 'render.log'

    # scenario_path = scenario['scenario_path']
    scenario_path = f"{SCENARIO_DIR_PATH / scenario_path}.py"

    # creating a temporary blender script from a script template
    print('\nCreating a temporary script...')
    render_script = tempfile.NamedTemporaryFile(mode='w+', delete=False)
    render_script.write(f'OUTPUT_PATH=r"{render_output_path}"\n')
    render_script.write(f'X_RESOLUTION={x_resolution}\n')
    render_script.write(f'Y_RESOLUTION={y_resolution}\n')
    with open(RENDER_TEMPLATE_PATH, mode='r') as f:
        render_script.writelines(f)
    render_script.close()

    # calling blender in a subprocess
    print('Calling Blender...')
    completed_process = subprocess.run(
        [blender_path, "-b", "-P", scenario_path, "-P", render_script.name],
        text=True,
        stderr=subprocess.STDOUT,
        stdout=subprocess.PIPE,
    )

    # writing render log
    print('Writing render log...')
    with open(log_output_path, mode='w+') as logfile:
        logfile.writelines(completed_process.stdout)

    # deleteing the temporary file
    print('Removing temporary files...')
    os.remove(render_script.name)

    return completed_process
