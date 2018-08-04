import csv
import pprint

pp = pprint.PrettyPrinter(indent=4)

tasks_data = None
task_users_data = None
project_users_data = None

with open("tasks_data.csv") as f:
    reader = csv.DictReader(f)
    tasks_data = [r for r in reader]

with open("task_users_data.csv") as f:
    reader = csv.DictReader(f)
    task_users_data = [r for r in reader]

with open("project_users_data.csv") as f:
    reader = csv.DictReader(f)
    project_users_data = [r for r in reader]

print("\nHackNPlan hours calculator by Oski")
print("-"*15)

for user in project_users_data:
    userid = int(user["UserId"])

    user_tasks = []
    for task_data in task_users_data:
        if(task_data["UserId"] == user["UserId"]):
            user_tasks.append(task_data)

    total_time = 0

    for task in user_tasks:
        time = next(x for x in tasks_data if x["TaskId"] == task["TaskId"])["FinalCost"]
        total_time += float(time)

    print(str(round(total_time, 1)) + " hours done by " + user["UserName"])
