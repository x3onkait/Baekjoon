import datetime

month_name_converter = {
    'January'   : 1,
    'February'  : 2,
    'March'     : 3,
    'April'     : 4,
    'May'       : 5,
    'June'      : 6,
    'July'      : 7,
    'August'    : 8,
    'September' : 9,
    'October'   : 10,
    'November'  : 11,
    'December'  : 12
}

month_date_converter = {
    1  : 31,
    2  : 28,
    3  : 31,
    4  : 30,
    5  : 31,
    6  : 30,
    7  : 31,
    8  : 31,
    9  : 30,
    10 : 31,
    11 : 30,
    12 : 31
}

input    = list(input().split())

year    = int(input[2])
month   = month_name_converter[input[0]]

if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
    month_date_converter[2] = 29
day     = int(input[1].replace(',', ''))
hour    = int(input[3].split(':')[0])
minute  = int(input[3].split(":")[1])

year_to_second = sum(month_date_converter.values()) * 86400

# get accumulated date
year_from_start_second = 0
for _seq in range(1, month):
    year_from_start_second += month_date_converter[_seq] * 86400
year_from_start_second += (day - 1) * 86400
year_from_start_second += hour * 3600
year_from_start_second += minute * 60

ratio_percentage = year_from_start_second * 100 / year_to_second
print(ratio_percentage)