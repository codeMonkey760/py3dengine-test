import py3dengine
import py3dinput
from py3dmath import Quaternion, Vector3


class MouseControllerComponent(py3dengine.Component):
    def __init__(self):
        super().__init__(self)
        self.x_sens = 1.0
        self.y_sens = 1.0
        self.last_pos = None

    def update(self, dt):
        cur_pos = py3dinput.get_cursor_pos()

        if self.last_pos is None:
            self.last_pos = cur_pos
            return

        delta = (cur_pos[0] - self.last_pos[0], cur_pos[1] - self.last_pos[1])
        self.last_pos = cur_pos

        try:
            transform = self.get_owner().get_transform()
        except AttributeError:
            transform = None
        if transform is None:
            return

        pitch = Quaternion.FromAxisAndDegrees(Vector3(1.0, 0.0, 0.0), delta[1] * self.y_sens)
        yaw = Quaternion.FromAxisAndDegrees(Vector3(0.0, 1.0, 0.0), delta[0] * self.x_sens)

        transform.set_orientation((pitch * yaw))

    def parse(self, values, resource_manager):
        self.x_sens = values['x_sensitivity']
        self.y_sens = values['y_sensitivity']
