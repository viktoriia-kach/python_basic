from modern_flat import ModernFlat


class SafeFlat(ModernFlat):
    def __init__(self, number):
        super().__init__(number)
        self.__has_safe = True
        self.__safe_content = ["money", "documents"]
        self.__price = 100000

    def describe(self, friend=False, owner=False):
        description = (
            f"Flat {self.number} has {self.door_color} "
            f"door color and {self.electricity_readings} "
            f"electricity count.\n"
        )
        friend_description = (
            f"Flat has {self._design} design and "
            f"rooms count is {self._room_number}. "
            f"The flat has{' ' if self._has_tv else ' no '}TV.\n"
        )
        owner_description = (
            f"The flat price is {self.__price} USD. The "
            f"flat has{' ' if self.__has_safe else ' no '}safebox. "
            f"The safe content is: "
            f"{', '.join(self.__safe_content) if self.__safe_content else 'empty'}."
        )

        if friend:
            description += friend_description

        if owner:
            description += friend_description + owner_description

        print(description)


if __name__ == '__main__':
    flat = SafeFlat(212)

    flat.describe()
    # Output:
    # Flat 212 has brown door color and 0 electricity count.
    flat.describe(friend=True)
    # Output:
    # Flat 212 has brown door color and 0 electricity count.
    # Flat has modern design and rooms count is 3. The flat has TV.
    flat.describe(owner=True)
    # Output:
    # Flat 212 has brown door color and 0 electricity count.
    # Flat has modern design and rooms count is 3. The flat has TV.
    # The flat price is 100000 USD. The flat has safebox. The safe content is: money, documents.

    flat.__has_safe = False
    flat.__safe_content = []
    flat.__price = 1000
    print("\n")
    flat.describe(owner=True)
    # Output:
    # Flat 212 has brown door color and 0 electricity count.
    # Flat has modern design and rooms count is 3. The flat has TV.
    # The flat price is 100000 USD. The flat has safebox. The safe content is: money, documents.

    flat._SafeFlat__has_safe = False
    flat._SafeFlat__safe_content = []
    flat._SafeFlat__price = 1000
    print("\n")
    flat.describe(owner=True)
    # Output:
    # Flat 212 has brown door color and 0 electricity count.
    # Flat has modern design and rooms count is 3. The flat has TV.
    # The flat price is 1000 USD. The flat has no safebox. The safe content is: empty.
