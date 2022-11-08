import logging

logging.basicConfig(level=logging.INFO)


def log_set(file_path, message):
    log_file = logging.getLogger('one')
    file_handler = logging.FileHandler(file_path, encoding='UTF-8')
    formatter_one = logging.Formatter("%(asctime)s : %(levelname)s :%(message)s")
    file_handler.setFormatter(formatter_one)
    log_file.addHandler(file_handler)

    consol_log = logging.getLogger('two')
    console_handler = logging.StreamHandler()
    formatter_two = logging.Formatter("%(asctime)s : %(levelname)s : %(funcName)s : %(message)s")
    console_handler.setFormatter(formatter_two)
    consol_log.addHandler(console_handler)

    log_file.warning(message)
    consol_log.info(message)
