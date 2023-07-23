"""
Project Management
Time to complete: 70 minutes
"""

import datetime


def main():
    Menu = """- (L)oad Projects
- (S)ave projects
- (D)isplay Projects
- (F)ilter projects by date
- (A)dd new project
- (U)pdate project"""
    FILENAME = "projects.txt"
    projects = load_file(FILENAME)
    print(projects)
    print(Menu)
    User_Choice = input(">>> ").upper()
    while User_Choice != "":
        if User_Choice == "L":
            projects = load_projects(FILENAME)
        elif User_Choice == "S":
            save_project(FILENAME, projects)
        elif User_Choice == "D":
            print("NO")
        elif User_Choice == "F":
            print("NO")
        elif User_Choice == "A":
            print("NO")
        elif User_Choice == "U":
            print("NO")
        print(Menu)
        User_Choice = input(">>> ").upper()


def load_file(filename):
    projects = []
    in_file = open(filename, 'r', newline='')
    in_file.readline()
    for row in in_file:
        projects.append(row)

    return projects


def load_project(projects):
    updated_projects = []
    Filename = input("Filename: ")

    return updated_projects


def save_project(filename, projects):
    out_file = open(filename, 'w', newline='')
    out_file.readline()
    for project in projects:
        out_file.write(project)


main()
