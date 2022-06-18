import logging

# 创建日志对象
logger = logging.getLogger()
logger.setLevel(level="DEBUG")
# 创建控制台处理器
console_handler = logging.StreamHandler()
# 控制台等级
console_handler.setLevel(level="INFO")
# 添加到处理器
logger.addHandler(console_handler)
# 格式器
fmt = "%(name)s--->%(message)s--->%(asctime)s"
logging.basicConfig(level="DEBUG", format=fmt)

logging.debug("This is debug message")
logging.info("This is info message")
logging.warning("This is warning message")
logging.error("This is error")
logging.critical("This is critical message")