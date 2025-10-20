# 💻 Challenge: Safe Undo System

# Scenario:
# You’re writing a program that manages a list of user tasks.
# Every time the user adds or removes a task, the system should save a snapshot of the list so they can undo their last change.

# But — here’s the catch:
# If you use shallow copies incorrectly, the undo will not work properly.

# 🧠 Your Task:

# Write a Python script that:

# Starts with an empty list called tasks.

# Every time a user enters a new task (using input()), add it to the list.

# Keep a history list that stores copies of tasks before every change.

# Allow the user to type:

# "undo" → undo the last change (restore the previous snapshot)

# "show" → display the current list of tasks

# "exit" → quit the program

# Use deepcopy to ensure that the undo system works correctly.

# ⚡ Extra rule (to make it a real test):

# You cannot use global variables outside the main loop except for tasks and history.
# So you must handle the logic carefully.
# in this activity i borrowed the a concept of Data Structures and Algorithms(DSA) mentioning pop.
# this activity uses the concepts of functions, deepcopy from copy library, lists, and conditionals(if else statements).
# it also displays the global variable concept, as well as while loop.
import copy

tasks = []
history = []
def main():
    global tasks, history
    user_input = str(input("What do you wanna do? (add, undo, show, exit): "))
    
    if user_input == "add":
        history.append(copy.deepcopy(tasks))
        input2 = input("Enter a new Task: ")
        tasks.append(input2)
    elif user_input == "undo":
        if history:
            tasks = history.pop()  # Restore last snapshot
            print("Last action undone.")
        else:
            print("No actions to undo.")
    elif user_input == "show":
        print(tasks)
    elif user_input == "exit":
        command = "exit"
        return command
    else:
        print("Invalid input")


while main() != "exit":
     pass
