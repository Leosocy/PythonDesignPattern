class Chart(object):
    
    def __init__(self, type):
        self._type = type
        if type.lower() == "histogram":
            print("初始化柱状图")
        elif type.lower() == "pie":
            print("初始化饼状图")
        elif type.lower() == "line":
            print("初始化折线图")

    def display(self):
        if self._type.lower() == "histogram":
            print("显示柱状图")
        elif self._type.lower() == "pie":
            print("显示化饼状图")
        elif self._type.lower() == "line":
            print("显示化折线图")

if __name__ == '__main__':
    histogram = Chart("histogram")
    histogram.display()