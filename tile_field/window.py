#!/usr/bin/env python


import pygame
import __builtin__

class Window(__builtin__.object):
    "Window class contained by Frames that hold buttons and widgets etc."
    def __init__(self, size, pos=(0, 0), **kwargs):
        self.size = size
        self.Window = pygame.Surface(size)
        self.buttons = []
        self.widgets = []
        buttons = kwargs.get('buttons')
        widgets = kwargs.get('widgets')

        self.pos = pos
        self.x, self.y =  pos

        if kwargs:
            if buttons:
                self.add_button(buttons, True)
            elif widgets:
                self.add_widget(widgets, True)

    def add_button(self, button, sequence=False):
        if sequence:
            self.buttons = button
        elif not sequence:
            self.buttons.append(button)


    def add_widget(self, widget, sequence=False):
        if sequence:
            self.widgets = widget
        elif not sequence:
            self.widgets.append(widget)


    def draw_controls(self, ):
        

    def update(self, ):
        pass

