from game.world.worldGenerator import worldGenerator
from OpenGL.GL import *

from functions import roundPos, cube_vertices, adjacent
from game.items.Item import Item


class ItemHandler:

    def __init__(self, batch, item, opaque, alpha_textures, gl):
        self.batch, self.item, self.alpha_textures, self.opaque = batch, item, alpha_textures, opaque
        self.transparent = gl.transparent
        self.gl = gl


        self.color = True
