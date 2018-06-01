from abc import ABCMeta, abstractmethod
import unittest

class DrawingTool(object, metaclass=ABCMeta):

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def draw(self):
        pass

    @abstractmethod
    def erase(self):
        pass


class CircleDrawingTool(DrawingTool):

    def __init__(self):
        print("初始化圆形绘图工具")

    def draw(self):
        print("绘制圆形")

    def erase(self):
        print("擦除圆形")


class SquareDrawingTool(object):

    def __init__(self):
        print("初始化方形绘图工具")

    def draw(self):
        print("绘制方形")

    def erase(self):
        print("擦除方形")


class TriangleDrawingTool(object):

    def __init__(self):
        print("初始化三角形绘图工具")

    def draw(self):
        print("绘制三角形")

    def erase(self):
        print("擦除三角形")


class DrawingToolFactory(object):

    @staticmethod
    def create(drawing_tool_type):
        if drawing_tool_type.lower() == 'circle':
            return CircleDrawingTool()
        elif drawing_tool_type.lower() == 'square':
            return SquareDrawingTool()
        elif drawing_tool_type.lower() == 'triangle':
            return TriangleDrawingTool()
        else:
            raise RuntimeError('Unsupported Drawing Tool Type!')

class DrawingToolTests(unittest.TestCase):

    def test_supported_drawing_tool_type(self):
        drawing_tool = DrawingToolFactory.create('triangle')
        self.assertIsInstance(drawing_tool, TriangleDrawingTool)

    def test_unsupported_drawing_tool_type(self):
        self.assertRaises(RuntimeError, DrawingToolFactory.create, 'unsupported')

if __name__ == '__main__':
    unittest.main()