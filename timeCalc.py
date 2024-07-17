def add_time(start, duration,day=""):
    startData=start.split(" ")
    timeValues=startData[0].split(":")
    meridiemValue=startData[1]
    hour=int(timeValues[0])
    minute=int(timeValues[1])

    addValues=duration.split(":")
    hourAdd=int(addValues[0])
    minuteAdd=int(addValues[1])

    minute=minute+minuteAdd
    minuteCarry=int(minute/60)
    minute=minute%60

    hour=hour+minuteCarry

    hour+=hourAdd

    dayIncrement=0
    if((not(int(hour/12))%2==0) and (hour>11)):
        if(meridiemValue=="PM"):
            meridiemValue="AM"
            dayIncrement+=1
        else:
            print("here")
            meridiemValue="PM"

    dayIncrement+=int(hour/24)
    hour=hour%12
    if(hour==0):
        hour=12

    minuteStr=str(minute)
    if(minute<10):
        minuteStr="0"+minuteStr
    
    timeStr=str(hour)+":"+minuteStr+" "+meridiemValue
    
    dayIncStr=""
    if(dayIncrement==1):
        dayIncStr=" (next day)"
    elif(dayIncrement>1):
        dayIncStr=" ("+str(dayIncrement)+" days later)"


    weekDays=["sunday","monday","tuesday","wednesday","thursday","friday","saturday","sunday"]

    newDay=""
    if(not day==""):
        dayIndex=weekDays.index(day.lower())
        newDayIndex=int(int(dayIndex+dayIncrement)%7)
        newDay=weekDays[newDayIndex]
        day=newDay
        day=", "+day[:1].upper()+day[1:]

    return(timeStr+day+dayIncStr)
