#!/usr/bin/env python


import pygame
import math
import __builtin__

class object(__builtin__.object):
    """This is the Base Object. It ids and classifies the object."""
    #Counter
    Object = 0
    def __init__(self, ):
        #Set the obj_id to a id number so it can later be identified by that number.
        self.obj_id = object.Object
        object.Object += 1


class TileID(object):
    """This is Tile Object. Sets the id for different type of tiles."""
    #This is the [Tile] variable. It is set at 0 to start the identification of its objects.
    Tile = 0
    def __init__(self, ):
        super(TileID, self).__init__()
        #Sets the [tile_id] to its value and increments the counter
        self.tile_id = TileID.Tile
        TileID.Tile += 1

