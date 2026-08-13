# navigation/decision.py


# Distance limits in meters
DANGER_DISTANCE = 1.0
CAUTION_DISTANCE = 2.0


def get_object_side(x_center, frame_width):
    """
    Determine whether an object is on the
    left, center, or right side of the camera.
    """

    left_limit = frame_width / 3
    right_limit = (frame_width / 3) * 2

    if x_center < left_limit:
        return "left"

    elif x_center > right_limit:
        return "right"

    else:
        return "center"


def make_navigation_decision(object_name, side, distance):
    """
    Decide what the user should do based on
    object position and distance.
    """

    # Very close obstacle
    if distance <= DANGER_DISTANCE:

        if side == "left":
            return f"Stop! {object_name} is {distance} meters away. Move right."

        elif side == "right":
            return f"Stop! {object_name} is {distance} meters away. Move left."

        else:
            return f"Stop! {object_name} is {distance} meters ahead. Move left or right."

    # Obstacle at medium distance
    elif distance <= CAUTION_DISTANCE:

        if side == "left":
            return f"Caution! {object_name} on the left at {distance} meters. Move right."

        elif side == "right":
            return f"Caution! {object_name} on the right at {distance} meters. Move left."

        else:
            return f"Caution! {object_name} ahead at {distance} meters. Prepare to move around it."

    # Object is far away
    else:
        return f"{object_name} detected at {distance} meters. Continue forward."


def navigation_decision(object_name, x_center, frame_width, distance):
    """
    Complete navigation decision function.

    Input:
        object_name  -> detected object
        x_center     -> center X coordinate of bounding box
        frame_width  -> camera frame width
        distance     -> obstacle distance in meters

    Output:
        Navigation instruction
    """

    side = get_object_side(x_center, frame_width)

    instruction = make_navigation_decision(
        object_name,
        side,
        distance
    )

    return side, instruction


# Test the module
if __name__ == "__main__":

    print("Smart Indoor Navigation Decision Module")
    print("----------------------------------------")

    frame_width = 640

    # Test 1: Object in center
    side, instruction = navigation_decision(
        "Chair",
        320,
        frame_width,
        0.8
    )

    print("\nTest 1")
    print("Object Side:", side)
    print("Instruction:", instruction)

    # Test 2: Object on left
    side, instruction = navigation_decision(
        "Person",
        120,
        frame_width,
        1.2
    )

    print("\nTest 2")
    print("Object Side:", side)
    print("Instruction:", instruction)

    # Test 3: Object on right
    side, instruction = navigation_decision(
        "Table",
        550,
        frame_width,
        1.5
    )

    print("\nTest 3")
    print("Object Side:", side)
    print("Instruction:", instruction)

    # Test 4: Far object
    side, instruction = navigation_decision(
        "Chair",
        320,
        frame_width,
        3.0
    )

    print("\nTest 4")
    print("Object Side:", side)
    print("Instruction:", instruction)
