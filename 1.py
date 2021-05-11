def solution(s):
    def listToString(s):
        str1 = ""
        for ele in s:
            str1 += ele
        return str1

    stack = []
    d = {"zero": 0,
         "one": 1,
         "two": 2,
         "three": 3,
         "four": 4,
         "five": 5,
         "six": 6,
         "seven": 7,
         "eight": 8,
         "nine": 9
         }
    def toNumber(s):
        strings = [str(integer) for integer in s]
        a_string = "".join(strings)
        an_integer = int(a_string)
        return an_integer
    numStack =[]
    for i in range(len(s)):

        if s[i].isnumeric():
            stack = []
            numStack.append(int(s[i]))
        else:
            stack.append(s[i])
            if d.get(listToString(stack)) != None:
                print(d.get(listToString(stack)))
                numStack.append(d.get(listToString(stack)))
                stack = []
    return toNumber(numStack)


if __name__ == '__main__':
    solution("onetwonine")
