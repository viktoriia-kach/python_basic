class Flat:
    def __init__(self, number):
        self.number = number
        self.door_color = "brown"
        self.electricity_readings = 0

    def display_number(self):
        print(f"Flat number is {self.number}")


if __name__ == '__main__':
    flat = Flat(212)

    flat.display_number()
    # Output: Flat number is 212
    print(f"Flat has {flat.door_color} door color")
    # Output: Flat has brown door color
    print(f"Electricity readings for flat {flat.number} "
          f"are {flat.electricity_readings}")
    # Output: Electricity readings for flat 212 are 0
