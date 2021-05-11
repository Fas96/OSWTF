def hourglassSum(arr):
    maxsum = -99 #initializing

    for i in range(4):
        for j in range(4):
            top=sum(arr[i][j:j+3])
            mid = arr[i+1][j+1]
            bot = sum(arr[i+2][j:j+3])
            hourclass = top+bot+mid

            maxsum=max(hourclass,maxsum)

    return maxsum


if __name__ == '__main__':
    pass