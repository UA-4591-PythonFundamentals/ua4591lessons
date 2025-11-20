import os
import logging
current_path = os.path.abspath(__file__)
dir_path = os.path.dirname(current_path)
print(f"Current file path: {current_path}")
logging.basicConfig(level=logging.ERROR,
                    filename=os.path.join(dir_path, 'app.log'),
                    filemode='w',
                    format='%(asctime)s\t%(levelname)s\t%(filename)s\t%(funcName)s\t%(message)s')



if __name__ == "__main__":
    logging.debug('This is a debug message')
    logging.info('This is an info message')
    logging.warning('This is a warning message')
    logging.error('This is an error message')
    logging.critical('This is a critical message')