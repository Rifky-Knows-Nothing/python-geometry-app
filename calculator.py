# --- Simple Geometry Calculator ---
import math

def calculate_square_area(side):
    """Calculates the area of a square given its side length."""
    if side < 0:
        # Simple error handling
        return "Error: Side length cannot be negative."
    return side * side

def calculate_circle_area(radius):
    """Calculates the area of a circle given its radius."""
    if radius < 0:
        return "Error: Radius cannot be negative."
    return math.pi * radius * radius

def calculate_triangle_area(base, height):
    """Calculates the area of a triangle given its base and height."""
    if base < 0 or height < 0:
        return "Error: Base and height cannot be negative."
    return 0.5 * base * height

def run_calculator_app():
    """Runs the interactive geometry calculator application."""
    print("--- Geometry Calculator ---")

    try:
        # Get inputs
        square_side = float(input("Enter the side length of the square: "))
        circle_radius = float(input("Enter the radius of the circle: "))
        triangle_base = float(input("Enter the base of the triangle: "))
        triangle_height = float(input("Enter the height of the triangle: "))

        # Calculate results
        square_result = calculate_square_area(square_side)
        circle_result = calculate_circle_area(circle_radius)
        triangle_result = calculate_triangle_area(triangle_base, triangle_height)

        # Print results
        print(f"\n--- Geometry Calculator Results ---")

        # Format square result
        if isinstance(square_result, (int, float)):
            print(f"Area of a square with side {square_side}: {square_result:.2f}")
        else:
            print(f"Area of a square with side {square_side}: {square_result}")

        # Format circle result
        if isinstance(circle_result, (int, float)):
            print(f"Area of a circle with radius {circle_radius}: {circle_result:.2f}")
        else:
            print(f"Area of a circle with radius {circle_radius}: {circle_result}")

        # Format triangle result
        if isinstance(triangle_result, (int, float)):
            print(f"Area of a triangle with base {triangle_base} and height {triangle_height}: {triangle_result:.2f}")
        else:
            print(f"Area of a triangle with base {triangle_base} and height {triangle_height}: {triangle_result}")

    except ValueError:
        print("Error: Invalid input. Please enter numeric values.")

    input("\nPress Enter to exit...")

# Main execution block
if __name__ == "__main__":
    run_calculator_app()