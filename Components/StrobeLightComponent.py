import py3dengine


class StrobeLightComponent(py3dengine.Component):
    def __init__(self):
        super().__init__()

        self.time = 0.0
        self.light_component = None

    def start(self):
        self.light_component = self.get_owner().get_component_by_type(py3dengine.LightComponent)
        self.state_transition(0)

    def update(self, dt):
        self.time = self.time + dt

        if 0.0 < self.time <= 1.0 and self.state != 0:
            self.state_transition(0)
        elif 1.0 < self.time <= 2.0 and self.state != 1:
            self.state_transition(1)
        elif 2.0 < self.time <= 3.0 and self.state != 2:
            self.state_transition(2)
        elif 3.0 < self.time <= 4.0 and self.state != 3:
            self.state_transition(3)
        else:
            while self.time > 4.0:
                self.time = self.time - 4
            self.state_transition(0)

    def state_transition(self, new_state):
        if new_state == 0:
            self.light_component.set_diffuse_color([1.0, 0.0, 0.0])
        elif new_state == 1:
            self.light_component.set_diffuse_color([0.0, 1.0, 0.0])
        elif new_state == 2:
            self.light_component.set_diffuse_color([0.0, 0.0, 1.0])
        elif new_state == 3:
            self.light_component.set_diffuse_color([1.0, 1.0, 1.0])