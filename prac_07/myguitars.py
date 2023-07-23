class Guitar:
    def __init__(self, name="", year=0, cost=0):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        return f"{self.name} ({self.year}) : ${self.cost}"

    def __lt__(self, other):
        return self.year < other.year


def main():
    guitars = []

    in_file = open("guitars.csv", "r")
    in_file.readline()
    for line in in_file:
        parts = line.strip().split(',')
        guitar = Guitar(parts[0], int(parts[1]), float(parts[2]))
        guitars.append(guitar)

    guitars.sort()
    for guitar in guitars:
        print(guitar)


if __name__ == "__main__":
    main()
