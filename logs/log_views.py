import logging

logging.basicConfig(level=logging.INFO)


def log_set(file_path, message):
    log_file = logging.getLogger('three')
    file_handler = logging.FileHandler(file_path, encoding='UTF-8')
    formatter_three = logging.Formatter("%(asctime)s : %(levelname)s :%(message)s")
    file_handler.setFormatter(formatter_three)
    log_file.addHandler(file_handler)

    consol_log = logging.getLogger('four')
    console_handler = logging.StreamHandler()
    formatter_four = logging.Formatter("%(asctime)s : %(levelname)s : %(funcName)s : %(message)s")
    console_handler.setFormatter(formatter_four)
    consol_log.addHandler(console_handler)

    log_file.warning(message)
    consol_log.info(message)
    log_file.handlers = []
    consol_log.handlers = []