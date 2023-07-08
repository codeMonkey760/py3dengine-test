import py3dengine
import py3dlogger


class Scene2RootComponent(py3dengine.Component):
    def start(self):
        super().start()

        scene = self.get_owner().get_scene()
        scene.set_key_callback(self.on_q_released, 81, 0, 0)

    def activate(self):
        super().activate()
        py3dlogger.info("[Scene2RootComponent]: Scene 2 is unloading CollisionDetectionTest ... get ready")
        try:
            py3dengine.unload_scene("CollisionDetectionTest")
            py3dlogger.info("[Scene2RootComponent]: CollisionDetectionTest unloaded without incident")
        except Exception as err:
            py3dlogger.error("[Scene2RootComponent]: Unloading CollisionDetectionTest raised error: " + str(err))

    def on_q_released(self):
        py3dengine.quit()
