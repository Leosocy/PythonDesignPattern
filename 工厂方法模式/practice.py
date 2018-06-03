from abc import ABCMeta, abstractmethod
import unittest


class ImageReader(object):
    @abstractmethod
    def read(self, image_path):
        pass


class JpgImageReader(ImageReader):
    def read(self, image_path):
        print("Read jpg image:%s" % (image_path))


class GifImageReader(ImageReader):
    def read(self, image_path):
        print("Read gif image:%s" % (image_path))


class ImageReaderFactory(object):
    @abstractmethod
    def create(self):
        pass


class JpgImageReaderFactory(ImageReaderFactory):
    def create(self):
        return JpgImageReader()


class GifImageReaderFactory(ImageReaderFactory):
    def create(self):
        return GifImageReader()


class ImageReaderFactorySelector(object):
    @staticmethod
    def get_image_reader_factory(reader_type):
        for sc in ImageReaderFactory.__subclasses__():
            if sc.__name__ == reader_type:
                return sc()
        return None


class ImageReaderTests(unittest.TestCase):
    def test_jpg_reader(self):
        factory = ImageReaderFactorySelector.get_image_reader_factory(
            'JpgImageReaderFactory')
        self.assertIsInstance(factory, JpgImageReaderFactory)
        reader = factory.create()
        self.assertIsInstance(reader, JpgImageReader)
        reader.read('test.jpg')


if __name__ == '__main__':
    unittest.main()