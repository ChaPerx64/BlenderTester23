import pytest
import logging
from runner.sysinfo import get_sysinfo

logger = logging.getLogger(__name__)


def pytest_addoption(parser):
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
    return get_sysinfo()
