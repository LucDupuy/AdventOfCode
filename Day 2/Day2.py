file = open("input.txt", 'r')
list = file.read().splitlines()

max_dict = {
    "red": 12,
    "green": 13,
    "blue": 14
}
sum = 0

for game_idx, game in enumerate(list):

    add_game = True

    tmp_dict = {
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

            if value > max_dict[color]:
                add_game = False
                break
        else:
            continue
        break

    if add_game:
        sum += (game_idx+1)


print(sum)