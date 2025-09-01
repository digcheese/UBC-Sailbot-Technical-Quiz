def bound_to_180(angle):
    """Bounds the provided angle between [-180, 180) degrees.

    e.g.)
        bound_to_180(135) = 135.0
        bound_to_180(200) = -160.0

    Args:
        angle (float): The input angle in degrees.

    Returns:
        float: The bounded angle in degrees.
    """
    return (angle + 180) % 360 - 180 


def is_angle_between(first_angle, middle_angle, second_angle):
    """Determines whether an angle is between two other angles.

    e.g.)
        is_angle_between(0, 45, 90) = True
        is_angle_between(45, 90, 270) = False

    Args:
        first_angle (float): The first bounding angle in degrees.
        middle_angle (float): The angle in question in degrees.
        second_angle (float): The second bounding angle in degrees.

    Returns:
        bool: True when `middle_angle` is not in the reflex angle of `first_angle` and `second_angle`, false otherwise.
    """

    # finds the bounded difference between angles
    first_second_difference: float = (first_angle - second_angle + 180) % 360 - 180
    middle_first_difference: float = (first_angle - middle_angle + 180) % 360 - 180
    middle_second_difference: float = (second_angle - middle_angle + 180) % 360 - 180


    # the magnitude of angle between first and second must be greater than the magnitude betwen middle and second and first.
    return abs(first_second_difference) > abs(middle_second_difference) and abs(first_second_difference) > abs(middle_first_difference)
