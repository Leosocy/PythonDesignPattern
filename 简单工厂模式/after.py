from abc import abstractmethod, ABCMeta

class Chart(metaclass=ABCMeta):
    """
    """

    @abstractmethod
    def __init__(self):
        pass
        
    @abstractmethod
    def display(self):
        pass


class HistogramChart(Chart):
    """
    """

    def __init__(self):
        print("初始化柱状图")

    def display(self):
        print("显示柱状图")


class PieChart(Chart):
    """
    """

    def __init__(self):
        print("初始化饼状图")

    def display(self):
        print("显示饼状图")


class LineChart(Chart):
    """
    """

    def __init__(self):
        print("初始化折线图")

    def display(self):
        print("显示折线图")

class ChartFactory(object):
    
    def create(self, chart_type):
        for sc in Chart.__subclasses__():
            if sc.__name__ == chart_type:
                return sc()
                

if __name__ == '__main__':
    chart_factory = ChartFactory()
    chart = chart_factory.create("HistogramChart")
    chart.display()