#!/usr/bin/env python


import pygame
from objects import TileID
from constants import RED, GREEN, BLUE, PURPLE, COBALT

from mapgrabber import grabber

class Tile(TileID):
    """Tile is a base representation of any visible/invisible 'graphics' object."""
    def __init__(self, size, pos, color=COBALT):
        super(Tile, self).__init__()
        self.tile = pygame.Surface(size).convert_alpha()
        self.tile_rect = self.tile.get_rect()
        self.tile.fill(color)


class TileSystem(object):
    """This is the TileSystem. It will make instances of this for maps etc."""

    def __init__(self, ):
        super(TileSystem, self).__init__()
        self.rect_list = []
        self.big_rect = None


    def generate_rect_list(self, 
