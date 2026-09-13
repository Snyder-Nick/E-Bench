import math
def line_volume(outer_diameter, wall_thickness, length):
    """
    Calculate the volume of a cylindrical line. 
    No units are specified, ensure that all input units are consistent (e.g., all in meters or all in inches).
    outer_diameter: The outer diameter of the cylindrical line.
    wall_thickness: The thickness of the wall of the cylindrical line.
    length: The length of the cylindrical line.
    """
    # Input validation
    if length <= 0:
        raise ValueError("Length must be a positive number.")
    if outer_diameter <= 0:
        raise ValueError("Outer diameter must be a positive number.")
    if wall_thickness <= 0:
        raise ValueError("Wall thickness must be a positive number.")
    if wall_thickness >= outer_diameter / 2:
        raise ValueError("Wall thickness must be less than half of the outer diameter.")

    # Calculate the volume of a cylindrical line given its outer diameter, wall thickness, and length.
    volume = math.pi * (outer_diameter/2 - wall_thickness)**2 * length
    return volume