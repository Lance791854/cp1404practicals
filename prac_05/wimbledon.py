"""
wimbledon
Estimate: 50 minutes
Actual:   60 minutes
"""


def main():
    wimbledon_stats = read_file()

    champions = count_champion_wins(wimbledon_stats)

    print("Wimbledon Champions:")
    for champ, wins in champions.items():
        print(f"{champ:} {wins}")

    country_wins = count_country_wins(wimbledon_stats)

    sorted_countries = sorted(country_wins)
    winning_countrys = ", ".join(sorted_countries)
    print(f"\nThese {len(country_wins)} countries have won Wimbledon:")
    print(winning_countrys)


def count_country_wins(wimbledon_stats):
    country_wins = set()
    for win in wimbledon_stats:
        winning_country = win[1]
        country_wins.add(winning_country)
    return country_wins


def count_champion_wins(wimbledon_stats):
    champions = {}
    for champ in wimbledon_stats:
        champion = champ[2]
        if champion in champions:
            champions[champion] += 1
        else:
            champions[champion] = 1
    return champions


def read_file():
    wimbledon_stats = []
    filename = "wimbledon.csv"
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        lines = in_file.readlines()[1:]
        for line in lines:
            line = line.split(",")
            wimbledon_stats.append(line)
    return wimbledon_stats


main()
