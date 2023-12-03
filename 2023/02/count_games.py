def get_game_id(line):
    return int(line.split(":")[0].split(" ")[1])


def get_game_data(line):
    data = []
    line = line.split(":")[1].strip()
    games_data = line.split(";")
    for game_data in games_data:
        game = {}
        for item in game_data.split(","):
            num, key = item.strip().split(" ")
            game[key.strip()] = int(num)
        data.append(game)
    return data


def is_valid(game, allowed):
    print(game)
    for key in game:
        if key in allowed and game[key] > allowed[key]:
            return False
    return True


def main():
    with open("input02.txt", "r") as f:
        data = [line.strip() for line in f]
        games = []
        for line in data:
            games.append([get_game_id(line), get_game_data(line)])

        allowed = {"red": 12, "green": 13, "blue": 14}
        sum = 0
        for game in games:
            valid = True
            for subgame in game[1]:
                if not is_valid(subgame, allowed):
                    valid = False
                    break
            if valid:
                sum += game[0]
        print(sum)


main()
