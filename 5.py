colors = ["red", "green", "blue", "yellow", "black", "white"]
color = input("Enter a color: ")

if color in colors:
    print(f"The color is found at index {colors.index(color)}")
else:
    print("Sorry, I could not find your color")
