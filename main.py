import sys
import argparse

from my_package.homework import *

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--number', dest='n', required=True, type=int, help='Hello')
    result = parser.parse_args()
    print(sys.argv, result)
    print('Factorial', factorial(result.n))

