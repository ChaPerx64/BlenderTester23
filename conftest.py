import pytest
import logging
from runner.sysinfo import get_sysinfo

logger = logging.getLogger(__name__)


def pytest_addoption(parser):
    """
    Add command-line options for pytest.

    Args:
        parser (argparse.ArgumentParser): The pytest argument parser.

    Options:
        --blender_path: Path to the executable file blender.exe.
        --output_path: Folder where test results will be saved.
        --x_resolution: The width of the rendered image.
        --y_resolution: The height of the rendered image.

    Example:
        Running pytest with custom options:

        ```
        pytest --blender_path /path/to/blender.exe --output_path /path/to/results --x_resolution 1920 --y_resolution 1080
        ```

    """
    parser.addoption(
        "--blender_path",
        help="path to the executable file blender.exe"
    )
    parser.addoption(
        "--output_path",
        help="folder where test results will be saved."
    )
    parser.addoption(
        "--x_resolution",
        help="the width of the rendered image."
    )
    parser.addoption(
        "--y_resolution",
        help="the height of the rendered image."
    )


@pytest.fixture(scope='session')
def input_args(request):
    """
    Pytest fixture to retrieve input arguments for tests.

    Args:
        request (pytest.FixtureRequest): The request object.

    Returns:
        dict: A dictionary containing input arguments for tests.

    Example:
        Usage of the 'input_args' fixture in a test:

        ```python
        def test_example(input_args):
            print(f"Blender Path: {input_args['blender_path']}")
            print(f"Output Path: {input_args['output_path']}")
        ```

    """
    input_args = {
        'blender_path': request.config.getoption("--blender_path",),
        'output_path': request.config.getoption("--output_path"),
        'x_resolution': request.config.getoption("--x_resolution"),
        'y_resolution': request.config.getoption("--y_resolution"),
    }
    logger.debug(
        'Parameters recieved:\n' +
        '\n'.join([f"{key} : {value}" for key, value in input_args.items()])
    )
    return input_args


@pytest.fixture(scope='session')
def sysinfo():
    """
    Pytest fixture to retrieve system information.

    Returns:
        dict: A dictionary containing system information.

    """
    return get_sysinfo()
