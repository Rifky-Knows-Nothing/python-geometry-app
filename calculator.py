# --- Simple Geometry Calculator ---

def calculate_square_area(side):
    """Calculates the area of a square given its side length."""
    if side < 0:
        # Simple error handling
        return "Error: Side length cannot be negative."
    return side * side

def calculate_circle_area(radius):
    """Calculates the area of a circle given its radius."""
    # We will use a simple pi approximation for this example
    PI = 3.14159
    if radius < 0:
        return "Error: Radius cannot be negative."
    return PI * radius * radius

def calculate_triangle_area(base, height):
    """Calculates the area of a triangle given its base and height."""
    if base < 0 or height < 0:
        return "Error: Base and height cannot be negative."
    return 0.5 * base * height

# Main execution block
if __name__ == "__main__":
    
    # Test cases
    square_side = 5
    circle_radius = 10
    triangle_base = 6
    triangle_height = 4
    
    # Calculate and print results
    square_result = calculate_square_area(square_side)
    circle_result = calculate_circle_area(circle_radius)
    triangle_result = calculate_triangle_area(triangle_base, triangle_height)
    
    print(f"--- Geometry Calculator Results ---")
    print(f"Area of a square with side {square_side}: {square_result}")
    print(f"Area of a circle with radius {circle_radius}: {circle_result:.2f}") # Format to 2 decimal places
    print(f"Area of a triangle with base {triangle_base} and height {triangle_height}: {triangle_result}")
    
    # Example of error case
    error_result = calculate_square_area(-1)
    print(f"Test case with negative input: {error_result}")