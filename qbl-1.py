def solution(id_list, report, k):
    id_list = ["muzi", "frodo", "apeach", "neo"]
    report = ["muzi frodo", "apeach frodo", "frodo neo", "muzi neo", "apeach muzi"]
    k = 2
    countReport = {}

    for re in report:
        if re.split(" ")[0] not in countReport:
            countReport[re.split(" ")[0]] = 1
        else:
            countReport[re.split(" ")[0]] += 1

    answer = []
    print(countReport)
    return answer


if __name__ == '__main__':
    solution([], [], 3)
