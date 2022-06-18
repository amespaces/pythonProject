import logging

logger = logging.getLogger()
logger.setLevel(level="DEBUG")
logging.Formatter
# 创建文本处理器
file_handle = logging.FileHandler("./log.txt", mode="a", encoding="utf-8")
file_handle.setLevel(level="ERROR")

logger.addHandler(file_handle)

fmt = "%(name)s--->%(message)s--->%(asctime)s"
logging.basicConfig(level="DEBUG", format=fmt)

logging.debug("This is debug message")
logging.info("This is info message")
logging.warning("This is warning message")
logging.error("This is error")
logging.critical("This is critical message")
