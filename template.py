import os
from pathlib import Path
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",

)


list_of_files = [
    'src/__ini__.py',
    'src/helper.py',
    '.env',
    'app.py',
    'requirements.txt'
]


for filepath in list_of_files:
    filepath = Path(filepath)

    filedir, filename = os.path.split(filepath)


    if filedir != "":
        os.makedirs(filedir, exist_ok = True)
        logging.info(f'creating directories :: {filedir} of filename :: {filename}')

    if not os.path.exists(filepath):
        with open(filepath, 'w') as f:
            pass
            logging.info(f'creating file : {filepath}')
    else:
        logging.info(f'file {filepath} already exists')



