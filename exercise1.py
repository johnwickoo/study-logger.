import datetime
import json

study_log = {}

current_date = datetime.datetime.now()
todays_task = input("What did you do today?");
todays_task = todays_task.title();
duration = input("how many hours?");
problems_solved = input("How many problems did you solve?");

valid_ratings = (1,2,3,4,5)
while True:
	todays_rating = int(input("Rate your session 1-5"));
	if todays_rating in valid_ratings:
		 break
	print("Please enter a number between 1 and 5")
	
difficulties_encountered = input("Any blockers?")


#study_log[current_date] the current date is the key, so basically its a nested dictionary, the value is another dictionary with the details of the session.
study_log[current_date] = {
	"task": todays_task,
	"duration": duration,
	"problems_solved": problems_solved,
	"rating": todays_rating,
	"difficulties": difficulties_encountered
}

print("Today's study log:", study_log[current_date])

with open("study_log.txt", "a") as f:
	f.write(json.dumps(study_log[current_date]) + "\n")
	f.write("\n--- END OF ENTRY ---\n\n")
	
print("Logged. Keep going.")