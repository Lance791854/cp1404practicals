import csv


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

    print("My guitars!")
    name = input("Name: ")
    year = int(input("Year: "))
    cost = float(input("Cost: "))
    guitars.append(Guitar(name, year, cost))

    in_file = open("guitars.csv", "r")
    in_file.readline()
    for line in in_file:
        parts = line.strip().split(',')
        guitar = Guitar(parts[0], int(parts[1]), float(parts[2]))
        guitars.append(guitar)

    guitars.sort()
    for guitar in guitars:
        print(guitar)

    out_file = open('guitars.csv', 'w', newline='')
    writer = csv.writer(out_file)
    writer.writerow(['Name', 'Year', 'Cost'])
    for guitar in guitars:
        writer.writerow([guitar.name, guitar.year, guitar.cost])
    out_file.close()


if __name__ == "__main__":
    main()
