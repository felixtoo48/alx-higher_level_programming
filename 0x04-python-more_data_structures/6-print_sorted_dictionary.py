#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    for kv in sorted(a_dictionary.items()):
        print(kv[0], ':', kv[1])
