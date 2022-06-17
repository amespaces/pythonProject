from common.log import Log


class Test:
    def __init__(self):
        log = Log()
        self.logger = log.get_log()

    def test1(self):
        self.logger.info("开始执行")


test = Test()
test.test1()
