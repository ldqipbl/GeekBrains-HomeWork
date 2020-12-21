"""Unit-тесты клиента"""

import sys
import os
import unittest
from common.variables import RESPONSE, ERROR, USER, ACCOUNT_NAME, TIME, ACTION, PRESENCE
from client import create_presence, process_ans


class TestClass(unittest.TestCase):
    '''
    Класс с тестами
    '''

    def test_def_presense(self):
        """Тест коректного запроса"""
        test = create_presence()
        test[TIME] = 1.1  # время необходимо приравнять принудительно
                          # иначе тест никогда не будет пройден
        self.assertEqual(test, {ACTION: PRESENCE, TIME: 1.1, USER: {ACCOUNT_NAME: 'Guest'}})

    def test_200_ans(self):
        """Тест корректтного разбора ответа 200"""
        self.assertEqual(process_ans({RESPONSE: 200}), '200 : OK')

    def test_400_ans(self):
        """Тест корректного разбора 400"""
        self.assertEqual(process_ans({RESPONSE: 400, ERROR: 'Bad Request'}), '400 : Bad Request')

    def test_no_response(self):
        """Тест исключения без поля RESPONSE"""
        self.assertRaises(ValueError, process_ans, {ERROR: 'Bad Request'})


    def test_assert_equal(self):
        test = create_presence()
        self.assertEqual(test[ACTION], 'presence')

    def test_assert_true(self):
        test = create_presence()
        self.assertTrue(TIME)

    def test_assert_not_in(self):
        test = create_presence()
        self.assertNotIn(USER, ACCOUNT_NAME)

    def test_assert_is_not_none(self):
        test = create_presence()
        self.assertIsNotNone(TIME)


if __name__ == '__main__':
    unittest.main()
