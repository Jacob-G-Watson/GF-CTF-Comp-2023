from GameFrame import Level, Globals, TextObject
from Objects import ResultsText
from collections import Counter
import os


class Result(Level):
    def __init__(self, screen, joysticks):
        Level.__init__(self, screen, joysticks)

        title = ResultsText(self, Globals.SCREEN_WIDTH / 3, 50, 'Results', 60, 'Comic Sans MS',
                            (255, 255, 255)
                            )
        title.x = Globals.SCREEN_WIDTH / 2 - title.width / 2
        self.add_room_object(title)

    def end_it(self):
        self.running = False
        self.quitting = True
        Globals.running = False

    def show_winner(self):
        file_name = os.path.join('Battles', 'results.txt')
        log_file = open(file_name, 'r')
        results_from_file = log_file.read().splitlines(False)
        log_file.close()

        results = {}
        for result in results_from_file:
            values = result.split(" ")
            if values[0] not in results:
                results[values[0]] = [1, int(values[2])]
            else:
                results[values[0]][1] += int(values[2])
                results[values[0]][0] += 1
        ordered_results = []
        for team in results:
            ordered_results.append([team, results[team][0], results[team][1]])
        ordered_results = sorted(ordered_results, key=lambda x: (x[1], x[2]), reverse=True)
        print(ordered_results)
        y_pos = 150
        for team in ordered_results:
            team_result = TextObject(
                self,
                Globals.SCREEN_WIDTH / 3,
                y_pos,
                '{}  W: {}  P: {}'.format(team[0], team[1], team[2]),
                80,
                'Comic Sans MS',
                (255, 255, 255)
            )
            team_result.x = Globals.SCREEN_WIDTH / 2 - team_result.width / 2
            self.add_room_object(team_result)
            y_pos += 80
