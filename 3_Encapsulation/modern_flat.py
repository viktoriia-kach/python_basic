from flat import Flat


class ModernFlat(Flat):
    def __init__(self, number):
        super().__init__(number)
        self._room_number = 3
        self._design = "modern"
        self._has_tv = True

    def get_room_number(self, friend=False):
        return self._room_number if friend else 0

    def get_design(self, friend=False):
        return self._design if friend else "undefined"

    def update_design(self, design, friend=False):
        if friend and design.startswith("modern"):
            self._design = design

    def turn_on_tv(self, friend=False):
        if friend and self._has_tv:
            print("TV turned on")
        else:
            print("Not defined")


if __name__ == '__main__':
    flat = ModernFlat(212)

    flat.display_number()
    # Output: Flat number is 212
    print(flat.get_design())
    # Output: undefined
    print(flat.get_design(friend=True))
    # Output: modern
    flat.update_design("modern warm", friend=True)
    print(flat.get_design(friend=True))
    # Output: modern warm

    flat._room_number = 4
    print(flat.get_room_number(friend=True))
    # Output: 4

    flat._design = "some design"
    print(flat.get_design(friend=True))
    # Output: some design

    flat._has_tv = False
    flat.turn_on_tv(friend=True)
    # Output: Not defined
