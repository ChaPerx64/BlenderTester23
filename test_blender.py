import pytest
import logging
import datetime
from pathlib import Path
from runner.reporting import save_report_json
from runner.runner import run_scenario
from runner.finder import find_scenarios

logger = logging.getLogger(__name__)

SCENARIO_DIR_PATH = Path().cwd() / 'scenarios'


@pytest.fixture(
    scope='function',
    params=find_scenarios(SCENARIO_DIR_PATH)
)
def testwrapper(request, sysinfo, input_args):
    output_path = get_name_and_create_subdir(
        input_args['output_path'],
        request.param
    )

    start_time = datetime.datetime.now()
    yield request.param, output_path, input_args
    end_time = datetime.datetime.now()

    # Save json with test information
    save_report_json(
        str(output_path),
        request.param.stem,
        start_time,
        end_time,
        sysinfo,
    )


def test_shapecreation(testwrapper):
    scenario_path, output_path, input_args = testwrapper
    logger.info(f'Starting with scenario "{scenario_path}"...')
    completed_process = run_scenario(
        input_args['x_resolution'],
        input_args['y_resolution'],
        output_path,
        input_args['blender_path'],
        scenario_path,
    )
    assert completed_process.returncode == 0, f"Blender run failed\n{completed_process.stdout}"
    assert completed_process.stdout is not '', "Blender subprocess STDOUT is empty!"
    assert 'Saved: ' in completed_process.stdout, "Image probably was not rendered"
    assert completed_process.stderr is None, completed_process.stderr


def get_name_and_create_subdir(output_path: str | Path, scenario_path: str | Path):
    scenario_name = Path(scenario_path).stem
    output_path = Path(output_path) / scenario_name
    logger.debug(f"Creating output dir: {output_path}")
    output_path.mkdir(parents=True, exist_ok=True)
    return output_path
