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


class LoggerFactory(object, metaclass=ABCMeta):
    @abstractmethod
    def create(self):
        pass


class DatabaseLoggerFactory(LoggerFactory):
    def create(self):
        # 连接数据库，代码省略
        # 创建数据库日志记录器对象
        logger = DatabaseLogger()
        # 初始化数据库日志记录器，代码省略
        return logger


class FileLoggerFactory(LoggerFactory):
    def create(self):
        # 创建日志文件
        # 创建文件日志记录器对象
        logger = FileLogger()
        # 初始化文件日志记录器，代码省略
        return logger


class LoggerFactorySelector(object):
    @staticmethod
    def get_logger_factory(factory_type):
        for sc in LoggerFactory.__subclasses__():
            if sc.__name__ == factory_type:
                return sc()
        return None


class LoggerTests(unittest.TestCase):
    def test_database_logger_factory(self):
        factory = LoggerFactorySelector.get_logger_factory(
            'DatabaseLoggerFactory')
        self.assertIsInstance(factory, DatabaseLoggerFactory)
        logger = factory.create()
        self.assertIsInstance(logger, DatabaseLogger)

    def test_unsupported_logger_factory(self):
        factory = LoggerFactorySelector.get_logger_factory(
            'UnsupportedLoggerFactory')
        self.assertIsNone(factory)


if __name__ == '__main__':
    unittest.main()