
def is_game_possible(game):
    colour_count = {"red": 0, "green": 0, "blue": 0}
    for game_cubes in game:
        cubes = game_cubes.strip().split(",")
        for num_cubes in cubes:
            num_cubes_list = num_cubes.strip().split()
            amount = int(num_cubes_list[0])
            colour = num_cubes_list[1]

            colour_count[colour] += amount

            if (amount > total_colour_limit[colour]):
                return False
            
    return True


def get_power(game):
    colour_min = {"red": 0, "green": 0, "blue": 0}
    for game_cubes in game:
        cubes = game_cubes.strip().split(",")
        for num_cubes in cubes:
            num_cubes_list = num_cubes.strip().split()
            amount = int(num_cubes_list[0])
            colour = num_cubes_list[1]

            if amount > colour_min[colour]:
                colour_min[colour] = amount
    
    return colour_min["red"] * colour_min["green"] * colour_min["blue"]


colours = ["red", "green", "blue"]

total_colour_count = {"red": 0, "green": 0, "blue": 0}
total_colour_limit = {"red": 12, "green": 13, "blue": 14}

with open("day2\input.txt") as f:
    lines = f.readlines()
    possible_sum = 0
    power_sum = 0

    for line in lines:
        game_list = line.strip().split(":")
        game_id = int(game_list[0].split()[1])
        
        game_cubes_all = game_list[1].strip().split(";")

        if is_game_possible(game_cubes_all):
            possible_sum += game_id

        power_sum += get_power(game_cubes_all)
            
    print(possible_sum)
    print(power_sum)

