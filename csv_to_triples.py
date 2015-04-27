#!/usr/bin/env python

import sys, csv

# currently loading everything into memory
# rather than going line-by-line


def handle_to_list_of_dicts(handle):
    reader = csv.DictReader(handle)
    return reader


def list_of_dicts_to_triple_set(lod, id_name):
    ids = set()
    triple_set = set()
    for d in lod:
        if id_name not in d:
            raise Exception('entity does not have ID ' + id_name)
        current_id = d[id_name]
        if current_id in ids:
            raise Exception('ID ' + current_id + 'is not unique')
        ids.add(current_id)
        for prop, value in d.iteritems():
            if prop == id_name:
                continue
            triple_set.add((current_id, prop, value))
    return triple_set

if __name__ == '__main__':
    # default to using `index` as ID column for now
    lod = handle_to_list_of_dicts(sys.stdin)
    trips = list_of_dicts_to_triple_set(lod, 'index')
    for trip in trips:
        print trip
