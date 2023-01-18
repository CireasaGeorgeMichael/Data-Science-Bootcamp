Capstone project 1 : Tasks management script with Python

Requirements :
- Create a python script that can be used for the management of tasks on a projects.
- The task manager should have the following options:
  - Register a new user.
    - Ask user to input new username and password
    - Add new username and password to the users .txt file
  - Add a new task
    - Ask user to input a title, description, date, user assigned for a new task.
    - Add new task to the tasks .txt file
  - View all tasks
    - Display all the tasks in the console.
  - View only users tasks
    - Display only the tasks  of the logged-in user in the console.
  - Generate report (only admin)
    - Generate a report of all the users and tasks in  separate .txt files
  - Display Statistics (only admin)
    - Display in the console the  details from the generated report.
  
To complete ths project I used:
- Define custom functions to encapsulate code that might be reused throughout the script
- .txt file creation and manipulation
- Error handling to avoid errors that stop the program from running.
- Recursive calling of functions for input validations.