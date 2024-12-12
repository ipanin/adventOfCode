from collections import defaultdict
import util

# Sample input string:
# "Game 1: 7 green, 14 red, 5 blue; 8 red, 4 green; 6 green, 18 red, 9 blue"
def parse_line(line: str) -> list[dict[str, int]]:
    res = []
    game_str, game_result_str = line.split(':')
    cube_sets = game_result_str.split(';') # 7 green, 14 red, 5 blue
    for cube_set in cube_sets:
        cube_dict = defaultdict(int)
        n_cube_strs = cube_set.split(',')
        for n_cube_str in n_cube_strs:
            n, color = n_cube_str.split()
            cube_dict[color.strip()] = int(n)
        res.append(cube_dict)

    return res

def load_data(fname: str):
    lines = util.load_str_lines(fname)
    return [parse_line(line) for line in lines]


# Find out which games would have been possible if the bag contained only specified number of each color
def solve1(games: list[list[dict[str, int]]], colors: dict[str, int]) -> int:
    def game_is_possible(game: list[dict[str, int]] , colors: dict[str,int]) -> bool:
        for color, color_count in colors.items():
            if max([cube_set[color] for cube_set in game]) > color_count:
                return False
        return True

    res = 0
    for i, game in enumerate(games):
        if game_is_possible(game, colors):
            res += i+1
    return res

def colors_when_game_is_possible(game: list[dict[str, int]]) -> dict[str, int]:
    colors = defaultdict(int)
    for color in ['red', 'green', 'blue']:
        colors[color] = max([cube_set[color] for cube_set in game])
    return colors

def product(numbers: list[int]) -> int:
    res = 1
    for n in numbers:
        res *= n
    return res

# fewest number of cubes of each color 
def solve2(games: list[list[dict[str, int]]]) -> int:
    res = 0
    for game in games:
        colors = colors_when_game_is_possible(game)
        res += product(colors.values())
    return res

def test(fname: str, expected1: int, expected2: int):
    games = load_data(fname)
    p1 = solve1(games, {'red':12, 'green':13, 'blue':14})
    util.assert_equal(p1, expected1, "Part1")
    
    p2 = solve2(games)
    util.assert_equal(p2, expected2, "Part2")

test("input_sample.txt", 8, 2286)
test("input.txt", 2101, 58269)