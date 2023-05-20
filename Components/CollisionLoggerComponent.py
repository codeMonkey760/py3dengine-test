import py3dengine
from py3dlogger import info


class CollisionLoggerComponent(py3dengine.Component):
    def collider_enter(self, event):
        super().collider_enter(event)

        name = self.get_owner().get_name()
        other_name = event.collider2.get_owner().get_name()

        info('[CollisionLoggerComponent]: "{}" entered into a collision with "{}"'.format(name, other_name))

    def collider_exit(self, event):
        super().collider_exit(event)

        name = self.get_owner().get_name()
        other_name = event.collider2.get_owner().get_name()

        info('[CollisionLoggerComponent]: "{}" exited a collision with "{}"'.format(name, other_name))
