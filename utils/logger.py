import logging

def get_logger(name:str)->logging.Logger:
    logger=logging.getLogger(name)
    logger.setlevel(logging.DEBUG)

    handler=logging.FileHandler('app.log')
    formatter=logging.Formatter('%(asctime)s - %(name)s - %(levlname)s - %(message)s')
    handler.setFormatter(formatter)

    if not logger.hasHandlers():
        
