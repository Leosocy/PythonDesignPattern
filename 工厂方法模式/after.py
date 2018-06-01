from abc import ABCMeta, abstractmethod, abstractstaticmethod
import unittest

class Logger(object, metaclass=ABCMeta):

    @abstractmethod
    def write(self):
        pass


class DatabaseLogger(Logger):

    def write(self):
        print("数据库日志记录")


class FileLogger(Logger):

    def write(self):
        print("文件日志记录") 


class LoggerFactory(object, metaclass=ABCMeta):

    @abstractstaticmethod
    def create():
        pass


class DatabaseLoggerFactory(LoggerFactory):

    def create():
        # 连接数据库，代码省略
        # 创建数据库日志记录器对象
        logger = DatabaseLogger()
        # 初始化数据库日志记录器，代码省略
        return logger


class FileLoggerFactory(LoggerFactory):

    def create():
         # 创建日志文件  
        # 创建文件日志记录器对象  
        logger = FileLogger()
        # 初始化文件日志记录器，代码省略
        return logger


class LoggerTests(unittest.TestCase):

    def test_database_logger_factory(self):
        logger = DatabaseLoggerFactory.create()
        self.assertIsInstance(logger, DatabaseLogger)
        

if __name__ == '__main__':
    unittest.main()