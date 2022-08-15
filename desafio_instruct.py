#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'automated_readability_index' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING sentence as parameter.
#

def automated_readability_index(sentence):
    words = sentence.split(' ')
    number_of_words = len(words)
    number_of_letters = len(sentence) - (number_of_words - 1)

    result = math.ceil(4.71 * (number_of_letters / number_of_words) + 0.5 * (number_of_words / 1) - 21.43)

    if result > 14:
        result = 14

    return result


sentence = input()

print(automated_readability_index(sentence))
