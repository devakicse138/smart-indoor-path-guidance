import random


# Safety distance in meters
SAFETY_DISTANCE = 1.5


def get_demo_distance():
    """
    Generate a demo distance for testing
    without an ultrasonic sensor.
    """
    distance = round(random.uniform(0.5, 4.0), 2)
    return distance


def check_distance(distance):
    """
    Check whether an obstacle is near.
    """

    if distance <= SAFETY_DISTANCE:
        return "DANGER"

    elif distance <= 3.0:
        return "CAUTION"

    else:
        return "SAFE"


def get_distance_status():
    """
    Get demo distance and its safety status.
    """

    distance = get_demo_distance()
    status = check_distance(distance)

    return distance, status


if __name__ == "__main__":

    print("Distance Measurement Module")
    print("---------------------------")

    for i in range(5):

        distance, status = get_distance_status()

        print(
            f"Obstacle Distance: {distance} meters | "
            f"Status: {status}"
        )
