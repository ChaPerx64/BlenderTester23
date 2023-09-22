from pathlib import Path
import os


def find_scenarios(search_root: str | Path = ''):
    print('Scanning the workfolder for test scenarios...')
    scenarios = list()
    for root, dirs, files in os.walk(search_root):
        for f in files:
            if f == 'scenario.py':
                scenario = {
                    'scenario_name': Path(root).name,
                    'scenario_path': Path(root) / f,
                }
                scenarios.append(scenario)
    print(f"{len(scenarios)} scenarios found:")
    for scenario in scenarios:
        print(
            f"{scenario['scenario_name']}\t\t\t\t{scenario['scenario_path']}")
    return scenarios
