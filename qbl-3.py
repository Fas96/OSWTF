def solution(fees, records):
    records = ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN",
               "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]

    fees = [180, 5000, 10, 600]
    inRecords = [ix for ix in records if ix.endswith("IN")]
    outRecords = [ix for ix in records if ix.endswith("OUT")]
    takeSim = []
    re = []
    inNum = []
    OutNum = []
    timeCal = []
    for checkIn in inRecords:
        for checkOut in outRecords:
            if checkIn.split(" ")[1] == checkOut.split(" ")[1] and (
                    checkOut.split(" ")[2] == "OUT" and checkIn.split(" ")[2] == "IN"):

                if checkIn not in inNum and checkOut not in OutNum:
                    takeSim.append([checkIn, checkOut])
                    inNum.append(checkIn)
                    OutNum.append(checkOut)

                    timeCal.append([checkOut.split(" ")[1], (60 * (int(checkOut.split(" ")[0].split(":")[0]) - int(
                        checkIn.split(" ")[0].split(":")[0]))) + (int(checkOut.split(" ")[0].split(":")[1]) - int(
                        checkIn.split(" ")[0].split(":")[1]))])

    # missingX = [mp for mp in xValues if xValues.count(mp) == 1][0]
    getcar = [mp[0] for mp in timeCal]
    temcar = {}
    print(timeCal)
    print(getcar)
    for t in timeCal:
        if t[0] not in temcar:
            print(t[1])
            temcar[t[0]] = t[1]
        else:
            temcar[t[0]] += t[1]

    print(temcar)
    payment = 0
    paymentamount = 0
    paymentArr = []

    for k, v in temcar.items():
        payment = v - fees[0]
        print(payment)
        if payment > 0:
            paymentamount = fees[1]
            paymentamount += payment / fees[3] * fees[3]
            paymentArr.append(paymentamount)
        else:
            paymentArr.append(fees[1] * (v / fees[0]))

    print(paymentArr)


if __name__ == '__main__':
    solution([], [])
