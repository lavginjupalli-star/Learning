from datetime import datetime
user_input=input("Enter your goal with deadline\n")
goal_list=user_input.split(":")
goal=goal_list[0]
date=datetime.strptime((goal_list[1]),"%d.%m.%Y")
print(type(date))
today=datetime.today()
days=date-today
hours=int(days.total_seconds()/60/60)
print (days)
print(f"You reach your goal {goal} in {hours} hours")
