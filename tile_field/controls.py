#!/usr/bin/env python


import __builtin__
import pygame
import sys, os
from COLORS import RED

from utility import sizeText, breakLines, choose
from math import floor

class Control(__builtin__.object):
    "This is the base class for all the 'controls' -- buttons, widgets, etc."
    categories = {}
    def __init__(self, size, pos, category):
        super(Control, self).__init__()
        self.size = size
        self.pos = pos
        self.x, self.y = pos


class piece(__builtin__.object):
    "an information piece that will give info about a button that is hovered over."
    def __init__(self, info, size, ):
        size_of_text = 5
        super(piece, self).__init__()
        permetations = sizeText(info, size, size_of_text)
        chosen_size = choose(permetations)
        self.ordered_sliced = breakLines(info, permetations[3], permetations[2])

        self.piece = pygame.Surface(size)
        self.piece_rect = piece.get_rect()
    
    def paste_to_piece_screen(self, ):
        for i in range(len(self.ordered_sliced)):
           self.ordered_sliced[i] 


        
class hover(piece):
    "this feature allows for the hovering of controls
    and the effects produced when hovering over that control."
    def __init__(self, control, highlight=False hover_color=(255, 0, 0, 125)):
        super(hover, self).__init__(control.get_size(), control.get_rect().xy)
        self.hover_control = pygame.Surface(control.get_size()).convert_alpha()
        self.hover_control_rect = self.hover_control.get_rect()
        self.hover_control.fill(hover_color)
    def update(self, core_button ):
        "core_button is the corresponding 'control' that inherited hover"




class Button(Control, hover):
    "This is Button class and it is a button."

    def __init__(self, size, pos=(0, 0), information=''):
        super(Button, self).__init__(size, pos)
        self.button = pygame.Surface(size).convert_alpha()
        self.button_rect = self.button.get_rect()

        

    def hover(self, ):
        pass

    def click(self, mouse_clicked=False):

        if mouse_clicked: 
            if self.button_rect.collidepoint(pygame.mouse.get_pos())

    def info(self, ):
        pass

    def update(self, ):

