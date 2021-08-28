days=["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]

def add_time(start, duration,day=""):
    laterDay = 0
    hourStart, am_pm = start.split()
    hourStart, minuteStart = hourStart.split(":")
    new_time = int(hourStart)
    hourDuration, minute = duration.split(":")

    if day!="":
        day=day.capitalize()
        index=days.index(day)

    if(int(hourDuration))>=24:
        laterDay=int(int(hourDuration)/24)
        hourDuration=int(hourDuration)-24*laterDay
    else:     
        hourDuration=int(hourDuration)

    hourDuration=int(hourDuration)
    addHour=int((int(minuteStart)+int(minute))/60)+hourDuration        
    addMinute=(int(minuteStart)+int(minute))%60
    addMinute=str(addMinute) if len(str(addMinute))>1 else "0"+str(addMinute)
   
    if (new_time+addHour)<12:
        new_time=str(new_time+addHour)+":"+addMinute+" "+am_pm  
    elif (new_time+addHour)==12:
       
        if am_pm=="AM":
            new_time=str(new_time+addHour)+":"+addMinute+" "+"PM"
        else:
            new_time=str(new_time+addHour)+":"+addMinute+" "+"AM"
            laterDay+=1 
    else:
        if am_pm=="AM":
            new_time=str(new_time+addHour-12)+":"+addMinute+" "+"PM"
        else:
            new_time=str(new_time+addHour-12)+":"+addMinute+" "+"AM"
            laterDay+=1    
 
    if day=="" and laterDay!=0 and laterDay!=1:
        new_time+=" ("+str(laterDay)+ " days later)"
    elif day !="" and laterDay==0:
        new_time+=", "+day
    elif day=="" and laterDay==0:
        pass
   
    else:

        if laterDay==1 and day!="":
            new_time+=", "+days[(index+laterDay)]+" (next day)"
        elif day!="":
            new_time+=", "+days[(index+laterDay)%7]+" ("+str(laterDay)+ " days later)"
        else:
             new_time+=" (next day)"
    return new_time

