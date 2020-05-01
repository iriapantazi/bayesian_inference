#! /usr/bin/env python

import unittest
from unittest.mock import patch
import simple_bayes.analysis_functions as afun
from simple_bayes.bayes import COINS_FILE

class Testing(unittest.TestCase):

    def test_coins(self):
        afun.coins(COINS_FILE)
        with self.assertRaises(Exception):
            afun.coins('invalid_example.csv')


if __name__ == '__main__':
    unittest.main()