def add_time(start, duration, weekday = 1):
  #Hmmmm h = 60m d = 24h, m = 1 so w  = 7d
  days = []
  hours = []
  minutes = []
  ampm = []
  lastday = []
  #new_time = ()
  
    #Take and convert start time data
  #s = start.split(" ")
  stime, meridian = start.split(" ")
  #stime = s[0]
  sh, sm = stime.split(":")
  sh = int(sh)
  sm = float(sm)
  #meridian = s[1]
  if meridian == "AM":
    sh = sh
  elif meridian == "PM":
    sh = sh + 12
  else:
    print("Error: meridian not AM or PM" )
  #shmtime = sh, sm
  dstime = sh + sm/60
  #Take and convert duration time data
  d = duration.split(":")
  dh = int(d[0])
  dm = float(d[1])
  #dtime = dh, dm
  ddtime = dh + dm/60
  #calculate start + duration
  ftime = dstime + ddtime
    #Convert ftime str to split again and reconvert to int ffs
  ftime = str(ftime)
    #separate  back into hours and minutes
  ftime_hours, ftime_minutes = ftime.split(".")
  ftime_hours = int(ftime_hours)
  #ftime_minutes = ftime[1]
  ftime_minutes = float("." + ftime_minutes)
  #ftime_minutes = float(ftime_minutes)
    #Do the time calculations
    #hours value for final answer
  remainder = ftime_hours % 24
  if remainder >= 13: 
    hoursans = remainder - 12
    hoursans = str(hours)
    hours.append(hoursans)
  else:
    hoursans = remainder
    hours.append(hoursans)
  #Deal with AM PM part of answer
  if remainder >= 12:
    ampmans = "PM"
    ampm.append(ampmans)
  else:
    ampmans = "AM"
    ampm.append(ampmans)
  #Find days
  if ftime_hours > 24:
    fdays = ftime_hours/24
    #print(fdays)
    fdays = str(fdays)
    fdays = fdays.split(".")
    fdays = fdays[0]
    days.append(fdays)
  #Deal with minutes part of answer
  ftime_minutes = ftime_minutes * 60
  if ftime_minutes >= 60:
    print("Error: minutes showing 60 or higher")
  else:
    ftime_minutes = int(round(ftime_minutes, 0))
    
    if ftime_minutes == 0:
      ftime_minutes = "00"
      minutes.append(ftime_minutes)
    else:
      ftime_minutes = str(ftime_minutes)
      if len(ftime_minutes) <= 1:
        ftime_minutes = "0" + ftime_minutes
        minutes.append(ftime_minutes)
      else:
        minutes.append(ftime_minutes)
  #Deal with days of the week
  weekdays = ["Sunday", "Monday", "tueSday", "Wednesday", "Thursday", "Friday", "Saturday"]
  if weekday in weekdays:
    startday = weekdays.index(weekday)
    startday = int(startday)
    endday = startday + int(days[0])
    if int(days[0]) > 1 and int(days[0]) < 8:
      endday = weekdays[endday]
      lastday.append(endday)
    elif int(days[0]) > 7:
      endday = int(days[0]) % 7
      endday = weekdays[endday]
      lastday.append(endday)
  #return new time with correct statements and formats
  if int(days[0]) == 1 and weekday == 1:
    new_time = str(hours[0]) + ":" + str(minutes[0]) + " " + str(ampm[0]) + " " + "(next day)"
  elif int(days[0]) > 1 and weekday == 1:
    new_time = str(hours[0]) + ":" + str(minutes[0]) + " " + str(ampm[0]) + " " + "(" + str(days[0]) + " days later)"
  if int(days[0]) == 1 and weekday != 1:
    new_time = str(hours[0]) + ":" + str(minutes[0]) + " " + str(ampm[0]) + ", " + str(lastday[0]) + " (next day)"
  elif int(days[0]) > 1 and weekday != 1:
    new_time = str(hours[0]) + ":" + str(minutes[0]) + " " + str(ampm[0]) + ", " + "(" + str(lastday[0]) + " days later"
               
  return new_time