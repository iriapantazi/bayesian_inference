### Utility for Bayesian Inference
---


## Introduction
The utility is built for solving the examples 1, 2, 3 from 
the [reading material 11](https://ocw.mit.edu/courses/mathematics/18-05-introduction-to-probability-and-statistics-spring-2014/readings/MIT18_05S14_Reading11.pdf) 
that can be found on the [MIT course 18.05: Introduction to probability and statistics](https://ocw.mit.edu/courses/mathematics/18-05-introduction-to-probability-and-statistics-spring-2014/readings/).
It can be used for solving the corresponding 
[reading questions](https://ocw.mit.edu/courses/mathematics/18-05-introduction-to-probability-and-statistics-spring-2014/readings/reading-questions-11/).
The input files from each example are:
 - ex1.csv
 - ex2.csv
 - ex3.csv
 - reading1.csv
 - reading2.csv


# Steps

1. Read the hypotheses.
  - These N hypotheses are expressed in numbers.
  - The numbers describe the coin bias. By default, it is 
    considered to be the probability of getting H 
    (heads, x=1) in a single toss.
  
2. Read hypotheses' probabilities
  - These probabilities consist the prior.
  - Sum of hypotheses' probabilities is unity.

# Notes
  - pandas dataframe is not used

## Contributions
If you have any suggestions/corrections,
please contact [Iria Pantazi](iria.a.pantazi@gmail.com).