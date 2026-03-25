total_hours = 0
total_problems = 0
total_sessions = 0
total_rating = 0
total_blockers = []

with open("study_log.txt","r",encoding = "utf-8") as f:
 content = f.read()

for line in content.splitlines():
	if line.startswith("Hours:"):
		hours = int(line.split(":")[1].strip())
		total_hours += hours
	if line.startswith("Problems:"):
		problems = int(line.split(":")[1].strip())
		total_problems += problems
	if line.startswith("Date:"):
		total_sessions += 1
	if line.startswith("Rating:"):
		rating = int(line.split(":")[1].strip())
		total_rating += rating
	if line.startswith("Blockers:"):
		blocker = line.split(":")[1].strip()
		total_blockers.append(blocker)
average_rating = total_rating / total_sessions	




	
print("WEEKLY SUMMARY\n")
print("--------\n")
print(f"Total sessions logged:{total_sessions}\n")
print(f"Total hours studied:{total_hours}\n")
print(f"Total problems solved:{total_problems}\n")
print(f"Average session rating:{average_rating}\n\n")
print(f"BLOCKERS THIS WEEK:\n")

for blockers in total_blockers:
	print('. '+blockers)
	

