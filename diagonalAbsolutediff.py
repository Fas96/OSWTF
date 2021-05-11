def absolutediffDig(arr):
    leftdig = rightdig = 0
    n = len(arr)

    for i in range(len(arr)):
        leftdig += arr[i][i]
        rightdig += arr[i][len(arr)-i-1]

    return abs(leftdig - rightdig)


if __name__ == '__main__':
    print(absolutediffDig([[1, 1, 1], [0, 1, 0], [1, 1, 1]]))
