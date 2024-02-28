import unittest
from unittest.mock import Mock
from  Class import Pizza, CartePizzeria, CartePizzeriaException

class TestCartePizzeria(unittest.TestCase):
    def test_is_empty_true(self):
        c = CartePizzeria()
        self.assertTrue(c.is_empty())
    def test_is_empty_false(self):
        c = CartePizzeria()
        c.add_pizza(Mock(spec=Pizza))
        self.assertFalse(c.is_empty())
    def test_nb_pizza(self):
        c = CartePizzeria()
        c.add_pizza(Mock(spec=Pizza))
        c.add_pizza(Mock(spec=Pizza))
        c.add_pizza(Mock(spec=Pizza))
        c.add_pizza(Mock(spec=Pizza))
        self.assertEqual(c.nb_pizzas(),4)
    def test_add_pizza(self):
        c = CartePizzeria()
        c.add_pizza(Mock(spec=Pizza))
        self.assertEqual(c.nb_pizzas(),1)

__name__ == '__main__'
unittest.main()