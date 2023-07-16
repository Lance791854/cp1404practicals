from prac_06.guitar import Guitar

Gibson = Guitar("Gibson L-5 CES", 1922, 16035.40)
Lemon = Guitar("Lemon G-3 LAM", 2000, 403.10)

print(Gibson.get_age())  # expected 101. Got 100
print(Lemon.get_age())  # expected 23. Got 9
print(Gibson.is_vintage())  # expected True. Got True
print(Lemon.is_vintage())  # expected False. Got False
