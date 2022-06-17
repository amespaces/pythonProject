import logging

logger = logging.getLogger()
logger.setLevel(level="DEBUG")
# 定义处理器
console_handle = logging.StreamHandler()
file_handle = logging.FileHandler("./log.txt", mode="a", encoding="utf-8")

# 定义格式
fmt1 = "%(name)s--->%(levelname)s--->%(asctime)s--->%(message)s "
fmt2 = "%(lineno)d--->%(levelname)s--->%(asctime)s--->%(message)s "

console_formatter = logging.Formatter(fmt1)
file_formatter = logging.Formatter(fmt2)

console_handle.setFormatter(console_formatter)
file_handle.setFormatter(file_formatter)

logger.addHandler(console_handle)
logger.addHandler(file_handle)

logging.debug("This is debug message")
logging.info("This is info message")
logging.warning("This is warning message")
logging.error("This is error")
logging.critical("This is critical message")
