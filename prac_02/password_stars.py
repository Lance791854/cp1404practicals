def main():
    minimum_pass_length = 8

    user_password = get_password(minimum_pass_length)

    print_stars(user_password)


def print_stars(user_password):
    print("*" * len(user_password))


def get_password(minimum_pass_length):
    user_password = input("Your password: ")
    while len(user_password) < minimum_pass_length:
        print(f"Password must be {minimum_pass_length} characters or longer.")
        user_password = input("Your password: ")
    return user_password


main()
