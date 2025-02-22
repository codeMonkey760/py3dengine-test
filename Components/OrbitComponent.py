import py3dengine
from py3dmath import Vector3, Quaternion
import math


class OrbitComponent(py3dengine.Component):
    def __init__(self):
        super().__init__()

        self.speed = 0.0
        self.axis = None
        self.radius = 0.0
        self.theta = 0.0
        self.owner = None

    def start(self):
        self.owner = self.get_owner()

    def update(self, dt):
        self.theta += math.radians(self.speed) * dt
        while self.theta >= math.tau:
            self.theta -= math.tau

        displacement = Vector3(math.cos(self.theta), 1.0, math.sin(self.theta))
        displacement *= self.radius

        self.owner.set_position(displacement)

    def parse(self, values, rm):
        super().parse(values, rm)

        self.speed = float(values['speed'])
        self.radius = float(values['radius'])

        x = float(values['axis']['x'])
        y = float(values['axis']['y'])
        z = float(values['axis']['z'])
        self.axis = Vector3(x, y, z)