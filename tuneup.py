#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Tuneup assignment

Use the timeit and cProfile libraries to find bad code.
"""

__author__ = "John Wilkinson / stackOverFlow and google, and 1 on 1 with Amanda Yonce"

import cProfile
import pstats
import functools
import timeit
import io
from pstats import SortKey

def decorator_profile(func):
    """A cProfile decorator function that can be used to
    measure performance.
    """
    def profile_performance(*args, **kwargs):
        prof = cProfile.Profile()
        prof.enable()
        func(*args, **kwargs)
        prof.disable()
        s = io.StringIO()
        sort_by = SortKey.CUMULATIVE
        ps = pstats.Stats(prof, stream=s).sort_stats(sort_by)
        ps.print_stats()
        print(s.getvalue())
        return ps
    return profile_performance
    # Be sure to review the lesson material on decorators.
    # You need to understand how they are constructed and used.


def read_movies(src):
    """Returns a list of movie titles."""
    print(f'Reading file: {src}')
    with open(src, 'r') as f:
        return f.read().splitlines()


def is_duplicate(title, movies):
    """Returns True if title is within movies list."""
    for movie in movies:
        if movie.lower() == title.lower():
            return True
    return False


def find_duplicate_movies(src):
    """Returns a list of duplicate movies from a src list."""
    movies = read_movies(src)
    duplicates = []
    while movies:
        movie = movies.pop()
        if movie in movies:
            duplicates.append(movie)
    return duplicates


def timeit_helper(func):
    """Part A: Obtain some profiling measurements using timeit."""
    t = timeit.Timer(func)
    result = t.repeat(repeat = 7, number=3)
    # print(result) 
    aanswer = map(lambda x: x/3, result)
    minlist = list(aanswer)
    # print(minlist)
    smallest = min(minlist)
    # print(smallest)
    output = (f'Best time across 7 repeats of 3 runs per repeat: {smallest} sec')
    print(output)
    return output

@decorator_profile
def main():
    """Computes a list of duplicate movie entries."""
    result = find_duplicate_movies('movies.txt')
    print(f'Found {len(result)} duplicate movies:')
    print('\n'.join(result))

# timeit_helper(main)

if __name__ == '__main__':
    main()
