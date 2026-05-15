"""Remove duplicate items from list."""

colors = ["red", "green", "yellow", "blue", "green", "red"]

unique_colors = list(dict.fromkeys(colors))
print(f"Unique colors: {unique_colors}")
