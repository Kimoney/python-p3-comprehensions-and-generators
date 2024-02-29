#!/usr/bin/env python3

def return_evens(num_list):
    # list comprehension :) ... I love one liners :-D
    evens = [num for num in num_list if (num % 2 == 0)]
    return evens  

def make_exclamation(sentence_list):
    # list comprehension :) another amazing one liner :_D
    exclamatory = [sentence + "!" for sentence in sentence_list]
    return exclamatory