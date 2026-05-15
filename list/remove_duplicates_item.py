"""Remove duplicate items from list."""

colors = ["red", "green", "yellow", "blue", "green", "red"]

unique_colors = []

for color in colors:
    if color not in unique_colors:
        unique_colors.append(color)

print(f"Unique colors: {unique_colors}")
