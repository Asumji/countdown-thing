import time

timer = input("Hours,Minutes,Seconds: ")

timeArray = timer.split(",")

hoursStr = timeArray[0]
minutesStr = timeArray[1]
secondsStr = timeArray[2]

if (hoursStr.isnumeric() and minutesStr.isnumeric() and secondsStr.isnumeric()):

    hours = int(hoursStr)
    minutes = int(minutesStr)
    seconds = int(secondsStr)
    if (minutes < 60 and seconds < 60):

        while hours > 0 or minutes > 0 or seconds > 0:
            time.sleep(1)
            if (seconds > 0):
                seconds -= 1
            elif (seconds == 0 and minutes > 0):
                minutes -= 1
                seconds = 59
            elif (seconds == 0 and minutes == 0 and hours > 0):
                minutes = 59
                seconds = 59
                hours -= 1
            print("Hours: " + str(hours) + "\nMinutes: " + str(minutes) + "\nSeconds: " + str(seconds))
        else:
            print("Timer has ended!")

    else:
        print("The time is not valid!")
else:
    print("The time is not valid!")