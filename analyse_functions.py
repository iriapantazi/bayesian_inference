0#! /usr/bin/env python

import sys
import numpy as np


class Coins():
    """
    This class creates the 1D vectors required for testing
    the hypotheses in bayesian statistics. All variables are
    declared for debugging purposes, and testing against theory.
    """
    def __init__(self, prior=None, likelihood=None, toss=None):
        self.prior = np.array(prior, dtype=np.float32)
        self.likelihood = np.asarray(likelihood, dtype=np.float32)
        self.toss = np.asarray(toss, dtype=np.int)


    def posterior(self):
        """
        This function calculates all the vectors required in bayesian
        statistics.
        """
        for ts in self.toss:
            # change likelihood according to toss
            if ts == 0:
                self.likelihood = np.subtract(1.0, self.likelihood)
            self.numerator = self.prior * self.likelihood
            self.normalisation = np.dot(self.prior, self.likelihood)
            self.posterior = np.divide(self.numerator, self.normalisation)
            self.prior = self.posterior
            # return to initial likelihood so that it change if ts==0
            self.likelihood = np.subtract(1.0, self.likelihood)
        return(self.posterior)



def coins(infile):
    """
    This functions reads the experiment's information.
    These are:
    1. the coins' bias (theta)
    2. the coins' prior (p_theta)
    3. the data from the experiment's execution (chi vector)
    """
    with open('files/'+infile, 'r') as f:
        for line in f.readlines():
            # TODO: assert correct input format
            vec = line.rstrip('\n').split(',')
            if vec[0] == 'theta':
                likelihood = vec[1:]
            elif vec[0] == 'prior':
                prior = vec[1:]
            elif vec[0] == 'toss':
                toss = vec[1:]

    try:
        exper = Coins(prior, likelihood, toss)
        posterior = exper.posterior()
        for entry in posterior:
            print(f'{entry}')
    except Exception as e:
        print({e})
        print(f'Error message concerning input file: {e}. Program exits.')
        sys.exit(-1)