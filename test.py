# Right triangle (left-aligned)
def print_right_triangle(height, char="*"):
    for i in range(1, height + 1):
        print(char * i)

# Isosceles (centered, filled)
def print_isosceles(height, char="*"):
    for i in range(height):
        spaces = height - i - 1
        stars = 2 * i + 1
        print(" " * spaces + char * stars)

# Hollow isosceles triangle
def print_hollow_isosceles(height, char="*"):
    if height <= 0:
        return
    # top
    print(" " * (height - 1) + char)
    # middle rows
    for i in range(1, height - 1):
        spaces_out = height - i - 1
        spaces_in = 2 * i - 1
        print(" " * spaces_out + char + " " * spaces_in + char)
    # bottom (only if height > 1)
    if height > 1:
        print(char * (2 * height - 1))

# Example usage:
if __name__ == "__main__":
    print("Right triangle (height=5):")
    print_right_triangle(5)
    print("\nIsosceles triangle (height=5):")
    print_isosceles(5)
    print("\nHollow isosceles triangle (height=6):")
    print_hollow_isosceles(6)
