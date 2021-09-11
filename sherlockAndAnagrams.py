def sherlockAndAnagrams(s):
    lst = []
    print(*enumerate(s))
    for index, val in enumerate(s):
        print(index,val)

    for i in range(1, len(s) // 2 + 1):
        lst.append(s[:i])

    print(lst)


if __name__ == '__main__':
    sherlockAndAnagrams("cdcd")
