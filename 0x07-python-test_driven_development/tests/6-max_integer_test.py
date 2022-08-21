#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def test_no_arg(self):
        self.assertEqual(max_integer(), None)

    def test_empty_list(self):
        self.assertEqual(max_integer([]), None)

    def test_string(self):
        self.assertEqual(max_integer("string"), 't')

    def test_max_at_middle(self):
        self.assertEqual(max_integer([3,4,8,22,12,6,13]), 22)

    def test_max_at_end(self):
        self.assertEqual(max_integer([3,4,8,9,12,6,18]), 18)

    def test_max_at_beginning(self):
        self.assertEqual(max_integer([25,3,4,8,9,12,6,13]), 25)

    def test_one_negative_number(self):
        self.assertEqual(max_integer([3,-34,4,8,19,12,6,13]), 19)

    def test_all_negative(self):
        self.assertEqual(max_integer([-3, -6, -17, -2, -12, -4]), -2)

    def test_list_of_one(self):
        self.assertEqual(max_integer([12]), 12)


