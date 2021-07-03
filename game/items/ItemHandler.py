from game.world.worldGenerator import worldGenerator
from OpenGL.GL import *

from game.items.Item import Item


class ItemHandler:
    top_color = ('c3f', (1.0,) * 12)
    ns_color = ('c3f', (0.8,) * 12)
    ew_color = ('c3f', (0.6,) * 12)
    bottom_color = ('c3f', (0.5,) * 12)

    def __init__(self, batch, item, opaque, alpha_textures, gl):
        self.batch, self.item, self.alpha_textures, self.opaque = batch, item, alpha_textures, opaque
        self.items = {'diamond_sword'}
        self.items = {}
        self.transparent = gl.transparent
        self.gl = gl
        self.fluids = {}
        self.collidable = {}
        self.gravity = {}

        '''self.top_color = ('c3f', (0.1,) * 12)
        self.ns_color = ('c3f', (0.1,) * 12)
        self.ew_color = ('c3f', (0.1,) * 12)
        self.bottom_color = ('c3f', (0.1,) * 12)'''

        self.color = True

    def hitTest(self, p, vec, dist=4):
        m = 8
        x, y, z = p
        dx, dy, dz = vec
        dx /= m
        dy /= m
        dz /= m
        prev = None
        return None, None

    def show(self, v, t, i, clrC=None):
        if not clrC:
            if self.color:
                if i == "left" or i == "front":
                    clr = self.ns_color
                if i == "right" or i == "back":
                    clr = self.ew_color
                if i == "bottom":
                    clr = self.bottom_color
                if i == "top":
                    clr = self.top_color
        else:
            clr = clrC[i]

        return self.opaque.add(4, GL_QUADS, t, ('v3f', v), ('t2f', (0, 0, 1, 0, 1, 1, 0, 1)), clr)

    def updateItem(self, item, customColor=None):
        shown = any(item.shown.values())
        if shown:
            if (item.name != 'water' and item.name != 'lava' and item.name != 'fire') and item.p not in self.collidable:
                self.collidable[item.p] = item
            elif item.p in self.gravity:
                print("smth will happen later :)")
        else:
            if item.p in self.collidable:
                del self.collidable[item.p]
            return

        show = self.show

    def set_adj(self, item, adj, state):
        x, y, z = item.p
        X, Y, Z = adj
        d = X - x, Y - y, Z - z
        f = 'left', 'right', 'bottom', 'top', 'back', 'front'
        for i in (0, 1, 2):
            if d[i]:
                j = i + i
                a, b = [f[j + 1], f[j]][::d[i]]
                item.shown[a] = state
                if not state and item.faces[a]:
                    item.faces[a].delete()
                    face = item.faces[a]
                    item.faces[a] = None

    def add(self, p, t, now=False):
        if p in self.items or self.items[p].name == "diamond_sword":
            return
        item = self.items[p] = Item(t, p, self.item[t],
                                    'alpha' if t in self.alpha_textures else 'blend' if (t =="diamond_sword")
                                    else 'solid')


        #for adj in adjacent(*item.p):
        #    if adj not in self.items:
        #        self.set_adj(item, adj, True)
        #    else:
        #        a, b = item.type, self.items[adj].type
        #        if a == b and (a == 'solid' or b == 'blend'):
        #            self.set_adj(self.items[adj], item.p, False)
        #        elif a != 'blend' and b != 'solid':
        #            self.set_adj(self.items[adj], item.p, False)
        #            self.set_adj(item, adj, True)
        #        if now:
        #            self.updateitem(self.items[adj])

        if now:
            self.updateitem(item)

    def remove(self, p):
        if p not in self.items:
            return
        if p in self.fluids:
            self.fluids.pop(p)
        item = self.items.pop(p)

        for side, face in item.faces.items():
            if face:
                face.delete()
            item.shown[side] = False
        self.updateitem(item)
