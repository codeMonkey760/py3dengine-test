import py3dengine
import py3dinput
from KeyboardControllerComponent import KeyboardControllerComponent


class RootComponent(py3dengine.Component):
    def __init__(self):
        super().__init__(self)

        self.camera = None
        self.hammer = None

        py3dinput.set_key_callback(self.on_q_released, 81, 0, 0)
        py3dinput.set_key_callback(self.on_1_released, 49, 0, 0)
        py3dinput.set_key_callback(self.on_2_released, 50, 0, 0)

    def on_q_released(self):
        py3dengine.quit()

    def on_1_released(self):
        self.__get_camera()
        self.__get_hammer()
        self.camera.enable(True)
        self.hammer.enable(False)

    def on_2_released(self):
        self.__get_camera()
        self.__get_hammer()
        self.camera.enable(False)
        self.hammer.enable(True)

    def __get_camera(self):
        if self.camera is None:
            self.camera = self.get_owner().get_child_by_name("Camera").get_component_by_type(KeyboardControllerComponent)

    def __get_hammer(self):
        if self.hammer is None:
            self.hammer = self.get_owner().get_child_by_name("Hammer").get_component_by_type(KeyboardControllerComponent)