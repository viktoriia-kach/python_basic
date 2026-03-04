class Plane:
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

    def take_off (self):  # зліт
        print(f"{self.side_text} takes off")

    def land (self):  # приземлення
           print(f"{self.side_text} lans")
