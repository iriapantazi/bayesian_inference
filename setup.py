#! /usr/bin/env python

from distutils.core import setup

setup(name='simple_bayes',
      version='0.1',
      description='simple posterior bayesian inference',
      url='https://github.com/iriapantazi/simple_bayes',
      author='Iria Pantazi',
      author_email='iria.a.pantazi@gmail.com',
      license='MIT',
      packages=['simple_bayes'],
      data_files=[('data_files', ['data_files/example_coins.csv'])],
      )