def swap_number(a: int, b: int) -> (int, int):
    a = a + b
    b = a - b
    a = a - b
    return a, b
