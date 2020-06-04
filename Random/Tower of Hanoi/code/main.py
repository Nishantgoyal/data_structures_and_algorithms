from tower import Tower


def main():
    tower = Tower()
    initial_rod = "one"
    final_rod = "two"
    tower.initialise_tower(initial_rod)
    tower.print_tower()
    tower.solve(initial_rod, final_rod)


if __name__ == "__main__":
    main()
