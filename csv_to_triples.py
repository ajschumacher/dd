#!/usr/bin/env python

import sys
import dd


if __name__ == '__main__':
    trips = dd.filename_to_triple_set(sys.argv[1])
    for trip in trips:
        print(trip)
