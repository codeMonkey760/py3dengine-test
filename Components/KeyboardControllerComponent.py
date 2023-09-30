import py3dengine
import py3dinput
import py3dmath


class KeyboardControllerComponent(py3dengine.Component):
    def __init__(self):
        super().__init__()
        self.speed = 1
        self.owner = None

    def start(self):
        self.owner = self.get_owner()

    def update(self, dt):
        x = 0
        y = 0
        z = 0
        if py3dinput.is_key_pressed(65):
            x = x - 1
        if py3dinput.is_key_pressed(68):
            x = x + 1
        if py3dinput.is_key_pressed(67):
            y = y - 1
        if py3dinput.is_key_pressed(32):
            y = y + 1
        if py3dinput.is_key_pressed(83):
            z = z - 1
        if py3dinput.is_key_pressed(87):
            z = z + 1

        displacement = py3dmath.Vector3(x, y, z)
        try:
            displacement = displacement.normalize()
        except ZeroDivisionError:
            return

        displacement = displacement * (self.speed * dt)

        displacement = displacement * self.owner.get_orientation()
        self.owner.move(displacement)

    def parse(self, values, resource_manager):
        super().parse(values, resource_manager)

        self.speed = float(values['speed'])
