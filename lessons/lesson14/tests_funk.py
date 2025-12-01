import unittest

from funk import solve_quadratic_equation, shufle_list

class TestSolveQuadraticEquation(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("Початок тестування розв'язання квадратного рівняння.")
    @classmethod
    def tearDownClass(cls):
        print("Завершення тестування розв'язання квадратного рівняння.")
    
    def setUp(self):
        print("\tПочаток тесту.")
    def tearDown(self):
        print("\tЗавершення тесту.")
    def test_two_real_roots(self):
        print("\t\tТестування випадку з двома дійсними коренями.")
        result = solve_quadratic_equation(1, -3, 2)
        self.assertEqual(result, (2.0, 1.0))

    def test_one_real_root(self):
        print("\t\tТестування випадку з одним дійсним коренем.")
        result = solve_quadratic_equation(1, -2, 1)
        self.assertEqual(result, 1.0)

    def test_no_real_roots(self):
        print("\t\tТестування випадку без дійсних коренів.")
        result = solve_quadratic_equation(1, 0, 1)
        self.assertIsNone(result, "Рівняння не має дійсних коренів.")

    def test_not_quadratic_equation(self):
        print("\t\tТестування випадку, коли коефіцієнт 'a' дорівнює нулю.")
        result = solve_quadratic_equation(0, 2, 1)
        self.assertIsNone(result, "Коефіцієнт 'a' не може бути нулем для квадратного рівняння.")


class TestShuffleList(unittest.TestCase):
    __original_list = [1, 2, 3, 4, 5]
    
    def setUp(self):
        self.original_list = self.__original_list.copy()

    def test_shuffle_list(self):
        print("\t\tТестування функції перемішування списку.")

        result = shufle_list(self.original_list)
        self.assertCountEqual(result, self.__original_list, "Перемішаний список повинен містити ті ж елементи.")
        self.assertNotEqual(result, self.__original_list, "Перемішаний список повинен бути в іншому порядку.")
    def test_empty_list(self):
        print("\t\tТестування функції перемішування порожнього списку.")
        original_list = []
        from funk import shufle_list
        result = shufle_list(original_list)
        self.assertEqual(result, [], "Перемішування порожнього списку повинно повернути порожній список.")
    def test_single_element_list(self):
        print("\t\tТестування функції перемішування списку з одним елементом.")
        original_list = [42]
        from funk import shufle_list
        result = shufle_list(original_list)
        self.assertEqual(result, [42], "Перемішування списку з одним елементом повинно повернути той же список.")
if __name__ == "__main__":
    unittest.main()

