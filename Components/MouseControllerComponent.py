import py3dengine
import py3dinput
import py3dlogger


class MouseControllerComponent(py3dengine.Component):
    def __init__(self):
        super().__init__(self)

    def update(self, dt):
        x, y = py3dinput.get_cursor_pos()

        py3dlogger.info('[MouseController]: Cursor is at {},{}'.format(x,y))

    def parse(self, values, resource_manager):
        pass
