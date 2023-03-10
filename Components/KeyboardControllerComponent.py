import py3dengine
import py3dinput
import py3dmath


class KeyboardControllerComponent(py3dengine.Component):
    def __init__(self):
        super().__init__(self)
        self.speed = 1

    def update(self, dt):
        x = 0
        z = 0
        if py3dinput.is_key_pressed(65):
            x = x - 1
        if py3dinput.is_key_pressed(68):
            x = x + 1
        if py3dinput.is_key_pressed(83):
            z = z - 1
        if py3dinput.is_key_pressed(87):
            z = z + 1

        displacement = py3dmath.Vector3(x, 0, z)
        try:
            displacement = displacement.normalize()
        except ZeroDivisionError:
            return

        displacement = displacement * self.speed

        transform = self.get_owner().get_transform()
        transform.move(displacement)

    def parse(self, values, resource_manager):
        self.speed = float(values['speed'])
