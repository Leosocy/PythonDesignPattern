from abc import ABCMeta, abstractmethod


class Button(metaclass=ABCMeta):
    @abstractmethod
    def display(self):
        pass


class SpringButton(Button):
    def display(self):
        print('浅绿色按钮')


class SummerButton(Button):
    def display(self):
        print('浅蓝色按钮')


class ButtonFactory(metaclass=ABCMeta):
    @abstractmethod
    def create(self):
        pass


class SpringButtonFactory(ButtonFactory):
    def create(self):
        return SpringButton()


class SummerButtonFactory(ButtonFactory):
    def create(self):
        return SummerButton()


class TextField(metaclass=ABCMeta):
    @abstractmethod
    def display(self):
        pass


class SpringTextField(TextField):
    def display(self):
        print('绿色边框文本框')


class SummerTextField(TextField):
    def display(self):
        print('蓝色边框文本框')


class TextFieldFactory(metaclass=ABCMeta):
    @abstractmethod
    def create(self):
        pass


class SpringTextFieldFactory(TextFieldFactory):
    def create(self):
        return SpringTextField()


class SummerTextFieldFactory(TextFieldFactory):
    def create(self):
        return SummerTextField()


class ComboBox(metaclass=ABCMeta):
    @abstractmethod
    def display(self):
        pass


class SpringComboBox(ComboBox):
    def display(self):
        print('绿色边框组合框')


class SummerComboBox(ComboBox):
    def display(self):
        print('蓝色边框组合框')


class ComboBoxFactory(metaclass=ABCMeta):
    @abstractmethod
    def create(self):
        pass


class SpringComboBoxFactory(ComboBoxFactory):
    def create(self):
        return SpringComboBox()


class SummerComboBoxFactory(ComboBoxFactory):
    def create(self):
        return SummerComboBox()


class Client(object):
    def display(self):
        button_factory = SpringButtonFactory()
        button = button_factory.create()
        button.display()
        text_field_factory = SpringTextFieldFactory()
        text_field = text_field_factory.create()
        text_field.display()
        combo_box_factory = SpringComboBoxFactory()
        combo_box = combo_box_factory.create()
        combo_box.display()


if __name__ == '__main__':
    client = Client()
    client.display()