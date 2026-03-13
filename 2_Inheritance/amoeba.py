class Amoeba:
    organization = "single-cell"
    habitation = "water"

    def __init__(self, name):
        self.name = name

    @classmethod
    def describe(cls):
        return (f"{cls.__name__} has {cls.organization} organization"
                f" and lives in {cls.habitation}.")

    @staticmethod
    def move(direction):
        print(f"Moves to the {direction} with pseudopodia")

    def eat(self, subject):
        print(f"{self.name.capitalize()} grows pseudopodia"
              f" to eat {subject}")

if __name__ == '__main__':
    print(Amoeba.describe())
    # Output: Amoeba has single-cell organization and lives in water

    amoeba = Amoeba("proteus")
    amoeba.move("left")
    # Output: Moves to the left with pseudopodia
    amoeba.eat("bacteria")
    # Output: Proteus grows pseudopodia to eat bacteria