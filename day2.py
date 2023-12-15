class Day2:
    def __init__(self):
        self.games = list()
        with open("data/day2.txt") as fp:
            for line in fp:
                self.games.append(self.parse_line(line))


    def parse_line(self, line)->dict:
        # Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
        game = dict()

        game["id"] = int(line.split(":")[0].split(" ")[1])
        game["guesses"] = list() 

        guesses = line.split(":")[1].split(";")

        for index, guess in enumerate(guesses, len(guesses)):
            picks = [pick.strip() for pick in guess.split(",")]
            print(picks)
            temp = dict()

            for pick in picks:
                color, n_balls = pick.split(" ")[1], pick.split(" ")[0]
                temp[color] = n_balls

            game["guesses"].append(temp)

        print(game)
        return game

if __name__ == "__main__":
    day2 = Day2() 