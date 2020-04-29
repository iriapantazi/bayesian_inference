#! /usr/bin/env python

import sys
import argparse
import analysis_functions as af

# constants
COINS_FILE = 'files/coins.csv'

def detect_python_version():
    """
    """
    if sys.version_info.major < 3:
        print(f'Python {sys.version_info.major} '
                f'is not supported. Program exits.')
        sys.exit(-1)


def parse_arguments():
    """
    parse_arguments:
    Args: -
    Returns: args [str]
    """
    parser = argparse.ArgumentParser(
                description='Calculate probabilities of hypotheses '
                'based on existing data that the user provides. '
                'This applies to the problem of tossing a (un)biased '
                'coin and recording the result.'
                )
    parser.add_argument('-i', '--input', nargs='?', const=COINS_FILE, 
                help='read input file')
    args = parser.parse_args()
    return(args)  


def main(args=None):
    """
    main:
    Args: -
    Returns: -
    """

    # to be included in web API endpoint
    if args == None:
        args = parse_arguments()

    # coin input
    if args.input:
        af.coins(args.input)
    else:
        print(f'No mode was provided, please see help. Program exits.')
        sys.exit(-1)


if __name__ == '__main__':
    detect_python_version()
    main()
