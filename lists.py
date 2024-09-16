# Create a list of the seven days of the week
Days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
Steps = []
print("Please enter the number of steps you've taken for each day:")

#  The count of steps of each day
for day in Days:
    count = int(input(f"How many step did you take on {day}:"))
    Steps.append(count)

# The daily steps for each day
for i in range(len(Days)):
    day = Days[i]
    count = Steps[i]
    print(f" {day} has = {count} steps")

# Totalsteps
totalSteps = sum(Steps)
print(f"Total number of steps taken: {totalSteps}")

# Average steps
Average = round(totalSteps / len(Steps))
print(f"Average steps:{Average}")
