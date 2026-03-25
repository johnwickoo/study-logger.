import datetime

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


with open("study_log.txt", "a") as f:
	f.write(f"Date: {current_date}\n")
	f.write(f"Task: {todays_task}\n")
	f.write(f"Hours: {duration}\n")
	f.write(f"Problems: {problems_solved}\n")
	f.write(f"Rating: {todays_rating}\n")
	f.write(f"Blockers: {difficulties_encountered}\n")
	f.write("\n--- END OF ENTRY ---\n\n")
	
print("Logged. Keep going.")