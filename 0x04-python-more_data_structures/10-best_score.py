#!/usr/bin/python3

def best_score(a_dictionary):
    if a_dictionary is None or not a_dictionary:
        return None

    else:
        best_score = max(a_dictionary, key=lambda x: a_dictionary[x])

        return best_score
