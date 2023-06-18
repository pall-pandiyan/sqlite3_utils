import os

from pathlib import Path


PROJECT_DIR = Path(__file__).resolve().parent.parent
DB_DIR = os.path.join(PROJECT_DIR, 'dbs')
