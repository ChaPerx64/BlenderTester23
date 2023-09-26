from datetime import datetime
from pathlib import Path
import json
import logging

logger = logging.getLogger(__name__)


def save_report_json(
        output_path: str,
        test_name: str,
        time_start: datetime,
        time_end: datetime,
        sysinfo: dict,):
    """
    Save test report information in JSON format to a specified output directory.

    Args:
        output_path (str): The directory where the JSON report file will be saved.
        test_name (str): The name of the test scenario.
        time_start (datetime): The start time of the test.
        time_end (datetime): The end time of the test.
        sysinfo (dict): System information to be included in the report.

    Note:
        This function creates a JSON report file containing information about the test,
        including its name, start time, end time, duration, and system information.
        The report file is saved in the specified 'output_path' directory.

    """
    logger.info('Saving test report into JSON-file')
    logger.debug(f"Saving path: {Path(output_path) / 'report.json'}")
    test_duration = time_end - time_start
    out_dict = dict()
    out_dict.update({
        'test_name': test_name,
        'test_started': time_start.isoformat(),
        'test_finished': time_end.isoformat(),
        'test_duration': f"{test_duration.total_seconds()} seconds",
        'system_info': sysinfo,
    })
    logger.debug('Test report:\n' +
                 '\n'.join([f"{key} : {value}" for key, value in out_dict.items()]))
    # Path(output_path).mkdir(parents=True, exist_ok=True)
    with open(Path(output_path) / 'report.json', mode='w+') as f:
        json.dump(out_dict, f, indent=2)
