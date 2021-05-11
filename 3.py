def solution(n, k, cmd):
    stack = []
    def listToString(s):
        str1 = ""
        for ele in s:
            str1 += ele
        return str1
    indexs = [v for v,ind in enumerate(cmd)]
    print(indexs)

    Res = ["O" for b in range(k)]
    move = indexs[0]
    for i in range(len(cmd)):
        if cmd[i] == "U " + str(indexs[i]):
            move = i - 1
        elif cmd[i] == "D " + str(indexs[i]):
            move = i + 1
        elif cmd[i] == "C":
            if move < len(Res):
                Res[move] = 'X'
                move = i + 1
            elif  move== len(Res):
                Res[move] = 'X'
                move = i - 1
        elif cmd[i] == "Z":
            move = move-1
            Res[move] = '0'

    return listToString(Res)


if __name__ == '__main__':
    print(solution(2, 8, ["D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z"]))
