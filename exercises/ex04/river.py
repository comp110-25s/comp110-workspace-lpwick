"""File to define River class."""

__author__ = "730621026"

from exercises.ex04.fish import Fish
from exercises.ex04.bear import Bear


class River:
    day: int
    bears: list[Bear]
    fish: list[Fish]

    def __init__(self, num_fish: int, num_bears: int):
        """New River with num_fish Fish and num_bears Bears"""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for _ in range(0, num_fish):
            self.fish.append(Fish())
        for _ in range(0, num_bears):
            self.bears.append(Bear())

    def check_ages(self):
        live_fish = []
        for fish in self.fish:
            if fish.age <= 3:
                live_fish.append(fish)
        self.fish = live_fish

        live_bears = []
        for bear in self.bears:
            if bear.age <= 5:
                live_bears.append(bear)
        self.bears = live_bears

    def remove_fish(self, ammount: int) -> None:
        while ammount > 0 and self.fish:
            self.fish.pop(0)
            ammount -= 1

    def bears_eating(self):
        for bear in self.bears:
            if len(self.fish) >= 5:
                bear.eat(3)
                self.remove_fish(3)

    def check_hunger(self):
        live_bears = []
        for bear in self.bears:
            if bear.hunger_score >= 0:
                live_bears.append(bear)
        self.bears = live_bears

    def repopulate_fish(self):
        new_fish: int
        new_fish = (len(self.fish) // 2) * 4
        while new_fish > 0:
            self.fish.append(Fish())
            new_fish -= 1

    def repopulate_bears(self):
        new_bears: int
        new_bears = len(self.bears) // 2
        while new_bears > 0:
            self.bears.append(Bear())
            new_bears -= 1

    def view_river(self):
        print(f"~~~ Day {self.day}: ~~~")
        print(f"Fish population: {len(self.fish)}")
        print(f"Bear population: {len(self.bears)}")

    def one_river_day(self):
        """Simulate one day of life in the river"""
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bears
        for bear in self.bears:
            bear.one_day()
        # Simulate one day for all Fish
        for fish in self.fish:
            fish.one_day()
        # Simulate Bear's eating
        self.bears_eating()
        # Remove hungry Bear's from River
        self.check_hunger()
        # Remove old Fish and Bear's from River
        self.check_ages()
        # Simulate Fish repopulation
        self.repopulate_fish()
        # Simulate Bear repopulation
        self.repopulate_bears()
        # Visualize River
        self.view_river()

    def one_river_week(self):
        max_days: int = 6
        days: int = 0
        while days <= max_days:
            self.one_river_day()
            days += 1
