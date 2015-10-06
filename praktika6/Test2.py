__author__ = 'student'
# Подключаем библиотеку для тестирования
import unittest
# Подключаем тестируемую библиотеку
import lib

# Класс, описывающий набор тестов
class LibTest(unittest.TestCase):

    # Тестируем работу sqrt с положительными аргументами
    def test_even_non_negative_arg(self):
        # Набор проверок
        self.assertEqual(lib.even(9), 0)
        self.assertEqual(lib.even(1), 0)
        self.assertEqual(lib.even(8), 1)
        self.assertEqual(lib.even(0), 1)
        self.assertEqual(lib.even(-2), 1)
        self.assertEqual(lib.even(-3), 0)


    def test_sqrt_negative(self):
        # Набор проверок
        self.assertEqual(lib.sqrt(0), 0)


# Запускаем тесты на исполнение
unittest.main(verbosity=2)
