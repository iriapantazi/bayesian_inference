#! /usr/bin/env python

import unittest
from unittest.mock import patch
from simple_bayes.bayes import COINS_FILE
import simple_bayes.analysis_functions as afun
from simple_bayes.analysis_functions import PostHypotheses, PostData
import numpy as np

class Testing(unittest.TestCase):

    def test_coins(self):
        """
        """
        with self.assertRaises(SystemExit):
            afun.coins('data_files/invalid_example.csv')


    def test_class_postHypotheses(self):
        """
        """
        likelihood = [0.5, 0.6, 0.9] # theta
        prior = [0.4, 0.4, 0.2]
        toss = [1, 1]
        returned = PostHypotheses(prior, likelihood, toss)
        self.assertCountEqual(returned.likelihood, np.array(likelihood, dtype=np.float32))
        self.assertCountEqual(returned.prior, np.array(prior, dtype=np.float32))
        self.assertCountEqual(returned.toss, np.array(toss, dtype=np.int))
        returned.posterior()
        self.assertCountEqual(returned.likelihood, np.array(likelihood, dtype=np.float32))
        self.assertCountEqual(returned.prior, np.array(prior, dtype=np.float32))
        self.assertCountEqual(returned.toss, np.array(toss, dtype=np.int))
        # compare posteriors up to 3 digits
        p_exp = [0.2463, 0.3547, 0.399]
        p_ret = list(returned.posterior)
        for i, j in zip(p_exp, p_ret):
            self.assertAlmostEqual(i, j, places=3)


    def test_class_postData(self):
        """
        """
        likelihood = [0.5, 0.6, 0.9] # theta
        prior = [0.4, 0.4, 0.2]
        toss = [1, 1]
        pred = 1

        returned = PostData(prior, likelihood, toss)
        self.assertCountEqual(returned.likelihood, np.array(likelihood, dtype=np.float32))
        self.assertCountEqual(returned.prior, np.array(prior, dtype=np.float32))
        self.assertCountEqual(returned.toss, np.array(toss, dtype=np.int))
        returned.posterior()
        self.assertCountEqual(returned.likelihood, np.array(likelihood, dtype=np.float32))
        self.assertCountEqual(returned.prior, np.array(prior, dtype=np.float32))
        self.assertCountEqual(returned.toss, np.array(toss, dtype=np.int))
        # compare posteriors up to 3 digits
        p_exp = [0.2463, 0.3547, 0.399]
        p_ret = list(returned.posterior)
        for i, j in zip(p_exp, p_ret):
            self.assertAlmostEqual(i, j, places=3)        
        

if __name__ == '__main__':
    unittest.main()