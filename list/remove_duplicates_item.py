"""Remove duplicate items from list."""

colors = ["red", "green", "yellow", "blue", "green", "red"]

unique_colors = []
index = 0
length = len(colors)

while index < length:
    current_color = colors[index]

    if current_color not in unique_colors:
        unique_colors.append(current_color)
    index += 1

print(f"Unique colors: {unique_colors}")
