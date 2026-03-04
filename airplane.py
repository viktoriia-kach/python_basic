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

        # create екземпляр класу
airbus =  Plane(
            side_text="Delta",
            main_color="white",
            addinal_colors=["red", "blue"],
            side_doors_color=4,
            autopilot=False,
        )

print(f"Additional colors: {', '.join(airbus.addinal_colors)}")

