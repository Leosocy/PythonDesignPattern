from abc import ABCMeta, abstractmethod
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


class LoggerFactory(object):

    @staticmethod
    def create(logger_type):
        if logger_type.lower() == 'db':
            # 连接数据库，代码省略
            # 创建数据库日志记录器对象
            logger = DatabaseLogger()
            # 初始化数据库日志记录器，代码省略
            return logger
        elif logger_type.lower() == 'file':
            # 创建日志文件  
            # 创建文件日志记录器对象  
            logger = FileLogger()
            # 初始化文件日志记录器，代码省略  
            return logger
        else:
            return None


class LoggerTests(unittest.TestCase):

    def test_create_db_logger(self):
        logger = LoggerFactory.create('db')
        self.assertIsInstance(logger, DatabaseLogger)

    def test_create_unsupported_logger(self):
        logger = LoggerFactory.create('unsupported')
        self.assertIsNone(logger)


if __name__ == '__main__':
    unittest.main()