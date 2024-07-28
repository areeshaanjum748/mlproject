import sys  # for python environment variables
import logging

def error_message_detail(error, error_detail:sys):
    '''
    This function takes an error and error_detail as input and returns a formatted error message
    '''
    _,_,exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    line_number = exc_tb.tb_lineno
    error_message = "Error occurred in python script name [{0}] line number [{1}] error message [{2}]".format(
       file_name,
       line_number,
       str(error)
    )
    return error_message

class CustomException(Exception):
    '''
    Custom exception class to handle specific exceptions
    '''
    def __init__(self, error_message, error_detail:sys):
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message, error_detail = error_detail)

    def __str__(self):
        return self.error_message



