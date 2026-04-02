import json

def load_entries():
	entries = []
	with open("study_log.txt","r",encoding = "utf-8") as f:

		for line in f:
			line = line.strip()
			if line.startswith("{") and line.endswith("}"):
				entry = json.loads(line)
				entries.append(entry)
	return entries



def print_summary(entries):
	total_hours = 0
	total_problems = 0
	total_sessions = len(entries)
	total_rating = 0
	total_blockers = []

	for entry in entries:
		hours = int(entry.get("duration", 0))
		total_hours += hours
		problems = int(entry.get("problems_solved", 0))
		total_problems += problems
		rating = int(entry.get("rating", 0))
		total_rating += rating
		blocker = entry.get("difficulties", "")
		if blocker:
			total_blockers.append(blocker)

	print("WEEKLY SUMMARY\n")
	print("--------\n")
	print(f"Total sessions logged:{total_sessions}\n")
	print(f"Total hours studied:{total_hours}\n")
	print(f"Total problems solved:{total_problems}\n")
	average_rating = total_rating / total_sessions if total_sessions > 0 else 0
	print(f"Average session rating:{average_rating}\n\n")
	print(f"BLOCKERS THIS WEEK:\n")
	for blockers in total_blockers:
		print('. '+blockers)

entries = load_entries()
print_summary(entries)

