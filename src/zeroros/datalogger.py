import datetime
import json
from pathlib import Path

from zeroros.messages import Message


class DataLogger:
    def __init__(self, log_dir: str = "logs"):
        self.log_dir = log_dir
        # create filename with date and time
        self.filename = datetime.datetime.now().strftime("%Y%m%d_%H%M%S") + "_log.json"
        self.log_file = Path(self.log_dir) / self.filename
        self.log_file.parent.mkdir(parents=True, exist_ok=True)
        # Open the log file
        self.file = open(self.log_file, "w")

    def log(self, msg: type[Message], topic_name: str = "unknown"):
        # Write message to file
        self.file.write(
            '{"class": "'
            + str(type(msg).__name__)
            + '", "topic_name": "'
            + topic_name
            + '", "timestamp": "'
            + str(datetime.datetime.utcnow().timestamp())
            + '", "message": '
            + json.dumps(msg.to_json())
            + "}\n"
        )
        self.file.flush()
