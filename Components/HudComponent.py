import py3dengine


class HudComponent(py3dengine.Component):
    def __init__(self):
        super().__init__()

        self.stats = None

    def start(self):
        self.stats = self.get_owner().get_component_by_index(1)

    def update(self, dt):
        self.stats.set_text(
            "FPS: {:#.2f}\nMS: {:#.2f}\nUPTIME: {:#.2f}".format(
                py3dengine.get_fps(),
                py3dengine.get_ms(),
                py3dengine.get_uptime()
            )
        )
