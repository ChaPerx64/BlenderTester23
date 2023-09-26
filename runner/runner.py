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
) -> subprocess.CompletedProcess:
    """
    Run a Blender scenario in a subprocess with specified settings.

    Args:
        x_resolution (str): The horizontal resolution of image rendered.
        y_resolution (str): The vertical resolution of image rendered.
        output_path (str): The directory where rendering output will be saved.
        blender_path (str): The path to the Blender executable.
        scenario_path (str): The path to the Python scenario script to be executed.

    Returns:
        subprocess.CompletedProcess: A CompletedProcess object representing
        the result of the Blender subprocess.

    Note:
        This function sets environment variables, such as X_RESOLUTION, Y_RESOLUTION,
        and OUTPUT_PATH, to configure the rendering process.
        It then calls Blender in a subprocess with the specified arguments.

    Example:
        Running a Blender scenario:

        ```
        x_resolution = '1920'
        y_resolution = '1080'
        output_dir = '/path/to/output'
        blender_exe = '/path/to/blender'
        scenario_script = '/path/to/scenario.py'
        result = run_scenario(
            x_resolution,
            y_resolution,
            output_dir,
            blender_exe,
            scenario_script
        )
        ```

    """
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
    """
    Save the render log to a specified file in the output directory.

    Args:
        output_path (str): The directory where the log file will be saved.
        log (str): The render log content to be saved.
        filename (str): The name of the log file.

    Note:
        If the 'log' parameter is empty, no log file will be created.

    Example:
        Saving a render log:

        ```
        output_dir = '/path/to/output'
        log_content = 'Render log content...'
        log_filename = 'render.log'
        save_render_log(output_dir, log_content, log_filename)
        ```

    """
    if log != '':
        log_output_path = Path(output_path) / filename
        with open(log_output_path, mode='w+') as logfile:
            logfile.writelines(log)
