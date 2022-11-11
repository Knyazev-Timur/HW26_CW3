import logging

logging.basicConfig(level=logging.INFO)

def logger_settings(file_path, message):
    logger_file = logging.getLogger('one')
    file_handler = logging.FileHandler(file_path, encoding='UTF-8')
    formatter_one = logging.Formatter("%(asctime)s : %(levelname)s :%(message)s")
    file_handler.setFormatter(formatter_one)
    logger_file.addHandler(file_handler)

    consol_loger = logging.getLogger('two')
    console_handler = logging.StreamHandler()
    formatter_two = logging.Formatter("%(asctime)s : %(levelname)s : %(funcName)s : %(message)s")
    console_handler.setFormatter(formatter_two)
    consol_loger.addHandler(console_handler)

    logger_file.info(message)
    consol_loger.info(message)
    logger_file.handlers = []
    consol_loger.handlers = []
