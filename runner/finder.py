from pathlib import Path
import os
import logging

logger = logging.getLogger(__name__)


def find_scenarios(search_root: str | Path = ''):
    logger.info('Searching for test scenarios...')
    logger.debug(f'Search root: {search_root}')
    scenarios = list()
    for root, dirs, files in os.walk(search_root):
        for f in files:
            if '.py' in f[-3:]:
                scenarios.append(Path(root) / f)
    logger.debug(
        'Scenarios found\n' +
        '\n'.join([str(path) for path in scenarios])
    )
    return scenarios
