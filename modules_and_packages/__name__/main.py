"""Demo of __name__ ."""

import demo


if __name__ == "__main__":
    result = demo.add(first_number=10, second_number=0.5)
    print(f"Result: {result}")
