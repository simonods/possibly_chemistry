import os
import sys
from pathlib import Path

if __name__ == '__main__':
    BASE_DIR = Path(__file__).resolve().parent
    sys.path.append(str(BASE_DIR / "app"))

    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'possibly_chemistry.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django."
        ) from exc
    execute_from_command_line(sys.argv)
