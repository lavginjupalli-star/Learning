
cal_to_hours=24
name_of_unit= "hours"

def cal_units(days):


    return f"There are {days*cal_to_hours} {name_of_unit} in {days} days "


def val_exe():
  try:##if input_days.isdigit():
    days=int(no_days)
    if days > 0:
      my_fun=cal_units(days)
      print(my_fun)
    elif days == 0:
       print("Should not equal to Zero")
    else:
       print("Should be positive")
  except ValueError:##else:
    print("Enter a valid number")


input_days=""
while input_days != "Exit":
    input_days=input("enter number of days,I'll validate ")
    for no_days in input_days.split(",") :
        val_exe()






