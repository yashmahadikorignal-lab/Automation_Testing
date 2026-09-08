import logging
import os

class LogGen:
    @staticmethod
    def logging():
        log_dir = os.path.join(os.path.abspath(os.curdir), "Logs")
        os.makedirs(log_dir, exist_ok=True)
        log_path = os.path.join(log_dir, "automation.log")

        logger = logging.getLogger("automation")
        logger.setLevel(logging.DEBUG)

        if not logger.handlers:
            file_handler = logging.FileHandler(log_path, mode="a", encoding="utf-8")
            formatter = logging.Formatter(
                "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
                datefmt="%m/%d/%y %I:%M:%S %p"
            )
            file_handler.setFormatter(formatter)
            logger.addHandler(file_handler)

        return logger
