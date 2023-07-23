"""
Project Management
Time to complete: 70 minutes
"""

def main():

import csv
import datetime

    Menu = """- (L)oad Projects
- (S)ave projects
- (D)isplay Projects
- (F)ilter projects by date
- (A)dd new project
- (U)pdate project"""
    FILENAME = "projects.txt"

    projects = []

    print(Menu)
    User_Choice = input(">>> ")
    while User_Choice != "":
        if User_Choice == "L":
            projects = load_projects(FILENAME)
        elif User_Choice == "S":
        elif User_Choice == "D":
        elif User_Choice == "F":
        elif User_Choice == "A":
        elif User_Choice == "U":

    print(Menu)

def load_projects(projects):
    updated_projects = []
    Filename = input("Filename: ")


    return updated_projects



main()
