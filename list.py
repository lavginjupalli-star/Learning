

"""months=["Jan","Feb","Mar","Apr","May","Jun","Jan"]
print(months)
print(type(months))
#months.pop("Mar")
print(set(months))
print(type(set(months)))
months.remove("Jan")
print (months)"""
"""input_units=""
while input_units != "exit":
    input_units=input("Enter units")
    u_d=input_units.split(":")
    print(u_d)

   ## dict={"Day":"","Units":"Hours" }
print("🔥 ONLY SPLIT CODE IS RUNNING 🔥")"""



def cal_units(input_days,conversion_unit):
    if conversion_unit == "hours":
        return f"There are {input_days*24} hours  in {input_days} days "
    elif conversion_unit == "minutes":
        return f"There are {input_days * 24*60} minutes in {input_days} days "
    else:
        return "Unknown unit"

def val_exe(du_dict):
  try:##if input_days.isdigit():
    input_days=int(du_dict["day"])
    if input_days > 0:
      my_fun=cal_units(input_days,du_dict["units"])
      print(my_fun)
    elif input_days == 0:
       print("Should not equal to Zero")
    else:
       print("Should be positive")
  except ValueError:##else:
    print("Enter a valid number")
"""input_units =""
while input_units != "Exit":
    input_units = input("enter number of units ")
    d_u = input_units.split(":")
    du_dict={"day":d_u[0],"units":d_u[1]}
    ##print(du_dict)
    val_exe()"""





