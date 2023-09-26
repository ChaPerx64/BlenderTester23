from pathlib import Path
import os
import logging

logger = logging.getLogger(__name__)


def find_scenarios(search_root: str | Path) -> tuple[list[Path], list[str]]:
    """
    Recursively searches for test scenario files with a '.py' extension under
    the 'search_root' directory.

    Args:
        search_root (str or Path): The directory path to start the search from.

    Returns:
        Tuple[List[Path], List[str]]: A tuple containing two lists:
            1. List of Path objects representing the found scenario file paths.
            2. List of scenario names (without the '.py' extension) corresponding
            to the found files.

    """
    logger.info('Searching for test scenarios...')
    logger.debug(f'Search root: {search_root}')
    names = list()
    scenarios = list()
    for root, dirs, files in os.walk(search_root):
        for f in files:
            if '.py' in f[-3:]:
                scenarios.append(Path(root) / f)
                names.append(f[:-3])
    logger.debug(
        'Scenarios found\n' +
        '\n'.join([str(path) for path in scenarios])
    )
    return scenarios, names
