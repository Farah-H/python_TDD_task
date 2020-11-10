# importing necessary modules and files
from divisible_class import Divisible
import unittest
import pytest

# defining testing class, which is a child of unittest.TestCase
class TestDivisible(unittest.TestCase):

    # instantiating the Divisible class so we can test it
    divisible_instance = Divisible()


    # test fails if the function returns false, when 5 is indeed a multiple of 10. 
    def test_divisible(self):
        self.assertEqual(self.divisible_instance.divisible(10,5), True)