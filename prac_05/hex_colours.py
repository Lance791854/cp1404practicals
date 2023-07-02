Color_name_to_color_code = {"Absolute Zero": "#0048ba", "Acid Green": "#b0bf1a", "AliceBlue": "#f0f8ff",
                            "Alizarin crimson": "#e32636", "Amaranth": "#e52b50", "Amber": "#ffbf00",
                            "Amethyst": "#9966cc", "AntiqueWhite": "#faebd7", "AntiqueWhite1": "#ffefdb",
                            "AntiqueWhite2": "#eedfcc"}

color_name = input("Enter a color name: ").lower()
while color_name != "":
    for color in Color_name_to_color_code:
        if color.lower() == color_name:
            print(Color_name_to_color_code[color])
    color_name = input("Enter a color name: ").lower()
