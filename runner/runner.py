from pathlib import Path
import subprocess
import tempfile
import os
import logging
from datetime import datetime


RENDER_SCRIPT_PATH = Path(__file__).parent / 'render_template.py'
SCENARIO_DIR_PATH = Path().cwd() / 'scenarios'

logger = logging.getLogger(__name__)


def run_scenario(
    x_resolution: str,
    y_resolution: str,
    output_path: str,
    blender_path: str,
    scenario_path: str,
):
    output_dir = Path(output_path) / scenario_path
    output_dir.mkdir(parents=True, exist_ok=True)

    # creating output paths
    render_output_path = output_dir / 'image'

    # scenario_path = scenario['scenario_path']
    scenario_path = f"{SCENARIO_DIR_PATH / scenario_path}.py"

    # setting environment variables that render_script will use
    os.environ['X_RESOLUTION'] = x_resolution
    os.environ['Y_RESOLUTION'] = y_resolution
    os.environ['OUTPUT_PATH'] = str(render_output_path)

    # calling Blender in a subprocess
    print('Calling Blender...')
    completed_process = subprocess.run(
        [
            blender_path,
            "-b",
            "-noaudio",
            "-E", "CYCLES",
            "-t", "0",
            "--python-exit-code", "1",
            "-P", scenario_path,
            "-P", RENDER_SCRIPT_PATH,
        ],
        text=True,
        capture_output=True,
    )

    # writing render log
    print('Writing render log...')
    save_render_log(output_dir, completed_process.stdout, 'render.log')
    save_render_log(output_dir, completed_process.stderr, 'render_err.log')

    return completed_process


def save_render_log(output_path, log, filename):
    if log != '':
        log_output_path = Path(output_path) / filename
        with open(log_output_path, mode='w+') as logfile:
            logfile.writelines(log)
