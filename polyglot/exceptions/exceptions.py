import sys as sys
import logging as logging
import time as time
from clint.textui import colored

def stop_current_application(self, exit_reason=None, set_timeout=0):
    assert isinstance(set_timeout, int), "Expected an integer" 
    if exit_reason is not None:
        logging.error(f"Exiting application [{exit_reason}]")

    time.sleep(set_timeout)
    sys.exit()

class PolyglotException(object):
    def __init__(self, error_message, suggestion=None, timeout=None):
        assert self.is_valid_timeout(timeout), "Timeout expected to be an integer"

        self.error_message = str(error_message)

        self.suggestion = suggestion
        self.create_exception_message(timeout)

    def create_exception_message(self, timeout=None, fatal=True):
        if timeout is not None:time.sleep(timeout)

        self.error_is_fatal = fatal

        self.suggestion = self.create_suggestion_message(self.suggestion)
        self.throw_exception(self.error_message, self.suggestion)

    def throw_exception(self, error, suggestion):
        throw_exception_data = [
            colored.red(f"ERROR: {error}"), colored.green(suggestion)
        ]
        for element in throw_exception_data:
            print(element)

        if error_is_fatal:
            stop_current_application()

    def is_valid_timeout(self, timeout):
        return isinstance(timeout, int) or timeout == None

    def create_suggestion_message(self, suggestion):
        if suggestion == None:return None

        return f"HELP: {suggestion}"