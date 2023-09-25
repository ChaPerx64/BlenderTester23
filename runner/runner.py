from pathlib import Path
import subprocess
import os
import logging
from textwrap import dedent


RENDER_SCRIPT_PATH = Path(__file__).parent / 'render_script.py'
SCENARIO_DIR_PATH = Path().cwd() / 'scenarios'

logger = logging.getLogger(__name__)


def run_scenario(
    x_resolution: str,
    y_resolution: str,
    output_path: str,
    blender_path: str,
    scenario_path: str,
):
    # creating output paths
    render_output_path = Path(output_path) / 'image'

    logger.debug('Environment variables set to:\n'
                 f"X_RESOLUTION: {x_resolution},\n"
                 f"Y_RESOLUTION: {y_resolution},\n"
                 f"OUTPUT_PATH: {str(render_output_path)}"
                 )
    # setting environment variables that render_script will use
    os.environ['X_RESOLUTION'] = x_resolution
    os.environ['Y_RESOLUTION'] = y_resolution
    os.environ['OUTPUT_PATH'] = str(render_output_path)

    # calling Blender in a subprocess
    logger.info('Calling Blender...')
    logger.debug('Blender call arguments:\n'
                 f'blender_path: {blender_path},\n'
                 f'scenario_path: {scenario_path},\n'
                 f'render_script_path: {RENDER_SCRIPT_PATH}'
                 )
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
        stderr=subprocess.STDOUT,
        stdout=subprocess.PIPE
    )

    # writing render log
    logger.info('Writing render log...')
    save_render_log(output_path, completed_process.stdout, 'render.log')

    return completed_process


def save_render_log(output_path, log, filename):
    if log != '':
        log_output_path = Path(output_path) / filename
        with open(log_output_path, mode='w+') as logfile:
            logfile.writelines(log)
