#! /usr/bin/env python

import sys
import numpy as np
np.set_printoptions(precision=4)


class PostHypotheses():
    """
    This class creates the 1D vectors required for testing
    the hypotheses in bayesian statistics. All variables are
    declared for debugging purposes, and testing against theory.
    """
    def __init__(self, prior=None, likelihood=None, toss=None):
        self.prior = np.array(prior, dtype=np.float32)
        # keep the prior bcs it will be updated if tosses > 1
        self.init_prior = self.prior
        self.likelihood = np.array(likelihood, dtype=np.float32)
        self.toss = np.array(toss, dtype=np.int)


    def posterior(self):
        """
        This function calculates all the vectors required in bayesian
        statistics. Currently all values are kept in variables for
        educational purposes. This will be omitted in future versions.
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
            if ts == 0:
                self.likelihood = np.subtract(1.0, self.likelihood)
        # set prior back to initial state before experiment starts
        self.prior = self.init_prior


    def print_formatted_output(self):
        """
        This function prints the formatted output along with information
        on the experiment.
        """
        print(f'For the experiment where the collected data are x={self.toss}.')
        for i, j, k in zip(self.likelihood, self.prior, self.posterior):
            print(f'Hypothesis \u03B8={i:.2f} with p(\u03B8)={j:.2f} has p(\u03B8|x)={k:.2f}.')        
        print(f'Vector output for the aforementioned hypotheses \u03B8: {self.posterior}')


class PostData(PostHypotheses):
    """
    Calculate posterior predictive probability on data that may emerge
    in a hypothetical execution of the experiment.
    """
    def __init__(self, prior=None, likelihood=None, toss=None, pred=None):
        super().__init__(prior, likelihood, toss)
        self.pred = pred


    def predictive(self):
        if self.pred == 0:
            self.likelihood = np.subtract(1.0, self.likelihood)
        self.pred_prob = np.dot(self.posterior, self.likelihood)
        self.likelihood = np.subtract(1.0, self.likelihood)


    def print_formatted_output(self):
        """
        This function prints the formatted output along with information
        on the experiment.
        """
        print(f'For the experiment where the collected data so far are x={self.toss}.')
        for i, j, k in zip(self.likelihood, self.prior, self.posterior):
            print(f'Hypothesis \u03B8={i:.2f} with p(\u03B8)={j:.2f} has p(\u03B8|x)={k:.2f}.')
        print(f'The probability that the next toss will be {self.pred} is p(x={self.pred}|x)={self.pred_prob:.4f}.')


def coins(infile):
    """
    This functions reads the experiment's information.
    These are:
    1. the coins' bias (theta) which is the likelihood
    2. the coins' prior (p_theta)
    3. the data from the experiment's execution (x vector)
    TODO: input format validation
    """
    
    pred = None
    with open(infile, 'r') as f:
        for line in f.readlines():
            vec = line.rstrip('\n').split(',')
            if vec[0] == 'theta':
                likelihood = vec[1:]
            elif vec[0] == 'prior':
                prior = vec[1:]
            elif vec[0] == 'toss':
                toss = vec[1:]
            elif vec[0] == 'predictive':
                pred = vec[1]

    try:
        if pred:
            exper = PostData(prior, likelihood, toss, pred)
            exper.posterior()
            exper.predictive()
            exper.print_formatted_output()
        else:
            exper = PostHypotheses(prior, likelihood, toss)
            exper.posterior()
            exper.print_formatted_output()
    except Exception as e:
        print(f'Error message concerning input file: {e}. Program exits.')
        sys.exit(-1)