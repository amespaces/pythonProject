# logging

## 快速使用

```python
import logging

logging.debug("This is debug message")
logging.info("This is info message")
logging.warning("This is warning message")
logging.error("This is error")
logging.critical("This is critical message")
```

```
WARNING:root:This is warning message
ERROR:root:This is error
CRITICAL:root:This is critical message
```

- 只会产生3种，因为默认日志级别是warning

## 创建控制台处理器

```python
import logging

# 创建日志对象
logger = logging.getLogger()
# 设置日志处理级别
logger.setLevel(level="DEBUG")


# 创建控制台处理器
console_handle = logging.StreamHandler()
# 设置控制台等级
console_handle.setLevel(level="DEBUG")

# 将控制台处理器添加到日志处理器中
logging.addhandler(console_handle)

# 创建格式器
fmt= "%(name)s--->%(message)s--->%(asctime)s"
logging.basicConfig(fmt)

```

## 创建文件处理器

```python
import logging

# 创建日志对象
logger　＝　logging.getLogger()
logger.setLevel("DEBUG")


# 创建文件处理器
file_handle = logging.FileHandler("./log.txt",mode="a",encoding = "utf-8")
file_handle.setLevel(level="DEBUG")

# 将文件处理器添加到日志处理器中
logger.addHandler(file_handle)

# 创建格式器
fmt= "%(name)s--->%(message)s--->%(asctime)s"
logging.basicConfig(fmt)
```

```python
 # FileHandler类部分源码
 def __init__(self, filename, mode='a', encoding=None, delay=False, errors=None):
 # Formatter类部分源码
def __init__(self, fmt=None, datefmt=None, style='%', validate=True, *,
                 defaults=None):
 %(name)s            Name of the logger (logging channel)
    %(levelno)s         Numeric logging level for the message (DEBUG, INFO,
                        WARNING, ERROR, CRITICAL)
    %(levelname)s       Text logging level for the message ("DEBUG", "INFO",
                        "WARNING", "ERROR", "CRITICAL")
    %(pathname)s        Full pathname of the source file where the logging
                        call was issued (if available)
    %(filename)s        Filename portion of pathname
    %(module)s          Module (name portion of filename)
    %(lineno)d          Source line number where the logging call was issued
                        (if available)
    %(funcName)s        Function name
    %(created)f         Time when the LogRecord was created (time.time()
                        return value)
    %(asctime)s         Textual time when the LogRecord was created
    %(msecs)d           Millisecond portion of the creation time
    %(relativeCreated)d Time in milliseconds when the LogRecord was created,
                        relative to the time the logging module was loaded
                        (typically at application startup time)
    %(thread)d          Thread ID (if available)
    %(threadName)s      Thread name (if available)
    %(process)d         Process ID (if available)
    %(message)s         The result of record.getMessage(), computed just as
                        the record is emitted
```

## 同时在文件和控制台生成日志

```python
import logging


# 创建日志对象
logger = logging.getLogger()
logger.setLevel("DEBUG")

#定义控制台和文件处理器
console_handle = logging.StreamHandler()
file_handle = logging.FileHandler("./log.txt", mode="a", encoding="utf-8")

# 定义格式 上代码块中附格式类的几个参数
fmt1 = "%(name)s--->%(levelname)s--->%(asctime)s--->%(message)s "
fmt2 = "%(lineno)d--->%(levelname)s--->%(asctime)s--->%(message)s "

# 格式器配置日志格式
console_formatter = logging.Formatter(fmt1)
file_formatter = logging.Formatter(fmt2)

# 设置格式
console_handle.setFormatter(console_formatter)
file_handle.setFormatter(file_formatter)

# 添加处理器
logger.addHandler(console_handle)
logger.addHandler(file_handle)

```

## 封装日志配置类

```python
import logging

class Log:
    
    def __init__(self,level="DEBUG"):
        # 创建日志对象,可以自定义姓名
        self.log = logging.getLogger("name")
        self.log.setLevel(level)
        
    def console_handle(self, level="DEBUG"):
        """控制台处理器"""
        console_handle = logging.StreamHandler()
        console_handle.setLevel(level)
        console_handle.setFormatter(self.get_formatter()[0])
        return console_handle
    
    def file_handle(self, level="DEBUG")：
    	"""文件处理器"""
        file_handle = logging.FileHandler("./log.txt",mode="a",encoding="utf-8")
        file_handle.setLevel("DEBUG")
        file_handle.setFormatter(self.get_formatter()[1])
        return file_handle
    
    def get_formatter(self):
        """返回格式器 元组"""
        console_fmt = logging.Formatter(fmt ="%(name)s--->%(levelno)s--->%(asctime)s--->%(message)s" )
        file_fmt = logging.Formatter(fmt ="%(levelname)s--->%(asctime)s--->%(message)s")
        return console_fmt, file_fmt
    
    def get_log(self):
    	# 日志器添加到控制台
        self.log.addHandler(self.console_handle())
        self.log.addHadnler(self.file_handle())
        # 返回日志对象
        return self.log
    	
    
```

测试

```python
from common.log import Log


class Test:
    def __init__(self):
        log = Log()
        self.logger = log.get_log()

    def test1(self):
        self.logger.info("开始执行")



test = Test()
test.test1()
```

