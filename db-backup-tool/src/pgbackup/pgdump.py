import subprocess
import sys


def dump(url: str):
    try:
        return subprocess.Popen(['pg_dump', url], stdout=subprocess.PIPE)
    except OSError as e:
        print(f"Most likely pg_dump couldn't not be found on the system: {e}")
        sys.exit(1)


def dump_file_name(url: str, timestamp=None):
    db_name = url.split('/')[-1].split('?')[0]
    if timestamp:
        return f"{db_name}-{timestamp}.sql"

    return f"{db_name}.sql"
