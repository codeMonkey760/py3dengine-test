import py3dengine


class RootComponent(py3dengine.Component):
    def __init__(self):
        self.state = 0
        self.stateChangeTimeout = 1.0
        self.timeSinceStateChange = 0.0

    def update(self, dt):
        self.timeSinceStateChange = self.timeSinceStateChange + dt
        if self.timeSinceStateChange >= self.stateChangeTimeout:
            self.timeSinceStateChange = self.timeSinceStateChange - self.stateChangeTimeout

            self.state = self.advanceState(self.state)

    def advanceState(self, oldState):
        newState = oldState + 1
        if newState > 6:
            newState = 0

        if newState == 0:
            self.resetScene()
        elif newState == 1:
            self.enableGO("Cube", False)
        elif newState == 2:
            self.enableGO("Cube", True)
            self.makeGOVisible("Cube", False)
        elif newState == 3:
            self.makeGOVisible("Cube", True)
            self.enableGO("Pyramid", False)
        elif newState == 4:
            self.enableGO("Pyramid", True)
            self.makeGOVisible("Pyramid", False)
        elif newState == 5:
            self.makeGOVisible("Pyramid", True)
            self.enableGO("Quad", False)
        elif newState == 6:
            self.enableGO("Quad", True)
            self.makeGOVisible("Quad", False)

        return newState

    def enableGO(self, name, value):
        parent = self.get_owner()
        target = parent.find_child_by_name(name)
        target.enable(value)

    def makeGOVisible(self, name, value):
        parent = self.get_owner()
        target = parent.find_child_by_name(name)
        target.make_visible(value)

