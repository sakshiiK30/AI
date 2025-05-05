import matplotlib.pyplot as plt

class Job:
    def __init__(self, id, deadline, profit):
        self.id = id
        self.deadline = deadline
        self.profit = profit

# Input
n = int(input("Enter the number of Jobs: "))
jobs = []
print("Enter the details of the Jobs:")
for i in range(n):
    print(f"Job {i + 1}:")
    id = int(input("Enter the Job ID: "))
    deadline = int(input("Enter the Deadline of Job: "))
    profit = int(input("Enter the Profit of Job: "))
    jobs.append(Job(id, deadline, profit))

# Sort jobs by descending profit
jobs.sort(key=lambda x: x.profit, reverse=True)

# Find max deadline
maxDeadline = max(job.deadline for job in jobs)

# Scheduling
slots = [0] * (maxDeadline + 1)
jobMap = {}  # To keep track of job ID to profit
totalProfit = 0

for job in jobs:
    for i in range(job.deadline, 0, -1):
        if slots[i] == 0:
            slots[i] = job.id
            jobMap[job.id] = job.profit
            totalProfit += job.profit
            break

# Output
print("Scheduled Jobs:", end=" ")
for i in range(1, len(slots)):
    if slots[i] != 0:
        print(slots[i], end=" ")
print("\nTotal Profit:", totalProfit)

# Prepare data for graph
x_labels = []
y_profits = []

for i in range(1, len(slots)):
    if slots[i] != 0:
        x_labels.append(f"Slot {i}\nJob {slots[i]}")
        y_profits.append(jobMap[slots[i]])
    else:
        x_labels.append(f"Slot {i}\nEmpty")
        y_profits.append(0)

# Plot graph
plt.figure(figsize=(10, 6))
bars = plt.bar(x_labels, y_profits, color='skyblue')
plt.title("Job Scheduling by Profit")
plt.xlabel("Time Slots")
plt.ylabel("Profit")
plt.grid(axis='y')

# Add profit labels on top of bars
for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2.0, height, f'{height}', ha='center', va='bottom')

plt.tight_layout()
plt.show()

OUTPUT:
Enter the number of Jobs: 4
Enter the details of the Jobs:
Job 1:
Enter the Job ID: 1
Enter the Deadline of Job: 4
Enter the Profit of Job: 20
Job 2:
Enter the Job ID: 2
Enter the Deadline of Job: 3
Enter the Profit of Job: 10
Job 3:
Enter the Job ID: 3
Enter the Deadline of Job: 4
Enter the Profit of Job: 40
Job 4:
Enter the Job ID: 4
Enter the Deadline of Job: 2
Enter the Profit of Job: 50
Scheduled Jobs: 2 4 1 3
Total Profit: 120
