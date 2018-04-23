#!/usr/bin/env python

import __builtin__
import pygame


class Frame(__builtin__.object):
    "This is the Frame class. It sets up preferences for a Frame -- a container for \
            windows which hold Widgets and buttons. A frame can hold other frames and 
            can not be the exact size as the screen(pygame.display) but it's initial Mother
            frame must reflect the screen."
            
    def __init__(self, ):
        super(Frame, self).__init__()
        #set 
        self.Frame = pygame.Rect(pygame.display.get_surface().get_rect())
        self.windows = []

    def add_window(self, window):
        self.windows.append(window)
    def blit_to_surface(self, a_list):
        if self.windows:
            for window in range(len(self.windows)):
                pygame.display.get_surface().blit(window.Window, (window.x, window.y))
    def update(self, ):
        pygame.display.get_surface().fill(pygame.Color('white'))

        self.blit_to_surface()



class MotherFrame(Frame):
    "Motherframe will 
