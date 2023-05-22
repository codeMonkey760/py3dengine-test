from py3dengine import Component
from py3dinput import get_cursor_pos
from py3dmath import Quaternion, Vector3


class MouseControllerComponent(Component):
    def __init__(self):
        super().__init__()
        self.__current_yaw = 0.0
        self.__current_pitch = 0.0
        self.x_sens = 1.0
        self.y_sens = 1.0
        self.last_pos = None
        self.transform = None

    def start(self):
        super().start()

        self.last_pos = get_cursor_pos()
        self.transform = self.get_owner().get_transform()

    def update(self, dt):
        cur_pos = get_cursor_pos()

        self.__current_yaw = self.__current_yaw + ((cur_pos[0] - self.last_pos[0]) * self.x_sens)
        self.__current_pitch = self.__current_pitch + ((cur_pos[1] - self.last_pos[1]) * self.y_sens)
        self.last_pos = cur_pos

        if self.__current_pitch < -88.0:
            self.__current_pitch = -88.0
        if self.__current_pitch > 88.0:
            self.__current_pitch = 88.0

        yaw = Quaternion.FromAxisAndDegrees(Vector3(0.0, 1.0, 0.0), self.__current_yaw)
        pitch = Quaternion.FromAxisAndDegrees(Vector3(1.0, 0.0, 0.0), self.__current_pitch)
        self.transform.set_orientation(yaw * pitch)

    def parse(self, values, resource_manager):
        super().parse(values, resource_manager)

        self.x_sens = values['x_sensitivity']
        self.y_sens = values['y_sensitivity']
        self.__current_yaw = values['yaw']
        self.__current_pitch = values['pitch']
