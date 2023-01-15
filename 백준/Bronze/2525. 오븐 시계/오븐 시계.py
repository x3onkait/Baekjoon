timeHR, timeMN = map(int, input().split())
reqMN          = int(input())

timeMN += reqMN
timeHR += int(timeMN / 60)
timeMN  = timeMN % 60

if timeHR >= 24:
    timeHR = timeHR % 24

print(f"{timeHR} {timeMN}")