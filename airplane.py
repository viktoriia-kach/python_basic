class Plane:
    engine_type = "turbofan" #класовий атрибут
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
    def inspect_engine(cls):     #класовий метод
         print(f"Plane as: {cls.engine_type}")

    def take_off (self):  # зліт
        print(f"{self.side_text} takes off")

    def land (self):  # приземлення
           print(f"{self.side_text} lans")

Plane.inspect_engine()