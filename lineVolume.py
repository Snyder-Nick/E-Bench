# User inputs
outer_radius = float(input("Enter the outer diameter of the line (in Inches): "))/2
internal_radius = outer_radius - float(input("Enter the wall thickness of the line (in Inches): "))
length = float(input("Enter the length of the line (in Feet): "))*12

# Calculations
volume = 3.14159 * internal_radius**2 * length

# Output
print(f"The volume of the line is: {volume:.2f} cubic inches.")