from lancelet import Lancelet


class Koala(Lancelet):
    habitation = "forest"
    support = "skeleton"

    def __init__(self, name, sleeping=False):
        super().__init__(name)
        self.sleeping = sleeping

    def eat(self, subject):
        if not self.sleeping:
            self.move("top")
            print(f"{self.name.capitalize()} climbs to "
                  f"the tree to eat {subject}")
        else:
            print(f"{self.name.capitalize()} cannot eat while sleeping")

    def change_state(self):
        if self.sleeping:
            print(f"{self.name.capitalize()} wakes up and sits on a branch")
        else:
            print(f"{self.name.capitalize()} lies on a branch and sleeps")

        self.sleeping = not self.sleeping


if __name__ == '__main__':
    print(Koala.describe())
    # Output: Koala has multi-cell organization and lives in forest. It has skeleton for support.

    koala = Koala(name="Phascolarctos")
    koala.move("right")
    # Output: Moves to the right with muscles
    koala.eat("eucalyptus leaves")
    # Output: Moves to the top with muscles
    # Output: Phascolarctos climbs to the tree to eat eucalyptus leaves
    koala.change_state()
    # Output: Phascolarctos lies on a branch and sleeps
    koala.eat("eucalyptus leaves")
    # Output: Phascolarctos cannot eat while sleeping
    koala.change_state()
    # Output: Phascolarctos wakes up and sits on a branch
