import logging
import os 
from datetime import datetime


LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
logs_path=os.path.join(os.getcwd(),"logs",LOG_FILE)
os.makedirs(logs_path,exist_ok=True)

LOG_FILE_PATH=os.path.join(logs_path,LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="%(asctime)s|%(levelname)s|%(message)s",
    level=logging.INFO,
)

if __name__=="__main__":
    try:
        a=1/0
    except Exception as e:
        logging.info("divided by zero")
        raise CustomException(e,sys)


"""import logging
import os 
from datetime import datetime

class CustomFormatter(logging.Formatter):
    def format(self, record):
        record.asctime = self.formatTime(record, self.datefmt)  # Add 'asctime' to the log record
        return super().format(record)

LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
logs_path = os.path.join(os.getcwd(), "logs")
os.makedirs(logs_path, exist_ok=True)
LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="%(asctime)s|%(levelname)s|%(message)s",
    level=logging.INFO,
    datefmt="%Y-%m-%d %H:%M:%S",  # Specify the date format for asctime
    style="%",  # Use '%' as the style since you are using the old-style formatting
)

# Set the custom formatter
logging.getLogger().handlers[0].setFormatter(CustomFormatter())

if __name__ == "__main__":
    logging.info("Logging has started")
"""