def countApplesAndOranges(s, t, a, b, apples, oranges):
    countApples = coutOranges = 0

    for apple in apples:
        if s <= apple + a <= t:
            countApples += 1
    for orange in oranges:
        if s <= orange + b <= t:
            coutOranges += 1
    print(countApples)
    print(coutOranges)


if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    s = int(first_multiple_input[0])

    t = int(first_multiple_input[1])

    second_multiple_input = input().rstrip().split()

    a = int(second_multiple_input[0])

    b = int(second_multiple_input[1])

    third_multiple_input = input().rstrip().split()

    m = int(third_multiple_input[0])

    n = int(third_multiple_input[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)
