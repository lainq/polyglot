import sys as sys
import logging as logging
import time as time
from clint.textui import colored


def stop_current_application(exit_reason=None, set_timeout=0):
    assert isinstance(set_timeout, int), "Expected an integer"
    if exit_reason is not None:
        logging.error(f"Exiting application [{exit_reason}]")

    time.sleep(set_timeout)
    sys.exit()


class PolyglotException(object):
    def __init__(self, error_message, suggestion=None, timeout=None, fatal=True):
        assert self.is_valid_timeout(timeout), "Timeout expected to be an integer"
        assert isinstance(fatal, bool), "Fatal expected a boolean value"

        self.error_message = str(error_message)
        self.error_is_fatal = fatal

        self.suggestion = suggestion
        self.create_exception_message(timeout)

    def create_exception_message(self, timeout=None):
        if timeout is not None:
            time.sleep(timeout)

        self.suggestion = self.create_suggestion_message(self.suggestion)
        self.throw_exception(self.error_message, self.suggestion)

    def throw_exception(self, error, suggestion):
        throw_exception_data = [
            colored.red(f"ERROR: {error}"),
            colored.green(suggestion),
        ]
        for element in throw_exception_data:
            print(element)

        if self.error_is_fatal:
            stop_current_application()

    def is_valid_timeout(self, timeout):
        return isinstance(timeout, int) or timeout == None

    def create_suggestion_message(self, suggestion):
        if suggestion == None:
            return None

        return f"HELP: {suggestion}"

    def __len__(self):
        return len(str(self.error_message))

    def __str__(self):
        return str(self.error_message)

    def __int__(self):
        return self.__len__()

    def __bool__(self):
        return bool(self.error_is_fatal)
