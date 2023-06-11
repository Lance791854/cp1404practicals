"""
CP1404/CP5632 - Practical
Pseudocode for temperature conversion
"""


def main():

    print_menu()

    choice = input(">>> ").upper()

    while choice != "Q":
        if choice == "C":
            calculate_celsius_to_fahrenheit()
        elif choice == "F":
            calculate_fahrenheit_to_celsius()
        else:
            print("Invalid option")
        print_menu()
        choice = input(">>> ").upper()
    print("Thank you.")


def print_menu():
    MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""
    print(MENU)
    return MENU


def calculate_celsius_to_fahrenheit():
    global celsius, fahrenheit
    celsius = float(input("Celsius: "))
    fahrenheit = celsius * 9.0 / 5 + 32
    print(f"Result: {fahrenheit:.2f} F")


def calculate_fahrenheit_to_celsius():
    global fahrenheit, celsius
    fahrenheit = float(input("Fahrenheit: "))
    celsius = 5 / 9 * (fahrenheit - 32)
    print(f"Result: {celsius:.2f} °C")


main()
