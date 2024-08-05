import time


def datenum(date):
    """datenum function is require a str input to indicate the date
    useage:
    1：datenum = datenum("yyyy-mm-dd-HH-mm-ss")
    2：datenum = datenum("yyyy-mm-dd-HH-mm")
    3：datenum = datenum("yyyy-mm-dd-HH")
    4：datenum = datenum("yyyy-mm-dd")
    if not input ss, default ss is 0
    if not input mm, default dd is 0
    if not input HH, default HH is 0"""
    print("Now, processing date_str to date_num")
    date_list = date.split('-')
    element2append = 6 - len(date_list)
    len_orig = len(date_list)
    for i in range(element2append):
        match (len_orig + i):
            case 1:
                date_list.append('1')
            case 2:
                date_list.append('1')
            case 3:
                date_list.append('0')
            case 4:
                date_list.append('0')
            case 5:
                date_list.append('0')
    date_str = '-'.join(date_list)

    parsed_time1 = time.strptime(date_str, "%Y-%m-%d-%H-%M-%S")
    mkt1 = int(time.mktime(parsed_time1))
    date_ystart = date_list[0] + '-' + '1' + '-' + '1'
    parsed_time2 = time.strptime(date_ystart, "%Y-%m-%d")
    mkt2 = int(time.mktime(parsed_time2))

    time_out = (float(date_list[0]) + (mkt1 - mkt2) / 3600 / 24 /
                (365 + (((not int(date_list[0]) % 4) and bool((int(date_list[0]) % 100))) or
                        (not int(date_list[0]) % 400))))
    return time_out
