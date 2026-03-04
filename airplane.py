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
boeing =  Plane(
            side_text="Southwind",
            main_color="white",
            addinal_colors=["red"],
            side_doors_color=5,
            autopilot=False,
        )

print(f"Plane text: {boeing.side_text}")

