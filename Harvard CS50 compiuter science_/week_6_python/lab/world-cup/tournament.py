import csv
import sys
import random

# Number of simluations to run
N = 1000


def main():

    # Ensure correct usage
    if len(sys.argv) != 2:
        sys.exit("Usage: python tournament.py FILENAME")

    teams = []
    filename = sys.argv[1]
    # открываем csv, извлекаем названия и рейтинг
    # названия и рейтинги словарями добавляем в список teams
    with open(filename) as file:
        reader = csv.DictReader(file)
        for i in reader:
            i["rating"] = int(i["rating"])
            teams.append(i)

    counts = {}

    # симуляция игр
    # проводим N циклов симуляций
    for i in range(N):

        # попбедителя определяем в функции
        win = simulate_tournament(teams)

        # записываем победителя и количество побед в словарь
        if win in counts:
            counts[win] += 1
        else:
            counts[win] = 1

    # Print each team's chances of winning, according to simulation
    for team in sorted(counts, key=lambda team: counts[team], reverse=True):
        print(f"{team}: {counts[team] * 100 / N:.1f}% chance of winning")


def simulate_game(team1, team2):
    """Simulate a game. Return True if team1 wins, False otherwise."""
    rating1 = team1["rating"]
    rating2 = team2["rating"]
    probability = 1 / (1 + 10 ** ((rating2 - rating1) / 600))
    return random.random() < probability


def simulate_round(teams):
    """Simulate a round. Return a list of winning teams."""
    winners = []

    # Simulate games for all pairs of teams
    for i in range(0, len(teams), 2):
        if simulate_game(teams[i], teams[i + 1]):
            winners.append(teams[i])
        else:
            winners.append(teams[i + 1])

    return winners


def simulate_tournament(teams):
    """Simulate a tournament. Return name of winning team."""

    # если команд в списке больше одной то повторяем цикл
    while len(teams) > 1:

        # вызываем функцию с симуляцией раундов
        # обратно получаем название команды
        teams = simulate_round(teams)

    return teams[0]["team"]


if __name__ == "__main__":
    main()