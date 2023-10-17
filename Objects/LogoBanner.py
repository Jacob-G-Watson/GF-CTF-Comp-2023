from GameFrame import RoomObject, Globals


class LogoBanner(RoomObject):
    def __init__(self, room, x, y):
        RoomObject.__init__(self, room, x, y)

        image = self.load_image("Logo_Banner.png")
        self.set_image(image, Globals.SCREEN_WIDTH, 180)

        self.depth = - 100
