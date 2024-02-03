from multiprocessing import Pool
from config import Config
import pandas as pd
import logging
import json
import os

class ETLProcess:
    @staticmethod
    def etl_process(process_id):
        try:
            os.chdir(Config.file_dir)
        except PermissionError as err:
            logging.error(f'Message: {err}')
        except OSError as err:
            logging.error(f'Message: {err}')
        try:
            with open(Config.file_name,'w') as new_file:
                new_file.writelines(Config.file_data)
        except IOError as err:
            logging.error(f'Message: {err}')
        try:
            data_frame = pd.read_csv(Config.file_name)
        except FileNotFoundError as err:
            logging.error(f'Message: {err}')
        try:
            with open(f'output_file_{process_id}.json', 'w') as output_file:
                transformed_data = data_frame.to_json(orient='columns')
                json.dump(transformed_data, output_file)
        except IOError as err:
            logging.error(f'Message: {err}')

class Parallelize:
    @staticmethod
    def parallel_process(num_processes=40):
        with Pool(num_processes) as pool:
            pool.map(
                ETLProcess.etl_process, 
                range(num_processes))