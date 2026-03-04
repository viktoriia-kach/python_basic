class Plane:
    engine_type = "turbofan"  # класовий атрибут

    def __init__(
        self,  # дозволяє звертатиля до екземплярів класу
        side_text,
        main_color,
        addinal_colors,
        side_doors_color,
        autopilot,
    ):  # метод (Dunder методи)

        self.side_text = side_text  # атрибут екземпляру класу
        self.main_color = main_color
        self.addinal_colors = addinal_colors
        self.side_doors_color = side_doors_color
        self.autopilot = autopilot

    @classmethod
    def inspect_engine(cls):  # класовий метод
        print(f"Plane as: {cls.engine_type}")

    @staticmethod
    def calculate_fuel(distance):  # статичний метод
        hour_fuel = 7000
        hour_distance = 900
        fuel = (hour_fuel * distance) / hour_distance
        print(f"For {distance} km plane needs {round(fuel)} kg of fuel")

    def take_off(self):  # зліт метод
        print(f"{self.side_text} takes off")

    def land(self):  # приземлення метод
        print(f"{self.side_text} lans")

#екземпляр класу
boeing = Plane(
    side_text="Southwind",
    main_color="white",
    addinal_colors=["red"],
    side_doors_color=5,
    autopilot=False,
)

#екземпляр класу
airbus = Plane(
    side_text="Delta",
    main_color="white",
    addinal_colors=["red", "blue"],
    side_doors_color=4,
    autopilot=False,
)

Plane.calculate_fuel(1000)
boeing.calculate_fuel(3500)
airbus.calculate_fuel(5300)