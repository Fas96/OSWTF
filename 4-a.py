def solution(n, start, end, roads, traps):
    answer = 0

    for i in roads:
        for pt in range(1, len(i)):
            if i[pt - 1] == i[pt]:
                answer += 1
            else:
                for j in traps:
                    if i[pt] == j:
                        answer += 2

    return answer


if __name__ == '__main__':
    print(solution(3, 1, 3, [[1, 2, 2], [3, 2, 3]], [2]))
