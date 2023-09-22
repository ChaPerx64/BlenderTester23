import psutil
import cpuinfo
import platform


def get_sysinfo() -> dict:
    return dict({
        'CPU': cpuinfo.get_cpu_info().get('brand_raw'),
        'RAM': f"{psutil.virtual_memory().total / 1024 / 1024 / 1024:.2f} GB",
        'SYSTEM INFO': f"{platform.system()} {platform.release()}",
    })
