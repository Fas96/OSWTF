def solution(v):
    stack = []
    for i in range(1, 5 + 1):
        for j in range(1, 5 + 1):
            if 0 <= i < 4 and 0 <= j < 4:
                print(v[i - 1][j][1], v[i + 1][j][1])
                for p in range(5):
                    if v[i - 1][j][p] == 'X' and v[i + 1][j][p] == 'X' and v[i][j - 1][p] == 'X' and v[i][j + 1][
                        p] == 'X':
                        stack.append(0)
                    elif v[i][j][p] == 'O':
                        stack.append(1)
                        p += 1

    return stack[len(stack) // 3:len(stack) - len(stack) // 3 - 1]


if __name__ == '__main__':
    print(solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"],
                    ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"],
                    ["PXOPX", "OXOXP", "OXPXX", "OXXXP", "POOXX"],
                    ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"],
                    ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]))
