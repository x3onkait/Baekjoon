timeHR, timeMIN, timeSEC = map(int, input().split())
reqSEC                   = int(input())

timeSEC += reqSEC
timeMIN += int(timeSEC / 60)
timeHR  += int(timeMIN / 60)

if timeHR  >= 24:
    timeHR  = timeHR % 24
if timeMIN >= 60:
    timeMIN = timeMIN % 60
if timeSEC >= 60:
    timeSEC = timeSEC % 60


print(f"{timeHR} {timeMIN} {timeSEC}")