import sys
from logger import logging 



def error_massage_details(error,error_details:sys):
        _,_,exc_tb = error_details.exc_info()
        file_name = exc_tb.tb_frame.f_code.co_filename
        error_massage = " error occur in python script name  [{0}] line number [{1} error massage [{2}]]".format(
        file_name,exc_tb.tb_lineno, str(error))

        return error_massage
        
class CustomException(Exception):
        def __init__(self, error_massage, error_details:sys):
                super.__init__(error_massage)
                self.error_message= error_massage_details(error_massage , error_details=error_details)

        def __str__(self):
               return self.error_message
if __name__== "__main__":
    
    try:
        a =1/10
    except Exception as e:
        logging.info('divied by zero ')
        raise CustomException(e,sys)