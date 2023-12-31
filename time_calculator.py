def add_time(start, duration, weekday = 1):
  days = []
  hours = []
  minutes = []
  ampm = []
  lastday = []
  #Take and convert start time data
  stime, meridian = start.split(" ")
  sh, sm = stime.split(":")
  sh = int(sh)
  sm = float(sm)
  if meridian == "AM":
    sh = sh
  elif meridian == "PM":
    sh = sh + 12
  else:
    print("Error: meridian not AM or PM" )
  dstime = sh + sm/60
  #Take and convert duration time data
  d = duration.split(":")
  dh = int(d[0])
  dm = float(d[1])
  ddtime = dh + dm/60
  #calculate start + duration
  ftime = dstime + ddtime
  #Convert ftime str to split again and reconvert to int ffs
  ftime = str(ftime)
    #separate  back into hours and minutes
  ftime_hours, ftime_minutes = ftime.split(".")
  ftime_hours = int(ftime_hours)
  ftime_minutes = float("." + ftime_minutes)
  #print(ftime_hours)
  #Do the time calculations
  #hours value for final answer
  remainder = ftime_hours % 24
  if remainder < 1: 
    hoursans = 12
    hours.append(hoursans)
  elif remainder >= 13:
    hoursans = remainder - 12
    hours.append(hoursans)
  else:
    hours.append(remainder)
  #Deal with AM PM part of answer
  if remainder >= 12:
    ampmans = "PM"
    ampm.append(ampmans)
  else:
    ampmans = "AM"
    ampm.append(ampmans)
  #Find days
  fdays = float(ftime_hours/24)
  if fdays < 1:
    fdays = 0
    days.append(fdays)
  else:
    fdays = str(fdays)
    fdays = fdays.split(".")
    fdays = fdays[0]
    fdays = int(fdays)
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
  weekdays = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
  if weekday != 1:
    weekday = str(weekday.capitalize())
  if weekday in weekdays:
    startday = weekdays.index(weekday)
    startday = int(startday)
    endday = startday + int(days[0])
    if int(days[0]) > 1 and int(days[0]) < 8:
      endday = weekdays[endday]
      lastday.append(endday)
    elif int(days[0]) >= 8:
      endday = (startday + int(days[0])) % 7
      endday = weekdays[endday]
      lastday.append(endday)
    elif int(days[0]) == 1 :
      endday = startday + 1
      if endday >= 7:
        endday = endday % 7
        endday = weekdays[endday]
        lastday.append(endday)
      else:
        endday = weekday[endday]
        lastday.append(endday)
  #return new time with correct statements and formats
  if days[0] == 1 and weekday == 1:
    new_time = str(hours[0]) + ":" + str(minutes[0]) + " " + str(ampm[0]) + " " + "(next day)"
  elif days[0] > 1 and weekday == 1:
    new_time = str(hours[0]) + ":" + str(minutes[0]) + " " + str(ampm[0]) + " " + "(" + str(days[0]) + " days later)"
  elif days[0] < 1 and weekday == 1:
    new_time = str(hours[0]) + ":" + str(minutes[0]) + " " + str(ampm[0])
  if days[0] == 1 and weekday != 1:
    new_time = start + ", " + str(lastday[0]) + " (next day)"
  elif days[0] > 1 and weekday != 1:
    new_time = str(hours[0]) + ":" + str(minutes[0]) + " " + str(ampm[0]) + ", " + str(lastday[0]) + " " + "(" + str(days[0]) + " days later)"
  elif days[0] < 1 and weekday != 1:
    new_time = str(hours[0]) + ":" + str(minutes[0]) + " " + str(ampm[0]) + ", " + weekday           
  return new_time