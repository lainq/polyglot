import sys as sys
import logging as logging
import time as time

def stop_current_application(self, exit_reason=None, set_timeout=0):
    assert isinstance(set_timeout, int), "Expected an integer" 
    if exit_reason is not None:
        logging.error(f"Exiting application [{exit_reason}]")

    time.sleep(set_timeout)
    sys.exit()

class PolyglotException(object):
    def __init__(self, error_message, line_number, suggestion=None):
        self.error_message = str(error_message)
        self.line_number = int(line_number)

        self.suggestion = suggestion

    def create_exception_message(self, timeout=None):
        pass
        