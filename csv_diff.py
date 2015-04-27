#!/usr/bin/env python

import sys
import dd


def diff_print(symbol, things):
    for thing in things:
        print(symbol, thing)

if __name__ == '__main__':
    left = dd.filename_to_triple_set(sys.argv[1])
    right = dd.filename_to_triple_set(sys.argv[2])
    left_only = left - right
    diff_print("<", left_only)
    print("---")
    right_only = right - left
    diff_print(">", right_only)
