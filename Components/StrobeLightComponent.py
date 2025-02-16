import py3dengine


class StrobeLightComponent(py3dengine.Component):
    def __init__(self):
        super().__init__()

        self.time = 0.0
        self.state = 0
        self.light_component = None

    def start(self):
        self.light_component = self.get_owner().get_component_by_type(py3dengine.LightComponent)
        self.state_transition(0)

    def update(self, dt):
        self.time = self.time + dt

        if self.time > 1.0:
            while self.time > 1.0:
                self.time -= 1.0
            self.state_transition((self.state + 1) % 4)

    def state_transition(self, new_state):
        if new_state == 0:
            self.light_component.set_diffuse_color([0.7, 0.3, 0.3])
            self.light_component.set_specular_color([0.7, 0.3, 0.3])
            self.light_component.set_ambient_color([0.1, 0.0, 0.0])
            self.state = 0
        elif new_state == 1:
            self.light_component.set_diffuse_color([0.3, 0.7, 0.3])
            self.light_component.set_specular_color([0.3, 0.7, 0.3])
            self.light_component.set_ambient_color([0.0, 0.1, 0.0])
            self.state = 1
        elif new_state == 2:
            self.light_component.set_diffuse_color([0.3, 0.3, 0.7])
            self.light_component.set_specular_color([0.3, 0.3, 0.7])
            self.light_component.set_ambient_color([0.0, 0.0, 0.1])
            self.state = 2
        elif new_state == 3:
            self.light_component.set_diffuse_color([1.0, 1.0, 1.0])
            self.light_component.set_specular_color([1.0, 1.0, 1.0])
            self.light_component.set_ambient_color([0.1, 0.1, 0.1])
            self.state = 3