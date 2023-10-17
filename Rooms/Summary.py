from GameFrame import Level, TextObject, Globals
from Objects import Logo, CompText, LogoBanner


class Summary(Level):
    def __init__(self, screen, joysticks):
        Level.__init__(self, screen, joysticks)

        self.background_colour = (255, 255, 255)

        title = CompText(
            self,
            Globals.SCREEN_WIDTH / 3,
            Globals.SCREEN_HEIGHT / 3,
            'GF Capture the Flag',
            80,
            'Comic Sans MS',
            (255, 0, 0)
        )

        title.x = Globals.SCREEN_WIDTH / 2 - title.width / 2
        self.add_room_object(title)

        ctf_text = TextObject(
            self,
            Globals.SCREEN_WIDTH / 3,
            Globals.SCREEN_HEIGHT / 3 + 100,
            '2022 Championships',
            100,
            'Comic Sans MS',
            (255, 0, 0)
        )

        ctf_text.x = Globals.SCREEN_WIDTH / 2 - ctf_text.width / 2
        self.add_room_object(ctf_text)

        if not Globals.first_run:
            self.set_timer(30, self.start_battle)

        bps_logo = Logo(self, 100, 0, "BestPractice_Logo.png", 450, 160)
        self.add_room_object(bps_logo)

        qc_logo = Logo(self, Globals.SCREEN_WIDTH - 580, 0, "QueenslandComputers_Logo.png", 492, 173)
        self.add_room_object(qc_logo)

        zenva_logo = Logo(self, Globals.SCREEN_WIDTH - 423, Globals.SCREEN_HEIGHT - 120, "Zenva_Logo.png", 403, 120)
        self.add_room_object(zenva_logo)

        IBM_Logo = Logo(self, 80, Globals.SCREEN_HEIGHT - 120, "IBM_Logo.png", 275, 120)
        self.add_room_object(IBM_Logo)

        qsite_logo = Logo(self, Globals.SCREEN_WIDTH / 2 - 180, Globals.SCREEN_HEIGHT - 120, "Qsite_Logo.png", 340, 120)
        self.add_room_object(qsite_logo)

        logo_banner = LogoBanner(self, 0, 0)
        self.add_room_object(logo_banner)

    def start_battle(self):
        if Globals.current_battle < len(Globals.game_list):
            self.running = False
        else:
            Globals.next_level = 2
            self.running = False
