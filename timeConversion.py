def timeConversion(s):
    # Write your code here
    # Note: - 12:00:00AM on a 12-hour clock is 00:00:00 on a 24-hour clock.
    # - 12:00:00PM on a 12-hour clock is 12:00:00 on a 24-hour clock.
    hour, mins, cat = s.split(':')
    cat, sec = cat[2:], cat[:2]

    hour = hour

    sec = sec
    t = ''

    if int(hour) == 12 and cat == 'AM':
        t = '00:' + str(mins) + ':' + str(sec)
    if int(hour) == 12 and cat == 'AM':
        t = str('00') + ":" + str(mins) + ":" + str(sec)
    if int(hour) == 12 and cat == 'PM':
        t = str(hour) + ":" + str(mins) + ":" + str(sec)

    if int(hour) < 12 and cat == 'AM':
        t = str(hour) + ":" + str(mins) + ":" + str(sec)
    if int(hour) < 12 and cat == 'PM':
        t = str((hour + 12)) + ":" + str(mins) + ":" + str(sec)

    return t


if __name__ == '__main__':
    s = input()

    result = timeConversion(s)

    print(result)
