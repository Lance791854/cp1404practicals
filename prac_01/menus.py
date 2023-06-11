name = input("Enter name: ")
print("(H)ello\n(G)oodbye\n(Q)uit")

user_choice = input(">>> ").lower()
while user_choice != "q":
    if user_choice == "h":
        print(f"Hello {name}")
    else:
        print(f"Goodbye {name}")
    user_choice = input(">>> ").lower()

print("Finished.")
