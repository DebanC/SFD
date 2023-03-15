from sensor.exception import SensorException
from sensor.logger import logging
from from_root import from_root
import os,sys




def test_exception():
    try:
        logging.info("we are didviding by zero")
        x=1/0
        
    except Exception as e:
        raise SensorException(e,sys)
    

if __name__=="__main__":
    try:
        test_exception()
    except Exception as e:
        print(e)
           


    