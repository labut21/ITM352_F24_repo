import json
import os
from datetime import datetime, timedelta
import time
from tabulate import tabulate

# Load tasks from a JSON file or initialize an empty list if the file doesn't exist
def load_tasks(filename="tasks.json"):
    if os.path.exists(filename):
        with open(filename, "r") as f:
            return json.load(f)
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

# Delete a task by its index
def delete_task(tasks):
    if not tasks:
        print("No tasks available to delete.\n")
        return
    
    print("Tasks List:")
    for idx, task in enumerate(tasks):
        print(f"{idx + 1}. {task['subject']} - {task['description']} (Deadline: {task['deadline']})")
    
    try:
        task_num = int(input("Enter the number of the task to delete: ")) - 1
        if 0 <= task_num < len(tasks):
            removed_task = tasks.pop(task_num)
            save_tasks(tasks)
            print(f"Task '{removed_task['subject']}' successfully deleted!\n")
        else:
            print("Invalid task number. Please try again.\n")
    except ValueError:
        print("Invalid input. Please enter a number.\n")

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

# Split tasks over available days with adjustments for weekends
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
            adjusted_hours = hours_per_day * 1.20
        else:
            adjusted_hours = hours_per_day
        
        hours, minutes = format_time(adjusted_hours)
        schedule.append({
            "date": study_day.strftime("%Y-%m-%d"),
            "hours": hours,
            "minutes": minutes
        })
    return schedule

# Format fractional hours into hours and minutes
def format_time(fractional_hours):
    hours = int(fractional_hours)
    minutes = round((fractional_hours - hours) * 60)
    if minutes == 60:
        hours += 1
        minutes = 0
    return hours, minutes

# Pomodoro timer


# Build study schedule based on tasks, prioritizing by deadlines and available time
def build_schedule(tasks):
    sorted_tasks = sorted(
        tasks,
        key=lambda x: datetime.strptime(x["deadline"], "%Y-%m-%d")
    )
    
    available_time_per_day = float(input("Enter your daily available study time (hours): "))
    print("\nGenerating Study Schedule...\n")

    schedule = {}
    today = datetime.today()
    
    for task in sorted_tasks:
        task_deadline = datetime.strptime(task["deadline"], "%Y-%m-%d")
        days_remaining = (task_deadline - today).days
        
        if days_remaining <= 0:
            print(f"Task '{task['subject']}' is overdue and won't be scheduled.\n")
            continue
        
        time_required = task["time_required"]
        for day in range(days_remaining):
            study_date = today + timedelta(days=day)
            study_date_str = study_date.strftime("%Y-%m-%d")
            
            # Check if date already has allocated time, and calculate remaining time
            allocated_time = sum(entry['hours'] + entry['minutes'] / 60 for entry in schedule.get(study_date_str, []))
            remaining_time = available_time_per_day - allocated_time
            
            if remaining_time > 0:
                allocated_hours = min(remaining_time, time_required)
                time_required -= allocated_hours
                
                # Split fractional hours into hours and minutes
                hours, minutes = format_time(allocated_hours)
                
                # Add to the schedule for the day
                if study_date_str not in schedule:
                    schedule[study_date_str] = []
                
                schedule[study_date_str].append({
                    "subject": task["subject"],
                    "description": task["description"],
                    "hours": hours,
                    "minutes": minutes
                })
                
                # Stop allocating time once the task is fully scheduled
                if time_required <= 0:
                    break
        
        if time_required > 0:
            print(f"Warning: Not enough time to fully schedule task '{task['subject']}' before its deadline.\n")
    
    # Call to display the schedule
    display_schedule(schedule)

def display_schedule(schedule):
    if not schedule:
        print("No schedule to display.\n")
        return
    
    table_data = []
    for date, sessions in sorted(schedule.items()):
        for session in sessions:
            table_data.append([
                date,
                session["subject"],
                session["description"],
                f"{session['hours']} hours {session['minutes']} minutes"
            ])
    
    # Use tabulate to create a table
    print("\nStudy Schedule:")
    print(tabulate(
        table_data,
        headers=["Date", "Subject", "Task Description", "Study Time"],
        tablefmt="grid"
    ))
    
# Main menu loop
def main():
    tasks = load_tasks()
    
    while True:
        print("Study Scheduler - Main Menu")
        print("1. Add a New Task")
        print("2. View Tasks")
        print("3. Delete a Task")
        print("4. Build Study Schedule")
        print("5. Start Pomodoro Timer")
        print("6. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            view_tasks(tasks)
        elif choice == '3':
            delete_task(tasks)
        elif choice == '4':
            build_schedule(tasks)
        elif choice == '5':
            if tasks:
                # Show available tasks
                view_tasks(tasks)
                try:
                    task_num = int(input("Enter the task number to start Pomodoro (0 to cancel): ")) - 1
                    if task_num == -1:
                        print("Pomodoro timer canceled.")
                        continue
                    if 0 <= task_num < len(tasks):
                        selected_task = tasks[task_num]
                        start_pomodoro(selected_task["subject"], 25, 5)  # Example: 25 minutes work, 5 minutes break
                    else:
                        print("Invalid task number.")
                except ValueError:
                    print("Invalid input. Please enter a valid task number.")
            else:
                print("No tasks available. Please add tasks first.")
        elif choice == '6':
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()