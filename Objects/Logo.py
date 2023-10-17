from GameFrame import RoomObject


class Logo(RoomObject):
    def __init__(self, room, x, y, image_name, x_size, y_size):
        RoomObject.__init__(self, room, x, y)

        griff_logo = self.load_image(image_name)
        self.set_image(griff_logo, x_size, y_size)

        self.depth = - 100
