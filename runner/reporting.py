from datetime import datetime
from pathlib import Path
import json


def save_report_json(
    output_path: str,
    test_name: str,
    time_start: datetime,
    time_end: datetime,
    sysinfo: dict,
):
    test_duration = time_end - time_start
    out_dict = dict()
    out_dict.update({
        'test_name': test_name,
        'test_started': time_start.isoformat(),
        'test_finished': time_end.isoformat(),
        'test_duration': f"{test_duration.total_seconds()} seconds",
        'system_info': sysinfo,
    })
    with open(Path(output_path) / 'report.json', mode='w+') as f:
        json.dump(out_dict, f, indent=2)
