# main.py

from navigation.source_destination import select_source_destination
from navigation.path_planner import find_path
from navigation.decision import navigation_decision
from distance.distance import get_demo_distance
from ble.ble_location import get_current_location
from voice.voice_output import speak, welcome_message


def show_route(path):
    """Display the calculated route."""

    print("\n==============================")
    print("       NAVIGATION ROUTE")
    print("==============================")

    for i, location in enumerate(path):

        if i == 0:
            print(f"START       : {location}")

        elif i == len(path) - 1:
            print(f"DESTINATION : {location}")

        else:
            print(f"              ↓")
            print(f"              {location}")


def run_navigation():

    # --------------------------------
    # 1. Start system
    # --------------------------------

    print("==========================================")
    print(" SMART INDOOR PATH GUIDANCE SYSTEM")
    print("==========================================")

    welcome_message()

    # --------------------------------
    # 2. Get current location from BLE
    # --------------------------------

    current_location, beacon, rssi_values = get_current_location()

    print("\nBLE INFORMATION")
    print("----------------")
    print("Current Location :", current_location)
    print("Detected Beacon  :", beacon)

    # --------------------------------
    # 3. Select source and destination
    # --------------------------------

    source, destination = select_source_destination()

    print("\nSOURCE      :", source)
    print("DESTINATION :", destination)

    # --------------------------------
    # 4. Find route
    # --------------------------------

    path = find_path(source, destination)

    if path is None:

        print("\nNo route found.")

        speak(
            "Sorry. No route was found "
            "to the selected destination."
        )

        return

    # --------------------------------
    # 5. Display route
    # --------------------------------

    show_route(path)

    speak(
        f"Route found from {source} "
        f"to {destination}."
    )

    # --------------------------------
    # 6. Navigation simulation
    # --------------------------------

    print("\n==============================")
    print("      NAVIGATION STARTED")
    print("==============================")

    for i in range(len(path) - 1):

        current = path[i]
        next_location = path[i + 1]

        print(
            f"\nCurrent Location : {current}"
        )

        print(
            f"Next Location    : {next_location}"
        )

        # --------------------------------
        # 7. Get simulated obstacle distance
        # --------------------------------

        distance = get_demo_distance()

        print(
            f"Obstacle Distance: {distance} meters"
        )

        # --------------------------------
        # 8. Demo obstacle information
        # --------------------------------

        # For now, we simulate an object
        # detected by YOLO.

        object_name = "Chair"

        # Simulate object position
        # 320 = center of 640px camera frame

        x_center = 320

        frame_width = 640

        # --------------------------------
        # 9. Make navigation decision
        # --------------------------------

        side, instruction = navigation_decision(
            object_name,
            x_center,
            frame_width,
            distance
        )

        print("Object          :", object_name)
        print("Object Position :", side)
        print("Instruction     :", instruction)

        # --------------------------------
        # 10. Give voice instruction
        # --------------------------------

        speak(instruction)

        # --------------------------------
        # 11. Move to next location
        # --------------------------------

        print(
            f"Moving from {current} "
            f"to {next_location}..."
        )

    # --------------------------------
    # 12. Destination reached
    # --------------------------------

    print("\n==============================")
    print("     DESTINATION REACHED")
    print("==============================")

    print(
        f"You have reached: {destination}"
    )

    speak(
        f"Destination reached. "
        f"You are at {destination}."
    )


if __name__ == "__main__":
    run_navigation()
