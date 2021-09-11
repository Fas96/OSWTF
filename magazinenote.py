def checkMagazine(magazine, note):
    # Write your code here

    mg = magazine.split()
    nt = note.split()
    di = {}
    for m in nt:
        if m in di.keys():
            di[m] += 1
        else:
            di[m] = 1

    for n in range(len(nt)):
        if note[n] not in mg[n:] and magazine.count(magazine[n]) != note.count(note[n]):
            print("No")
            return
    print("Yes")


def checkMagaziney(magazine, note):
    # Write your code here

    mg = magazine.split()
    nt = note.split()
    mdi = {}
    for m in mg:
        if m in mdi.keys():
            mdi[m] += 1
        else:
            mdi[m] = 1

    for st in nt:
        if st in mdi.keys():
            mdi[st] -= 1
        else:
            mdi[st] = 1
    if min(mdi.values()) < 0:
        print("No")
    else:
        print("Yes")


def twoStrings(s1, s2):
    common = ""

    for ch in s2:
        if ch in s1:
            common += ch
    if common:
        print("Yes")
    else:
        print("No")


if __name__ == '__main__':
    # checkMagaziney("two times three is not four", "two times two is four")
    twoStrings("hi", "world")
