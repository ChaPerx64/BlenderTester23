import pytest
import logging
import datetime
from pathlib import Path
from runner.sysinfo import get_sysinfo
from runner.reporting import save_report_json
from runner.runner import run_scenario

logger = logging.getLogger(__name__)


@pytest.fixture(scope='session')
def sysinfo():
    return get_sysinfo()


@pytest.fixture(
    scope='function',
    params=[
        'Primitives_wo_material',
        'Primitives_w_material',
        'Primitives_w_lighting',
    ])
def testwrapper(request, sysinfo):
    input_args = read_test_args(request)
    start_time = datetime.datetime.now()
    yield request.param

    # Save json with test information
    save_report_json(
        Path(input_args['output_path']) / request.param,
        request.node.name,
        start_time,
        datetime.datetime.now(),
        sysinfo,
    )


def read_test_args(request):
    return {
        'blender_path': request.config.getoption("--blender_path",),
        'output_path': request.config.getoption("--output_path"),
        'x_resolution': request.config.getoption("--x_resolution"),
        'y_resolution': request.config.getoption("--y_resolution"),
    }


def test_shapecreation(request, testwrapper):
    input_args = read_test_args(request)
    completed_process = run_scenario(
        input_args['x_resolution'],
        input_args['y_resolution'],
        input_args['output_path'],
        input_args['blender_path'],
        testwrapper,
    )
    assert completed_process.returncode == 0
