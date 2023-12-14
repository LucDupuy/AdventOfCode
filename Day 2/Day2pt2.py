file = open("input.txt", 'r')
list = file.read().splitlines()


total = 0

for game_idx, game in enumerate(list):

    min_dict = {
        "red": 0,
        "blue": 0,
        "green": 0
    }
    game = game.split(':', 1)[-1]
    game = game.split(';')

    print("Game: ", game)
    list_of_dicts_to_compare = []
    for idx, pick in enumerate(game):

        if not "red" in pick:
            game[idx] = pick + ", 0 red"

        elif not "blue" in pick:
            game[idx] = pick + ", 0 blue"
        
        elif not "green" in pick:
            game[idx] = pick + ", 0 green"

    for idx, pick in enumerate(game):
        for color in pick.split(','):
            color_list = color.split(' ')
            color = str(color_list[-1])
            value = int(color_list[1])

            if value > min_dict[color]:
                min_dict[color] = value

    power = 1
    for value in min_dict.values():
        power *= value

    total += power

print(total)