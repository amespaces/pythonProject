import logging


class Log:

    def __init__(self, level="DEBUG"):
        # 日志器对象
        self.log = logging.getLogger("name")
        self.log.setLevel(level)

    def console_handle(self, level="DEBUG"):
        """控制台处理器"""
        console_handle = logging.StreamHandler()
        console_handle.setLevel(level)
        console_handle.setFormatter(self.get_formatter()[0])
        return console_handle

    def file_handle(self, level="DEBUG"):
        """文件处理器"""
        file_handle = logging.FileHandler("./log.txt", mode="a", encoding="utf-8")
        file_handle.setLevel(level)
        file_handle.setFormatter(self.get_formatter()[1])
        return file_handle

    def get_formatter(self):
        """格式"""
        console_fmt= logging.Formatter(fmt="%(name)s--->%(levelno)s--->%(asctime)s--->%(message)s")
        file_fmt = logging.Formatter(fmt="%(levelname)s--->%(asctime)s--->%(message)s")
        return console_fmt, file_fmt

    def get_log(self):
        # 日志器添加到控制台
        self.log.addHandler(self.console_handle())
        # 添加到文件处理器
        self.log.addHandler(self.file_handle())
        return self.log