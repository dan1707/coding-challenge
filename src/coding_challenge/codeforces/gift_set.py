import math


def max_possible_gift_sets(red: int, blue: int, a: int, b: int) -> int:
    return calculate_max_gift_sets(red, blue, a, b)
    # first_solution_count = get_gift_set_count(red, blue, a, b)
    # second_solution_count = get_gift_set_count(red, blue, b, a)
    #
    # return first_solution_count if first_solution_count > second_solution_count else second_solution_count


def get_gift_set_count(red: int, blue: int, a: int, b: int) -> int:
    if a > red or b > blue:
        return 0

    first_candy_count = math.trunc(red / a)
    second_candy_count = math.trunc(blue / b)
    gs_count = first_candy_count if first_candy_count < second_candy_count else second_candy_count
    remaining_red = red - gs_count * a
    remaining_blue = blue - gs_count * b

    if gs_count > 0 and remaining_red > 0 and remaining_blue > 0:
        gs_count += get_gift_set_count(remaining_red, remaining_blue, b, a)
    return gs_count


def calculate_max_gift_sets(x: int, y: int, a: int, b: int) -> int:
    if x == y and a == b and x >= a:
        return x

    if x < a and x < b and y < a and y < b:
        return 0

    if (x == a and y ==b) or (x == b and y == a):
        return x if x < y else y

    start = x if x > y else y
    if a > b:
        start = math.floor(start/b)
    else:
        start = math.floor(start/a)
    max_g = 0
    for c in range(start, 0, -1):
        frxc = math.floor((x - a * c) / b)
        fryc = math.floor((y - b * c) / a)
        if frxc < 0 or fryc < 0:
            continue
        g = c
        g += frxc if frxc < fryc else fryc
        if max_g > g:
            return max_g
        max_g = g
    return max_g


if __name__ == '__main__':
    pass