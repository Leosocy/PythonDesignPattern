from abc import ABCMeta, abstractmethod
import unittest


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


class SkinFactory(object):
    @abstractmethod
    def create_button(self):
        pass

    @abstractmethod
    def create_text_field(self):
        pass

    @abstractmethod
    def create_combo_box(self):
        pass


class SpringSkinFactory(SkinFactory):
    def create_button(self):
        return SpringButton()

    def create_text_field(self):
        return SpringTextField()

    def create_combo_box(self):
        return SpringComboBox()


class SummerSkinFactory(SkinFactory):
    def create_button(self):
        return SummerButton()

    def create_text_field(self):
        return SummerTextField()

    def create_combo_box(self):
        return SummerComboBox()


class SkinFactorySelector(object):
    @staticmethod
    def get_skin_factory(skin_type):
        for sc in SkinFactory.__subclasses__():
            if sc.__name__ == skin_type:
                return sc()
        raise RuntimeError('Unsupported Skin Type')


class Client(object):
    def display(self, skin_type):
        factory = SkinFactorySelector.get_skin_factory('SpringSkinFactory')
        button = factory.create_button()
        text_field = factory.create_text_field()
        combo_box = factory.create_combo_box()
        button.display()
        text_field.display()
        combo_box.display()


class SKinTests(unittest.TestCase):
    def test_spring_skin_factory(self):
        factory = SkinFactorySelector.get_skin_factory('SpringSkinFactory')
        self.assertIsInstance(factory, SpringSkinFactory)

    def test_unsupported_skin_type(self):
        self.assertRaises(RuntimeError,
                          SkinFactorySelector.get_skin_factory,
                          'Unsupported')


if __name__ == '__main__':
    unittest.main()
