import logging
import os

class CustomLogger:

    def __init__(self, log_file_path, log_file_name, log_level=logging.DEBUG):
        """
        Initializes the custom logger with a log file and logging level.

        Args:
            log_file_name (str, optional): The name of the log file. Defaults to "script.log".
            log_level (int, optional): The logging level. Defaults to logging.DEBUG (all messages).
        """
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(log_level)

        formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")

        log_full_name = os.path.join(log_file_path, log_file_name)

        file_handler = logging.FileHandler(log_full_name)
        file_handler.setFormatter(formatter)
        self.logger.addHandler(file_handler)

        # Optional stream handler to also log to console
        # stream_handler = logging.StreamHandler()
        # stream_handler.setFormatter(formatter)
        # self.logger.addHandler(stream_handler)

    def debug(self, message):
        """Logs a debug message."""
        self.logger.debug(message)

    def info(self, message):
        """Logs an informational message."""
        self.logger.info(message)

    def warning(self, message):
        """Logs a warning message."""
        self.logger.warning(message)

    def error(self, message):
        """Logs an error message."""
        self.logger.error(message)

    def exception(self, message, exc_info=True):
        """Logs an error message with the traceback.

        Args:
            message (str): The error message.
            exc_info (bool, optional): Whether to include the traceback. Defaults to True.
        """
        self.logger.exception(message, exc_info=exc_info)


# Example usage
# logger = CustomLogger(f"D:\\Source\\Python\\Logs", "logs.txt")

# try:
#     print("hahah")
# except Exception as e:
#     logger.exception("An error occurred:", exc_info=True)

# logger.debug("Script debugged successfully!")
# logger.info("Script running...")
# logger.warning("Warning!")
# logger.error("Error - script failed!")
# logger.exception("Exception occured!")
