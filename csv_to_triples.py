#!/usr/bin/env python

import sys
import dd


if __name__ == '__main__':
    # default to using `index` as ID column for now
    lod = dd.handle_to_list_of_dicts(sys.stdin)
    trips = dd.list_of_dicts_to_triple_set(lod, 'index')
    for trip in trips:
        print(trip)
