#age calculator
try:
   year=int(input("enter year of your birth "))
   month=int(input("enter month your birth"))
   day=int(input("enter day of your birth"))
except:
    print("invlid input")
else:
     if date.today().month>month:
        print("hello! you are ",date.today().year-year,"years's ",date.today().month-month,"months's ",day," days old ")
     elif date.today().month==month:
          print("hello! you are ",date.today().year-year," year's ",date.today().day-day," days old")
     else:
          print("hello! you are ",date.today().year-year,"years's ",month-date.today().month,"months's ",day," days old ")
