from tower import Tower


def main():
    tower = Tower()
    tower.print_tower()
    initial_rod = "one"
    final_rod = "two"
    tower.initialise_tower(initial_rod)
    tower.solve(initial_rod, final_rod)


if __name__ == "__main__":
    main()
