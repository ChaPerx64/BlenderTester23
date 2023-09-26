import cpuinfo
import platform
import os
import sys
import logging

logger = logging.getLogger(__name__)


def get_ram_gb() -> str:
    """
    Get the total RAM size in gigabytes (GB) for the current system.

    Returns:
        str: A string representing the total RAM size in gigabytes (e.g., "16.00 GB").

    Raises:
        Exception: If an error occurs while attempting to retrieve the RAM size.

    Note:
        This function checks the current operating system (Windows, Linux, macOS)
        and uses appropriate methods to obtain the total physical memory.

    """
    try:
        # Check if the OS is Windows
        if sys.platform == 'win32':
            # Use the "wmic" command to get total physical memory on Windows
            result = os.popen(
                'wmic ComputerSystem get TotalPhysicalMemory /value').read()
            total_memory = int(result.strip().split('=')[1])
            total_memory_gb = total_memory / (1024 ** 3)
        # Check if the OS is Linux or macOS
        elif sys.platform in ['linux', 'darwin']:
            # Use the "/proc/meminfo" file to get total physical memory on Linux/macOS
            with open('/proc/meminfo', 'r') as mem_info:
                for line in mem_info:
                    if line.startswith('MemTotal:'):
                        total_memory_kb = int(line.split()[1])
                        total_memory_gb = total_memory_kb / (1024 ** 2)
                        break
        else:
            return "Unsupported operating system"
        return f"{total_memory_gb:.2f} GB"
    except Exception as e:
        return (f"Error occured: {e}")


def get_sysinfo() -> dict:
    """
    Collect and return system information including CPU, RAM, and operating system details.

    Returns:
        dict: A dictionary containing system information.

    """
    logger.info('Collecting system info...')
    return dict({
        'CPU': cpuinfo.get_cpu_info().get('brand_raw'),
        'RAM': get_ram_gb(),
        'SYSTEM INFO': f"{platform.system()} {platform.release()}",
    })
