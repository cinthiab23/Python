time_slots = ["Morning", "Midday", "Afternoon", "Evening"]
heart_rates = []
for time in time_slots:
    level = int(input(f"Enter you heart rate in beats for per minute for {time}:"))
    heart_rates.append([time, level])
# Average heart rate
total = 0
for rate in heart_rates:
    total = total + rate[1]
average = total / len(heart_rates)
print(average)
