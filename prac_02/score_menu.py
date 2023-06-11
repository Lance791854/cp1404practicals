

def main():

    print_menu()
    choice = ""
    choice = input("> ").upper()
    while choice != "Q":
        if choice == "G":
            score = get_valid_score(int(input("Enter Score: ")))
        elif choice == "P":
            user_score = calculate_result(score)
            print(user_score)
        elif choice == "S":
            print("*" * score)
        else:
           print("Invalid Input")
        print_menu()
        choice = input("> ").upper()
    print("Farewell")


def get_valid_score(user_score):
    while user_score < 0 or user_score > 100:
        print("Invalid Score")
        user_score = int(input("Enter Score: "))
    return user_score


def print_menu():
    menu = """(G)et a valid score
(P)rint result
(S)how stars
(Q)uit"""
    print(menu)


def calculate_result(score):
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


main()
