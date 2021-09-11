def gameoflife(str, times):
    for _ in range(times):
        for ch in range(len(str) - 1):
            if str[ch] == '0' and ch == 0 and str[ch + 1] == '1':
                var = str[:ch - 1] + '1' + str[ch:]
            if str[ch] == '0' and 0 < ch < (len(str) - 1) and (str[ch + 1] == '1' or str[ch - 1] == '1'):
                str[:ch-1]+'1'+str[ch:]
            if str[ch] == '0' and ch == (len(str) - 1) and str[ch - 1] == '1':
                str[:ch-1]+'1'+str[ch:]

            print(str)

    return str


if __name__ == '__main__':
    print(gameoflife('01000000001', 3))
