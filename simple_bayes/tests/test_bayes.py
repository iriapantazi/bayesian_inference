#! /usr/bin/env python

import unittest
from unittest.mock import patch
import simple_bayes.bayes as simba


class Testing(unittest.TestCase):

    def test_detect_python_version(self):
        """
        need to suppress
        """
        patcher = patch('sys.version_info', major=2)
        patcher.start()
        with self.assertRaises(SystemExit):
            simba.detect_python_version()

    """
    Testing parser.
    """


    """
    Testing main function.
    """

if __name__ == '__main__':
    unittest.main()