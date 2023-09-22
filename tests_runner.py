from pathlib import Path
import subprocess
import tempfile
import os
import platform
from datetime import datetime
import psutil
import cpuinfo
import json
import typer


def save_report_JSON(
    output_path: str,
    test_name: str,
    time_start: datetime,
    time_end: datetime,
):
    test_duration = time_end - time_start
    out_dict = dict()
    out_dict.update({
        'test_name': test_name,
        'test_started': time_start.isoformat(),
        'test_finished': time_end.isoformat(),
        'test_duration': f"{test_duration.total_seconds()} seconds",
        'system_info': dict({
            'CPU': cpuinfo.get_cpu_info().get('brand_raw'),
            'RAM': f"{psutil.virtual_memory().total / 1024 / 1024 / 1024:.2f} GB",
            'SYSTEM INFO': f"{platform.system()} {platform.release()}",
        })
    })
    with open(Path(output_path) / 'report.json', mode='w+') as f:
        json.dump(out_dict, f, indent=2)


def find_scenarios(search_root: str | Path = ''):
    scenarios = list()
    for root, dirs, files in os.walk(search_root):
        for f in files:
            if f == 'scenario.py':
                scenario = {
                    'scenario_name': Path(root).name,
                    'scenario_path': Path(root) / f,
                }
                scenarios.append(scenario)
    return scenarios


def test_scenario(
    x_resolution: str,
    y_resolution: str,
    output_path: str,
    blender_path: str,
    scenario: dict,
):
    test_name = scenario['scenario_name']
    script_template_path = scenario['scenario_path']
    test_started = datetime.now()

    # creating output paths
    render_output_path = Path(output_path) / 'image'
    log_output_path = Path(output_path) / 'render.log'

    # creating a temporary blender script from a script template
    # script_template_path = Path().cwd() / \
    #     'test_1' / 'scenario_1_template.py'
    script = tempfile.NamedTemporaryFile(mode='w+', delete=False)
    with open(script_template_path, mode='r') as f:
        script.writelines(f)
    script.write(
        f'\nrender_image(r"{render_output_path}", {x_resolution}, {y_resolution},)'
    )
    script.close()

    # calling blender in a subprocess
    with open(log_output_path, mode='w') as logfile:
        subprocess.run(
            f'"{blender_path}" -b -P "{script.name}"',
            stderr=logfile,
            stdout=logfile,
        )

    # deleteing the temporary file
    os.remove(script.name)

    test_finished = datetime.now()

    # saveing JSON-file
    save_report_JSON(
        output_path,
        test_name,
        test_started,
        test_finished
    )


def runtests(
    blender_path: str,
    output_path: str,
    x_resolution: int,
    y_resolution: int,
):
    # checking if all argumets are provided
    if not blender_path:
        raise ValueError('blender_path is not provided')
    if not output_path:
        raise ValueError('output_path is not provided')
    if not x_resolution:
        raise ValueError('x_resolution is not provided')
    if not y_resolution:
        raise ValueError('y_resolution is not provided')

    # checking if correct argument types are provided
    if not ((r'\blender' == blender_path[-8:]) or (r'\blender.exe' == blender_path[-12:])):
        raise FileNotFoundError(
            f'Incorrect input: blender_path ("{blender_path}") is not a blender executable.')
    if not Path(output_path).is_dir():
        raise NotADirectoryError(
            'Incorrect input: out_path is not a directory or does not exist')
    if type(x_resolution) != int:
        raise TypeError(
            'Incorrect input: x_resolution argument should be an int')
    if type(y_resolution) != int:
        raise TypeError(
            'Incorrect input: y_resolution argument should be an int')

    print('Test started')
    print('Scanning the workfolder for test scenarios...')

    # creating a directory for this run of tests
    output_path = Path(output_path) / \
        f"run_{datetime.strftime(datetime.now(), '%Y-%m-%d_%H-%M-%S')}"
    os.mkdir(output_path)

    # searching for the dir test scenarios
    scenarios = find_scenarios(Path().cwd() / 'scenarios')
    total_scenarios = len(scenarios)
    print(f"{total_scenarios} scenarios found:")
    for scenario in scenarios:
        print(
            f"{scenario['scenario_name']}\t\t\t\t{scenario['scenario_path']}")

    # running scenarios
    for n, scenario in enumerate(scenarios, 1):
        print(
            f"Running scenario {n}/{total_scenarios}: {scenario['scenario_name']}...")
        scenario_output_path = Path(output_path) / scenario['scenario_name']
        os.mkdir(scenario_output_path)
        test_scenario(
            x_resolution,
            y_resolution,
            scenario_output_path,
            blender_path,
            scenario
        )


if __name__ == "__main__":
    typer.run(runtests)
