import py3dengine
import py3dlogger
from KeyboardControllerComponent import KeyboardControllerComponent


class RootComponent(py3dengine.Component):
    def __init__(self):
        super().__init__()

        self.camera = None
        self.hammer = None
        self.selected_object_label = None

    def start(self):
        super().start()
        py3dlogger.info("[RootComponent]: Root says hi")

        scene = self.get_owner().get_scene()
        scene.set_key_callback(self.on_q_released, 81, 0, 0)
        scene.set_key_callback(self.on_1_released, 49, 0, 0)
        scene.set_key_callback(self.on_2_released, 50, 0, 0)
        scene.set_key_callback(self.on_3_released, 51, 0, 0)
        self.camera = self.get_owner().get_child_by_name("Camera").get_component_by_type(KeyboardControllerComponent)
        self.hammer = self.get_owner().get_child_by_name("Hammer").get_component_by_type(KeyboardControllerComponent)
        self.selected_object_label = self.get_owner().get_component_by_type(py3dengine.TextRendererComponent)
        self.selected_object_label.set_text('Selected Object: Camera')

        py3dengine.load_scene('Scenes/Scene2.json')
        # scene.set_cursor_mode('DISABLED')

    def end(self):
        super().end()
        py3dlogger.info("[RootComponent]: Root says bye")

    def on_q_released(self):
        py3dengine.quit()

    def on_1_released(self):
        self.camera.enable(True)
        self.hammer.enable(False)
        self.selected_object_label.set_text('Selected Object: Camera')

    def on_2_released(self):
        self.camera.enable(False)
        self.hammer.enable(True)
        self.selected_object_label.set_text('Selected Object: Hammer')

    def on_3_released(self):
        try:
            py3dengine.activate_scene("Scene2")
        except py3dengine.SceneError as err:
            py3dlogger.warning("Could not activate Scene2 " + str(err))
