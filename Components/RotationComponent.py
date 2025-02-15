import py3dengine
from py3dmath import Vector3, Quaternion


class RotationComponent(py3dengine.Component):
    def __init__(self):
        super().__init__()
        self.speed = 0.0
        self.axis = Vector3(0, 0, 1)
        self.owner = None

    def start(self):
        self.owner = self.get_owner()

    def update(self, dt):
        displacement = Quaternion.FromAxisAndDegrees(self.axis, self.speed * dt)
        self.owner.rotate(displacement)

    def parse(self, values, resource_manager):
        super().parse(values, resource_manager)

        self.speed = float(values['speed'])
        x = float(values['axis']['x'])
        y = float(values['axis']['y'])
        z = float(values['axis']['z'])

        self.axis = Vector3(x, y, z)
