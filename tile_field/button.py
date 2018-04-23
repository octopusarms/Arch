#!/usr/bin/env python


import __builtin__
import pygame
import sys, os


class Button(__builtin__.object):
    "This is Button class and it is a button."

    def __init__(self, size, information):
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
