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

# Main execution block
if __name__ == "__main__":
    
    # Test cases
    square_side = 5
    circle_radius = 10
    
    # Calculate and print results
    square_result = calculate_square_area(square_side)
    circle_result = calculate_circle_area(circle_radius)
    
    print(f"--- Geometry Calculator Results ---")
    print(f"Area of a square with side {square_side}: {square_result}")
    print(f"Area of a circle with radius {circle_radius}: {circle_result:.2f}") # Format to 2 decimal places
    
    # Example of error case
    error_result = calculate_square_area(-1)
    print(f"Test case with negative input: {error_result}")