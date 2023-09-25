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
    sysinfo: dict,
):
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
