import logging
import os
from datetime import datetime
# Create and configure logger
logfile=f"{datetime.now().strftime('%Y-%m-%d-%H-%M-S')}.log"
log_path=os.path.join(os.getcwd(),'logs',logfile)
os.makedirs(log_path,exist_ok=True)

log_file_path=os.path.join(log_path,logfile)
logging.basicConfig(filename=log_file_path,
                    format='[%(asctime)s] %(lineno)d  %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

if __name__ == '__main__':
    logging.info("logging has started")
    