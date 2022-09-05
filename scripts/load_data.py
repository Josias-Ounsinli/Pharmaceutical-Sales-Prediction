import pandas as pd
import logging

logging.basicConfig(filename='./general_logfile.log', filemode='a',
                    encoding='utf-8', level=logging.DEBUG)

def load_data(path: str):
    try:
        df = pd.read_csv(path)
    except BaseException:
        logging.warning('file not found or wrong file format')
    return df


