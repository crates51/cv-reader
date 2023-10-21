from cv_reader.utils import logging
import json
from pathlib import Path

logger = logging.get_logger()
PROJECT_PATH = Path(__file__).parent.parent.parent.resolve()


def get() -> dict:
    with open(f"{PROJECT_PATH}/seeds/cv.json", 'r') as j:
        data = json.loads(j.read())
    return data
