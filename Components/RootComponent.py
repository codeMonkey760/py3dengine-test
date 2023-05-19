import py3dengine
import py3dinput


class RootComponent(py3dengine.Component):
    def __init__(self):
        super().__init__(self)

        py3dinput.set_key_callback(self.on_q_released, 81, 0, 0)

    def on_q_released(self):
        py3dengine.quit()
