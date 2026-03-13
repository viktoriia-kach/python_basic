from amoeba import Amoeba


class Lancelet(Amoeba):
    organization = "multi-cell"
    support = "notochord"

    @classmethod
    def describe(cls):
        description = super().describe()
        return description + f" It has {cls.support} for support."

    @staticmethod
    def move(direction):
        print(f"Moves to the {direction} with muscles")

    def eat(self, subject):
        print(f"{self.name.capitalize()} filters water"
              f" to eat {subject}")


if __name__ == '__main__':
    print(Lancelet.describe())
    # Output: Lancelet has multi-cell organization and lives in water. It has notochord for support.

    lancelet = Lancelet("Amphioxus")
    lancelet.move("right")
    # Output: Moves to the right with muscles
    lancelet.eat("organic particles")
    # Output: Amphioxus filters water to eat organic particles
