"""Program to calculate cost and # of supplies for tea party """

__author__: str = "730621026"


def main_planner(guests: int) -> None:
    """Print Cost and # supplies per # of guests"""

    print("A Cozy Tea Party for " + str(guests) + " People!")
    print("Tea Bags:" + " " + str(tea_bags(people=guests)))
    print("Treats: " + str(treats(people=guests)))
    print("Cost: $" + str(cost(tea_bags(people=guests), treats(people=guests))))


def tea_bags(people: int) -> int:
    """Defines # of tea bags needed given # of people"""
    return 2 * people


def treats(people: int) -> int:
    """Defines # of treats needed given # of people"""
    return int(tea_bags(people=people) * 1.5)


def cost(tea_count: int, treat_count: int) -> float:
    """Cost for total # Treats and Tea bags"""
    return tea_count * 0.5 + treat_count * 0.75


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party? ")))
