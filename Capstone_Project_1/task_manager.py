# Notes: 
# 1. Use the following username and password to access the admin rights 
# username: admin
# password: password
# 2. Ensure you open the whole folder for this task in VS Code otherwise the 
# program will look in your root directory for the text files.

# =====importing libraries===========
import os
from datetime import datetime, date

DATETIME_STRING_FORMAT = "%Y-%m-%d"


def show_menu(string):
    print(string + " or select one of the options below:")
    print("b - Go back to Main Menu")
    return input(":")


# Calculate and return a string with the percentage
def percentage(parts, whole):
    return f'{round((parts / whole * 100), 2)}%'


def edit_due_date():
    while True:
        try:
            task_due_date = input("Due date of task (YYYY-MM-DD): ")
            due_date = datetime.strptime(task_due_date, DATETIME_STRING_FORMAT)
            break

        except ValueError:
            print("Invalid datetime format. Please use the format specified")
    return due_date


def edit_username():
    username = input("Enter the username of the person assigned to task: ")
    if username in ["b", ""]:
        return "b"
    elif username not in accounts:
        print("The username does not exist. Select one of the options below:\nb - Go back to Main Menu")
        # Call the function recursive if the input is not valid
        return edit_username()
    else:
        return username


def write_task_file(tasks):
    with open("tasks.txt", "w") as file:
        task_list_to_write = []
        for t in tasks:
            str_attrs = [
                t['username'],
                t['title'],
                t['description'],
                t['due_date'].strftime(DATETIME_STRING_FORMAT),
                t['assigned_date'].strftime(DATETIME_STRING_FORMAT),
                "Yes" if t['completed'] else "No"
            ]
            task_list_to_write.append(";".join(str_attrs))
        file.write("\n".join(task_list_to_write))


# Define functions
def reg_user():
    """Add a new user to the user.txt file"""
    # - Request input of a new username
    new_username = input("New Username: ")
    while new_username in accounts:
        new_username = show_menu(
            "\nThe username already exists.\nEnter another user name")

    # if input is b or empty return to main menu
    if new_username.strip() in ["b", ""]:
        return

    # - Request input of a new password
    new_password = input("New Password: ")

    # - Request input of password confirmation.
    confirm_password = input("Confirm Password: ")

    # - Check if the new password and confirmed password are the same.
    if new_password == confirm_password:
        # - If they are the same, add them to the user.txt file,
        print("New user added")
        accounts[new_username] = new_password

        with open("user.txt", "w") as out_file:
            # Write the users and their passwords in the file
            out_file.write("\n".join([f"{k};{accounts[k]}" for k in accounts]))

    # - Otherwise you present a relevant message.
    else:
        print("The user entered has not been added since the passwords do no match")


def add_task():
    """Allow a user to add a new task to task.txt file
    Prompt a user for the following:
    - A username of the person whom the task is assigned to,
    - A title of a task,
    - A description of the task and
     - the due date of the task."""
    task_username = edit_username()
    if task_username == "b":
        return

    task_title = input("Title of Task: ")
    while task_title.strip() == "":
        task_title = show_menu("Task title can't be empty. Please enter a valid task title")

    if task_title == "b":
        return

    task_description = input("Description of Task: ")
    while task_description.strip() == "":
        task_description = show_menu("Task title can't be empty. Please enter a valid task title")

    if task_description == "b":
        return

    due_date_time = edit_due_date()

    # Then get the current date.
    curr_date = date.today()
    ''' Add the data to the file task.txt and
        Include 'No' to indicate if the task is complete.'''
    new_task = {
        "username": task_username,
        "title": task_title,
        "description": task_description,
        "due_date": due_date_time,
        "assigned_date": curr_date,
        "completed": False
    }

    task_list.append(new_task)
    write_task_file(task_list)
    print("Task successfully added.")


def view_all():
    """Reads the task from task.txt file and prints to the console in the
        format of Output 2 presented in the task pdf (i.e. includes spacing
        and labelling)"""

    for idx, t in enumerate(task_list):
        disp_str = f"Task {idx}: \t\t {t['title']}\n"
        disp_str += f"Assigned to: \t {t['username']}\n"
        disp_str += f"Date Assigned: \t {t['assigned_date'].strftime(DATETIME_STRING_FORMAT)}\n"
        disp_str += f"Due Date: \t\t {t['due_date'].strftime(DATETIME_STRING_FORMAT)}\n"
        disp_str += f"Task Description: \n {t['description']}\n"
        print(disp_str)


def view_mine():
    """Reads the task from task.txt file and prints to the console in the
    format of Output 2 presented in the task pdf (i.e. includes spacing
    and labelling)"""

    index = 0
    for t in task_list:
        if t['username'] == curr_user:
            disp_str = f"Task {index}: \t\t {t['title']}\n"
            disp_str += f"Assigned to: \t {t['username']}\n"
            disp_str += f"Date Assigned: \t {t['assigned_date'].strftime(DATETIME_STRING_FORMAT)}\n"
            disp_str += f"Due Date: \t\t {t['due_date'].strftime(DATETIME_STRING_FORMAT)}\n"
            disp_str += f"Task Description: \n {t['description']}\n"
            print(disp_str)
            index += 1
    if index == 0:
        print("No tasks assigned for this user.")
        return

    while True:
        # Ask user to select task
        try:
            task_select = int(input("""Type the number of the task to select it.
Or type '-1' to go back to the main menu : \n"""))

        except ValueError:
            task_select = -1
            print("Invalid option selected. Please use the format specified")

        if task_select == -1:
            return

        elif task_select > len(task_list) - 1:
            print("There is no task with this identifier.\n")

        else:
            # Ask the user to choose an option, edit is displayed only if the selected task is not completed
            task_option = input(f"""Select one of the following Options below:
m - Mark the task as complete
{(not task_list[task_select]["completed"]) * "ed - Edit the task"}\n""").lower()
            if task_option == "m":
                # Change the task's completed value to True
                task_list[task_select]["completed"] = True
                print(f"Task number {task_select} has been marked as completed\n")
            elif task_option == "ed":
                # Ask the user to change the username and/or due date
                task_username = edit_username()
                if task_username == "b":
                    break
                else:
                    task_list[task_select]["username"] = task_username
                task_list[task_select]["due_date"] = edit_due_date()
                print("Task successfully edited.")
                break
            else:
                print("You have made a wrong choice, Please Try again\n")

            # Add the changes to the task.txt file
            write_task_file(task_list)
            return


def generate_report(tasks, users):
    # Get the current date
    curr_date = datetime.today()
    # Create a dictionary for the full report
    report = {"total_tasks": len(tasks),
              "total_users": len(users),
              "total_completed": 0,
              "overdue": 0,
              "users": {}
              }

    for task in tasks:
        # Check if username is in the users dictionary
        if task["username"] not in report["users"]:
            # Create a dictionary for that user inside
            report["users"][task["username"]] = {"nr_of_tasks": 0, "completed": 0, "overdue": 0}

        # Increase the number of task of a specific user
        report["users"][task["username"]]["nr_of_tasks"] += 1

        # Check if task is completed and add it to the report dictionary
        if task["completed"]:
            report["total_completed"] += 1
            report["users"][task["username"]]["completed"] += 1

        # Check if task is not completed and overdue and add it to the report dictionary
        if task["due_date"] < curr_date and task["completed"] is not True:
            report["overdue"] += 1
            report["users"][task["username"]]["overdue"] += 1

    # Go through all the users to add the ones that don't have tasks assigned
    for user in user_data:
        user = user.split(";")[0]
        if user not in report["users"]:
            report["users"][user] = {"nr_of_tasks": 0, "completed": 0, "overdue": 0}

    # Write the output files
    with open("task_overview.txt", "w") as task_overview_file, open("user_overview.txt", "w") as user_overview_file:
        task_overview_file.write(f"""----------------------------------------------------
Task Overview Report
Date : {curr_date.strftime('%Y-%m-%d')}
----------------------------------------------------
Total number of tasks :                      {report["total_tasks"]}
Total number of completed tasks :            {report["total_completed"]}
Total number of uncompleted tasks :          {report["total_tasks"] - report["total_completed"]}
Total number of overdue uncompleted tasks:   {report["overdue"]}
The percentage of tasks that are incomplete: {round((report["total_tasks"] - report["total_completed"]) / report["total_tasks"] * 100, 2)}% 
The percentage of tasks that are overdue:    {round(report["overdue"] / report["total_tasks"] * 100, 2)}%""")

        user_overview_file.write(f"""------------------------------------
User Overview Report
Date : {curr_date.strftime('%Y-%m-%d')}
--------------------------------------------------
Total number of user :                       {report["total_users"]}
Total number of tasks :                      {report["total_tasks"]}
--------------------------------------------------""")
        for user in report["users"]:
            try:
                user_overview_file.write(f"""\nUsername : {user}
Total number of tasks assigned to the user :                                                   {report["users"][user]["nr_of_tasks"]}
Percentage of the total number of tasks that have been assigned to the user :                  {percentage(report["users"][user]["nr_of_tasks"], report["total_tasks"])}
Percentage of the tasks assigned to the user that have completed :                             {percentage(report["users"][user]["completed"], report["users"][user]["nr_of_tasks"])}
Percentage of the tasks assigned to the user that must still be completed :                    {percentage((report["users"][user]["nr_of_tasks"] - report["users"][user]["completed"]), report["users"][user]["nr_of_tasks"])}
Percentage of the tasks assigned to the user that have not yet been completed and are overdue: {percentage(report["users"][user]["overdue"], report["users"][user]["nr_of_tasks"])}
-----------------------------------------------------------------------------------------------------""")
            except ZeroDivisionError:
                user_overview_file.write(f"""\nUsername : {user}
Total number of tasks assigned to the user :                                                   0
Percentage of the total number of tasks that have been assigned to the user :                  0%
Percentage of the tasks assigned to the user that have completed :                             0%
Percentage of the tasks assigned to the user that must still be completed :                    0%
Percentage of the tasks assigned to the user that have not yet been completed and are overdue: 0%
-----------------------------------------------------------------------------------------------------""")


def display_raport():
    with open("task_overview.txt", "r") as task_overview_file, open("user_overview.txt", "r") as user_overview_file:
        print("--------------------- Report ---------------------")
        for line, content in enumerate(task_overview_file):
            if line not in [0, 1, 3]:
                print(content[:-1])
        for line, content in enumerate(user_overview_file):
            if line not in [0, 1, 2, 3, 5]:
                print(content[:-1])


# Create tasks.txt if it doesn't exist
if not os.path.exists("tasks.txt"):
    with open("tasks.txt", "w") as default_file:
        pass

with open("tasks.txt", 'r') as task_file:
    task_data = task_file.read().split("\n")
    task_data = [t for t in task_data if t != ""]

task_list = []
for t_str in task_data:
    curr_t = {}

    # Split by semicolon and manually add each component
    task_components = t_str.split(";")
    curr_t['username'] = task_components[0]
    curr_t['title'] = task_components[1]
    curr_t['description'] = task_components[2]
    curr_t['due_date'] = datetime.strptime(task_components[3], DATETIME_STRING_FORMAT)
    curr_t['assigned_date'] = datetime.strptime(task_components[4], DATETIME_STRING_FORMAT)
    curr_t['completed'] = True if task_components[5] == "Yes" else False

    task_list.append(curr_t)

# ====Login Section====
'''This code reads usernames and password from the user.txt file to 
    allow a user to login.
'''
# If no user.txt file, write one with a default account
if not os.path.exists("user.txt"):
    with open("user.txt", "w") as default_file:
        default_file.write("admin;password")

# Read in user_data
with open("user.txt", 'r') as user_file:
    user_data = user_file.read().split("\n")

# Convert to a dictionary
accounts = {account.split(";")[0]: account.split(";")[1] for account in user_data}

logged_in = False
while not logged_in:

    print("LOGIN")
    curr_user = input("Username: ")
    curr_pass = input("Password: ")
    if curr_user not in accounts.keys():
        print("User does not exist")
        continue
    elif accounts[curr_user] != curr_pass:
        print("Wrong password")
        continue
    else:
        print("Login Successful!")
        logged_in = True

while True:
    # presenting the menu to the user and
    # making sure that the user input is converted to lower case.
    print()
    menu = input(f'''Select one of the following Options below:
r - Registering a user
a - Adding a task
va - View all tasks
vm - View my task
{"""gr - Generate reports
ds - Display statistics
e - Exit""" if (curr_user == "admin") else "e - Exit"}
: ''').lower()

    if menu == 'r':
        reg_user()

    elif menu == 'a':
        add_task()

    elif menu == 'va':
        if len(task_list) == 0:
            print("There are no tasks available.")
        else:
            view_all()

    elif menu == 'vm':
        view_mine()

    elif menu == 'gr' and curr_user == 'admin':
        '''If the user is an admin they can display statistics about number of users
            and tasks.'''
        if len(task_list) == 0:
            print("There are no tasks available.")
        else:
            generate_report(task_list, user_data)

    elif menu == 'ds' and curr_user == 'admin':
        '''If the user is an admin they can display statistics about number of users
            and tasks.'''
        if len(task_list) == 0:
            print("There are no tasks available.")
        else:
            # Check if the reports have been generated, if not generate them
            if not (os.path.exists("task_overview.txt") or os.path.exists("user_overview.txt")):
                generate_report(task_list, user_data)

            display_raport()

    elif menu == 'e':
        print('Goodbye!!!')
        exit()

    else:
        print("You have made a wrong choice, Please Try again")
