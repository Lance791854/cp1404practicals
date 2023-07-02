"""
emails
Estimate: 30 minutes
Actual:   35 minutes
"""

user_email = input("Email: ")
emails_and_names = {}

while user_email != "":
    name_parts = user_email.split("@")
    user_name = name_parts[0].split(".")
    name = " ".join(user_name)
    name_response = input(f"Is your name {name.title()}? (Y/n) ")
    if name_response != "y" and name_response != "":
        name = input("Name: ")

    emails_and_names[user_email] = name
    user_email = input("Email: ")

print()  # Wasn't sure how else to add a new line between the output and last email input request
for email, name in emails_and_names.items():
    print(f"{name} ({email:})")
