import json
import os
from datetime import datetime, timedelta
import time
from plyer import notification
from tabulate import tabulate
from collections import defaultdict
import re
from datetime import datetime

# Checks user inputs for correct date and time formats
def validate_input(input_type, value):
    print(f"Validating {input_type} with value: {value}")  # Debugging line
    
    if input_type == "deadline":
        # Check date format: YYYY-MM-DD
        try:
            datetime.strptime(value, "%Y-%m-%d")
            print(f"Deadline '{value}' is valid.")
            return True
        except ValueError:
            print(f"Invalid deadline format for '{value}'. Please use YYYY-MM-DD.")
            return False
    
    elif input_type == "time":
        # Check if value is a positive float
        try:
            time = float(value)
            if time > 0:
                print(f"Time '{value}' is valid.")
                return True
            else:
                print("Time must be a positive number.")
                return False
        except ValueError:
            print(f"Time '{value}' is invalid. Must be a number.")
            return False
    
    return False  # For other types of input, if needed

# Example of using validate_input
def main():
    # Check deadline input
    deadline = input("Enter a task deadline (YYYY-MM-DD): ")

    # Call validate_input to check if the deadline format is correct
    if validate_input("deadline", deadline):
        print(f"Deadline '{deadline}' is valid.")
    else:
        print(f"Deadline '{deadline}' is invalid.")

    # Validate time input
    estimated_time = input("Enter estimated time for the task (in hours): ")

    # Call validate_input to check if the time is a valid positive number
    if validate_input("time", estimated_time):
        print(f"Time '{estimated_time}' is valid.")
    else:
        print(f"Time '{estimated_time}' is invalid.")

def load_tasks(filename="tasks.json"):
    if os.path.exists(filename):
        with open(filename, "r") as f:
            return json.load(f)
    return []

def save_tasks(tasks, filename="tasks.json"):
    with open(filename, "w") as f:
        json.dump(tasks, f, indent=4)

def add_task(tasks):
    subject = input("Enter Subject: ")
    description = input("Enter Task Description: ")

    while True:
        deadline = input("Enter Deadline (YYYY-MM-DD): ")
        if validate_input("deadline", deadline):
            break

    while True:
        time_required = input("Enter Estimated Time (hours): ")
        if validate_input("time", time_required):
            time_required = float(time_required)
            break

    tasks.append({
        "subject": subject,
        "description": description,
        "deadline": deadline,
        "time_required": time_required,
        "time_logged": 0
    })
    save_tasks(tasks)
    print("Task added successfully!\n")

# Delete a task by its index in the task list
# This function was generated using ChatGPT with the prompt: "Improve the delete_task function with better error handling, and improve readabilty of the code."
def delete_task(tasks):
# Check if there are tasks to delete 
    if not tasks:
        print("No tasks available to delete.\n")
        return

# Show all tasks with an index for selection
    for idx, task in enumerate(tasks):
        print(f"{idx + 1}. {task['subject']} - {task['description']} (Deadline: {task['deadline']})")

    try:
        task_num = int(input("Enter the task number to delete: ")) - 1 # Convert input to zero-based index
        if 0 <= task_num < len(tasks):
            removed_task = tasks.pop(task_num)
            save_tasks(tasks)
            print(f"Deleted task: {removed_task['subject']}\n")
        else:
            print("Invalid task number.\n")
    except ValueError:
        print("Invalid input.\n")

def view_tasks(tasks):
    if not tasks:
        print("No tasks available.\n")
        return
    for idx, task in enumerate(tasks):
        print(f"Task {idx + 1}:")
        print(f"  Subject: {task['subject']}")
        print(f"  Description: {task['description']}")
        print(f"  Deadline: {task['deadline']}")
        print(f"  Estimated Time: {task['time_required']} hours")
        print(f"  Time Logged: {task['time_logged']} hours\n")

# This function was generated using ChatGPT with the prompt: "Write a function to split study hours over days until a task's deadline, adjusting for weekends." 
def split_task_over_days(task):

# Convert deadline string to a datetime object and get today's data
    deadline = datetime.strptime(task["deadline"], "%Y-%m-%d")
    today = datetime.today()

    if today > deadline:
        print(f"Deadline for {task['subject']} has passed!")
        return []

    days_remaining = (deadline - today).days

# Calculate the base number of study hours per day 
    hours_per_day = task["time_required"] / days_remaining

    schedule = []

# Loop through each day until the deadline 
    for i in range(days_remaining):
        study_day = today + timedelta(days=i)

# Adjust study hours for weekends (20% increase)
        if study_day.weekday() in [5, 6]:  # Weekend
            adjusted_hours = hours_per_day * 1.20
        else:
            adjusted_hours = hours_per_day

        hours, minutes = divmod(adjusted_hours * 60, 60)
        schedule.append({
            "date": study_day.strftime("%Y-%m-%d"),
            "hours": int(hours),
            "minutes": int(minutes)
        })
    return schedule

# Pomodoro timer
def start_pomodoro(task_name, work_time=25, break_time=5):
    tasks = load_tasks()
    total_time_worked = 0

    print(f"Starting Pomodoro for: {task_name}")
    try:
        for session in range(4):
            print(f"Session {session + 1}: Work ({work_time} minutes)")
            time.sleep(work_time * 60)
            total_time_worked += work_time / 60

            log_time(tasks, task_name, total_time_worked)

            print(f"Session {session + 1}: Break ({break_time} minutes)")
            time.sleep(break_time * 60)

        print("Pomodoro complete! Take a longer break.")
    except KeyboardInterrupt:
        print("Pomodoro interrupted. Logging progress...")
        log_time(tasks, task_name, total_time_worked)

# Record the time spent on a task and update the task data
def log_time(tasks, task_name, time_spent):
    for task in tasks:
        if task["subject"] == task_name:
            task["time_logged"] += time_spent
            save_tasks(tasks)
            print(f"Logged {time_spent} hours for '{task_name}'.")
            break


def format_time(fractional_hours):
# Converts a decimal number of hours into hours and minutes
    hours = int(fractional_hours)
    minutes = round((fractional_hours - hours) * 60)
    return hours, minutes

def countdown_timer(seconds, label):
    try:
        while seconds > 0:
            mins, secs = divmod(seconds, 60)
            print(f"{mins:02}:{secs:02} {label}", end="\r")
            time.sleep(1)
            seconds -= 1
    except KeyboardInterrupt:
        print("\nPomodoro interrupted. Logging progress...")
        raise

# Pomodoro timer
def start_pomodoro(task_name, work_time=25, break_time=5):
    tasks = load_tasks()
    total_time_worked = 0

    print(f"Starting Pomodoro for: {task_name}")
    try:
        for session in range(4):

            print(f"Session {session + 1}: Work ({work_time} minutes)")
            countdown_timer(work_time * 60, "Work")
            total_time_worked += work_time / 60
            log_time(tasks, task_name, total_time_worked)


            print(f"Session {session + 1}: Break ({break_time} minutes)")
            countdown_timer(break_time * 60, "Break")

        print("Pomodoro complete! Take a longer break.")
        notification.notify(
            title="Pomodoro Complete",
            message="Pomodoro session complete! Take a longer break.",
            timeout=10
        )
    except KeyboardInterrupt:
        print("\nPomodoro interrupted. Logging progress...")
        log_time(tasks, task_name, total_time_worked)

# This function was generated using ChatGPT with the prompt: "Help me write a function that builds a study schedule based on task deadlines and available study time."
def build_schedule(tasks):

# Sort the tasks by their deadline in ascending order
    sorted_tasks = sorted(tasks, key=lambda x: datetime.strptime(x["deadline"], "%Y-%m-%d"))
    available_time_per_day = float(input("Enter your daily available study time (hours): "))
    schedule = {}
    today = datetime.today()

# Loop through each task in the sorted list 
    for task in sorted_tasks:
        deadline = datetime.strptime(task["deadline"], "%Y-%m-%d")
        days_remaining = (deadline - today).days
        if days_remaining <= 0:
            print(f"Task '{task['subject']}' is overdue.")
            continue
        time_required = task["time_required"]
        for day in range(days_remaining):
            study_date = today + timedelta(days=day)
            date_str = study_date.strftime("%Y-%m-%d")
            allocated_time = sum(entry["hours"] + entry["minutes"] / 60 for entry in schedule.get(date_str, []))
            remaining_time = available_time_per_day - allocated_time
            if remaining_time > 0:
                allocated_hours = min(remaining_time, time_required)
# Decrease the remaining required time for the task 
                time_required -= allocated_hours
                hours, minutes = format_time(allocated_hours)
                schedule.setdefault(date_str, []).append({
                    "subject": task["subject"],
                    "description": task["description"],
                    "hours": hours,
                    "minutes": minutes
                })
                if time_required <= 0:
                    break

# If there is still time left for the task that couldn't be fully scheduled, print a warning 
        if time_required > 0:
            print(f"Not enough time to fully schedule task '{task['subject']}'.")
    display_schedule(schedule)

# Shows the study schedule using the 'tabulate' library for a user-friendly tabular view
def display_schedule(schedule):
    if not schedule:
        print("No schedule to display.")
        return
    table_data = []
    for date, sessions in sorted(schedule.items()):
        for session in sessions:
            table_data.append([
                date, session["subject"], session["description"], f"{session['hours']}h {session['minutes']}m"
            ])
    print(tabulate(table_data, headers=["Date", "Subject", "Description", "Study Time"], tablefmt="grid"))

def generate_report(tasks):
    if not tasks:
        print("No tasks available for report.")
        return
    subject_totals = defaultdict(float)
    task_details = []
    for task in tasks:
        subject_totals[task["subject"]] += task["time_logged"]
        task_details.append({
            "Subject": task["subject"],
            "Description": task["description"],
            "Deadline": task["deadline"],
            "Estimated Time": task["time_required"],
            "Time Logged": task["time_logged"]
        })
    print(tabulate(task_details, headers="keys", tablefmt="grid"))
    summary = [{"Subject": k, "Total Time Logged": v} for k, v in subject_totals.items()]
    print(tabulate(summary, headers="keys", tablefmt="grid"))

# Handles user inputs and calls the appropriate functions based on the user's choice
def main():
    tasks = load_tasks()
    
    while True:
        print("Study Scheduler - Main Menu")
        print("1. Add a New Task")
        print("2. View Tasks")
        print("3. Delete a Task")
        print("4. Build Study Schedule")
        print("5. Start Pomodoro Timer")
        print("6. Generate Report")
        print("7. Exit")
        
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
                view_tasks(tasks)
                try:
                    task_num = int(input("Enter the task number to start Pomodoro (0 to cancel): ")) - 1
                    if task_num == -1:
                        print("Pomodoro timer canceled.")
                        continue
                    if 0 <= task_num < len(tasks):
                        selected_task = tasks[task_num]
                        start_pomodoro(selected_task["subject"], 25, 5)  # 25 minutes work, 5 minutes break
                    else:
                        print("Invalid task number.")
                except ValueError:
                    print("Invalid input. Please enter a valid task number.")
            else:
                print("No tasks available. Please add tasks first.")
        elif choice == '6':
            generate_report(tasks)
        elif choice == '7':
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()