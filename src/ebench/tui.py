from .line_volume import line_volume

def main():
    user_input = ''
    while True:
        # User input
        outer_diameter = float(input("Enter the outer diameter of the cylindrical line: "))
        wall_thickness = float(input("Enter the wall thickness of the cylindrical line: "))
        length = float(input("Enter the length of the cylindrical line: "))

        # Calculate the volume
        volume = line_volume(outer_diameter, wall_thickness, length)
        
        # Output to terminal
        print(f"The volume of the cylindrical line is: {volume:.2f}")

        # Prompt user to continue or quit
        user_input = input("Input 'Q' to quit or any other key to continue: ")
        if user_input == 'Q':
            break

if __name__ == "__main__":
    main()