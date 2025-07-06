import sys
import traceback
from networksecurity.logging import logger

class NetworkSecurityException(Exception):
    def __init__(self, error_message: Exception, error_details: sys):
        super().__init__(error_message)
        self.error_message = error_message

        # Get traceback object
        _, _, exc_tb = error_details.exc_info()
        self.lineno = exc_tb.tb_lineno if exc_tb else None
        self.file_name = exc_tb.tb_frame.f_code.co_filename if exc_tb else None

    def __str__(self):
        return (
            f"Error occurred in Python script [{self.file_name}], "
            f"line number [{self.lineno}], error message: {self.error_message}"
        )