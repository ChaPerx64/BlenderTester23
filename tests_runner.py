import os
import typer
from pathlib import Path
from datetime import datetime
from runner.runner import run_scenario
from runner.finder import find_scenarios
from runner.sysinfo import get_sysinfo
from runner.reporting import save_report_json


def runtests(
    blender_path: str,
    output_path: str,
    x_resolution: int,
    y_resolution: int,
    create_dir=False
):
    print('Test started\n')

    # checking if correct argument types are provided
    if not (('blender' == os.path.basename(blender_path)) or ('blender.exe' == os.path.basename(blender_path))):
        raise FileNotFoundError(
            f'Incorrect input: blender_path ("{blender_path}") is not a blender executable.')
    if not Path(output_path).is_dir():
        raise NotADirectoryError(
            'Incorrect input: out_path is not a directory or does not exist')

    print('Collecting system info')
    sysinfo = get_sysinfo()

    # creating a directory for this run of tests
    if create_dir:
        print('Creating a directory for this run of tests')
        output_path = Path(output_path) / \
            f"run_{datetime.strftime(datetime.now(), '%Y-%m-%d_%H-%M-%S')}"
        os.mkdir(output_path)

    # searching for the dir test scenarios
    scenarios = find_scenarios(Path().cwd() / 'scenarios')

    # Runninf scenarios
    for n, scenario in enumerate(scenarios, 1):
        print(
            f"\nRunning scenario {n}/{len(scenarios)}: {scenario['scenario_name']}...")
        scenario_output_path = Path(output_path) / scenario['scenario_name']
        os.mkdir(scenario_output_path)
        test_started = datetime.now()
        run_scenario(
            x_resolution,
            y_resolution,
            scenario_output_path,
            blender_path,
            scenario
        )
        test_finished = datetime.now()
        print('Forming a report...')
        save_report_json(
            scenario_output_path,
            scenario['scenario_name'],
            test_started,
            test_finished,
            sysinfo,
        )
        print('Scenario run complete.')

    print('\nTest completed.')


if __name__ == "__main__":
    typer.run(runtests)
