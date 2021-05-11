def minimumSwaps(arr):
    counter = b = 0

    for i in range(len(arr) - 1):
        for j in range(i):
            if i + 1 == arr[i]:
                b += 1
            if arr[i] < arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
                counter = max(i, j)
    return counter - (b - counter), arr, b


def minimumSwapsy(arr):
    visited = [False for _ in range(len(arr))]
    sum = 0
    for i in range(len(arr)):
        if not visited[i]:
            currentIndex, shouldbeIndex = i, arr[i] - 1
            lenOfCircle = 0
            visited[i] = True
            while shouldbeIndex != i:
                visited[shouldbeIndex] = True
                currentIndex, shouldbeIndex = shouldbeIndex, arr[shouldbeIndex] - 1
                lenOfCircle += 1
            sum += lenOfCircle

    return sum


def arrayManipulation(n, queries):
    maxCount, ourArr = 0, [0 for _ in range(n)]

    for arr in queries:
        print(ourArr)
        for i in range(arr[0] - 1, arr[1]):
            ourArr[i] += arr[2]
            maxCount = max(maxCount, ourArr[i])
    return maxCount


def arrayManipulationy(n, queries):
    arr = [0] * (n * 2)

    for a, b, k in queries:
        arr[a] += k
        arr[b + 1] -= k
    maxnum = temp = 0
    for var in arr:
        temp +=var
        maxnum = max(maxnum,temp)


if __name__ == '__main__':
    print(minimumSwapsy([3, 7, 6, 9, 1, 8, 10, 4, 2, 5]))
