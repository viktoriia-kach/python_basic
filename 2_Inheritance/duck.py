class Flyer:
    @staticmethod
    def fly():
        print("Flying")


class Swimmer:
    @staticmethod
    def swim():
        print("Swimming")


class Duck(Flyer, Swimmer):
    @staticmethod
    def quack():
        print("Quacking")


duck = Duck()
duck.fly()  # Output: Flying
duck.swim()  # Output: Swimming
duck.quack()  # Output: Quacking
