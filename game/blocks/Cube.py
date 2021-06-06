class Cube:
    def __init__(self, name, p, t, typ):
        self.name, self.p, self.t, self.type = name, p, t, typ
        self.color = {'left': None, 'right': None, 'bottom': None, 'top': None, 'back': None, 'front': None}
        self.shown = {'left': False, 'right': False, 'bottom': False, 'top': False, 'back': False, 'front': False}
        self.faces = {'left': None, 'right': None, 'bottom': None, 'top': None, 'back': None, 'front': None}
        #self.position = x, y, z

    def x(self):
        return self.position[0]

    def y(self):
        return self.position[1]

    def z(self):
        return self.position[2]
