import json
from datetime import datetime, timedelta

# Load tasks from a JSON file or initialize an empty list if the file doesn't exist
def load_tasks(filename="tasks.json"):
    try:
        with open(filename, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

# Save tasks to a JSON file
def save_tasks(tasks, filename="tasks.json"):
    with open(filename, "w") as f:
        json.dump(tasks, f, indent=4)

# Add a new task with an estimated study time
def add_task(tasks):
    subject = input("Enter Subject: ")
    description = input("Enter Task Description: ")
    deadline = input("Enter Deadline (YYYY-MM-DD): ")
    time_required = float(input("Enter Estimated Time (hours): "))
    
    task = {
        "subject": subject,
        "description": description,
        "deadline": deadline,
        "time_required": time_required
    }
    
    tasks.append(task)
    save_tasks(tasks)
    print("Task added successfully!\n")

# View all tasks
def view_tasks(tasks):
    if not tasks:
        print("No tasks available.\n")
        return
    for idx, task in enumerate(tasks):
        print(f"Task {idx + 1}:")
        print(f"  Subject: {task['subject']}")
        print(f"  Description: {task['description']}")
        print(f"  Deadline: {task['deadline']}")
        print(f"  Estimated Time: {task['time_required']} hours\n")

# Function to split tasks over available days with adjustments for specific days (e.g., weekends)
def split_task_over_days(task, increase_on_weekends=True):
    deadline = datetime.strptime(task["deadline"], "%Y-%m-%d")
    today = datetime.today()
    
    if today > deadline:
        print(f"Deadline for {task['subject']} has already passed!")
        return []
    
    days_remaining = (deadline - today).days
    hours_per_day = task["time_required"] / days_remaining
    
    schedule = []
    for i in range(days_remaining):
        study_day = today + timedelta(days=i)
        is_weekend = study_day.weekday() in [5, 6]  # Saturday = 5, Sunday = 6
        
        if is_weekend and increase_on_weekends:
            # Add 20% more study time on weekends
            adjusted_hours = hours_per_day * 1.20
        else:
            # Keep the original hours for weekdays
            adjusted_hours = hours_per_day
        
        # Split the time into hours and minutes
        hours = int(adjusted_hours)
        minutes = int((adjusted_hours - hours) * 60)
        
        schedule.append({
            "date": study_day.strftime("%Y-%m-%d"),
            "hours": hours,
            "minutes": minutes
        })
    return schedule

# Build study schedule based on user tasks
def build_schedule(tasks):
    sorted_tasks = sorted(tasks, key=lambda x: datetime.strptime(x["deadline"], "%Y-%m-%d"))
    print("\nStudy Schedule:")
    
    for task in sorted_tasks:
        print(f"Subject: {task['subject']} - {task['description']}")
        print(f"Deadline: {task['deadline']} - Time Required: {task['time_required']} hours")
        
        # Split the task over available days with the option to increase study time on weekends
        schedule = split_task_over_days(task, increase_on_weekends=True)
        
        if schedule:
            for study_session in schedule:
                print(f"  Date: {study_session['date']} - Study Time: {study_session['hours']} hours and {study_session['minutes']} minutes")
        print("\n")

# Main menu loop
def main():
    tasks = load_tasks()
    
    while True:
        print("Study Scheduler - Main Menu")
        print("1. Add a New Task")
        print("2. View Tasks")
        print("3. Build Study Schedule")
        print("4. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            view_tasks(tasks)
        elif choice == '3':
            build_schedule(tasks)
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()