def add_time(start, duration):
  #Hmmmm h = 60m d = 24h, m = 1 so w  = 7d
  
  weekdays = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
  days = []
  hours = []
  minutes = []
  ampm = []
  
  #Take and convert start time data
  s = start.split(" ")
  stime = s[0]
  sh = int(stime[0:2])
  sm = float(stime[3:])
  meridian = s[1]
  if meridian == "AM":
    sh = sh
  elif meridian == "PM":
    sh = sh + 12
  else:
    print("Error: meridian not AM or PM" )
  shmtime = sh, sm
  dstime = sh + sm/60
  #Take and convert duration time data
  d = duration.split(":")
  dh = int(d[0])
  dm = float(d[1])
  dtime = dh, dm
  ddtime = dh + dm/60
  #calculate start + duration
  ftime = dstime + ddtime
  
  #Convert ftime str to split again and reconvert to int ffs
  ftime = str(ftime)
    #separate  back into hours and minutes
  ftime = ftime.split(".")
  ftime_hours = int(ftime[0])
  ftime_minutes = ftime[1]
  ftime_minutes = "." + ftime_minutes
  ftime_minutes = float(ftime_minutes)
   
  #Do the time calculations
  #print remainder? divide returned dh value by 24 if larger than 24 and return remainder(12hour), days, else return ftime in 12 hour format.
  
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
    ftime_minutes = str(ftime_minutes)
    if len(ftime_minutes) <= 1:
      ftime_minutes = "0" + ftime_minutes
      minutes.append(ftime_minutes)
    else:
      minutes.append(ftime_minutes)

  
    
    
       

    
  


  print(hours, days, ftime_hours)
  new_time = dstime + ddtime
  

  
  return new_time