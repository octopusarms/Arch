#!/usr/bin/env python

import pygame
import math

def findEqualSize(quantity, size, desired_dimensions, **kwargs):
    """findEqualSize takes quantity, number of shapes, size, region it will be contained in,
    desired_dimensions, favorable condition of dimensions, and **kwargs, a list of 'rules'
    and finds equal sizes, order, and shape of a rectangular/square region."""
    #quantity, size assigned
    self.quantity = quantity
    self.size = size

    width = desired_dimensions[0]
    height = desired_dimensions[1]
    
    #this is a list containing all the 
    try:
        pass

    pass


def sizeText(info, size, size_of_text):
    "The text will always be a mono-text."
    grow_text, shrink_text = size_of_text
    text = pygame.font.SysFont('ubuntumono', size_of_text, False, False)
    mono_text = 'ubuntumono'
    size_w, size_h = size[0], size[1]
    counter = 0
    size_of_info = len(info)
    permetations = []
    while True:
        text_size = text.size('z')
        amount_in_row = size_w / text_size
        amount_in_column = size_h / text_size
        amount_in_all = amount_in_row * amount_in_column
        if amount_in_all > size_of_info:
            permetations.append(text_size, grow_text, amount_in_all, amount_in_row, amount_in_column)
        else:
            counter += 1 

        grow_text += 1
        text = pygame.font.SysFont(mono_text, grow_text, False, False)

        if counter >= 3:
            break
    return permetations



def breakLines(info, size_per_line, total_size):
    "info is the data to be displayed
    size_per_line is the amount that can be contained per line
    total_size is the total amount given to obtain info

    takes info and the size_per_line and breaks info into those sizes per line"

    length_of_info = len(info)
    assert length_of_info < total_size
    iterations = math.ceil(length_of_info / size_per_line)
    sliced = []
    last_slice_max = 0
    for i in range(iterations):
        sliced.append(info[last_slice_max:i*size_per_line])

        last_slice_max = i*size_per_line

    return sliced


def choose(permetations, info_len):
    "This simply calculates left over space and chooses one with least left over space."
    keep = None
    size_of_last = None
    current = 0
    additive = 1
    for i in range(len(permetations)):
        first = permetations[current][2] - info_len
        second = permetations[i+additive][2] - info_len
        if first > second:
            keep = permetations[i+additive]
            current += 1
            if i > len(permetations)-1:
                additive= 0
        else:
            keep = permetations[current]
            if i > len(permetations) - 1:
                additive = 0
    return keep


