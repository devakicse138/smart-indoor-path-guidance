# ble/ble_location.py

import random


# Simulated BLE beacons installed inside the building
BLE_BEACONS = {
    "BEACON_01": "Entrance",
    "BEACON_02": "Reception",
    "BEACON_03": "Main Corridor",
    "BEACON_04": "Classroom 1",
    "BEACON_05": "Classroom 2",
    "BEACON_06": "Laboratory",
    "BEACON_07": "Lab 2",
    "BEACON_08": "Staircase",
    "BEACON_09": "First Floor",
    "BEACON_10": "Classroom 3"
}


def simulate_rssi():
    """
    Generate simulated RSSI values for testing.

    Stronger RSSI means the beacon is closer.
    """

    rssi_values = {}

    for beacon_id in BLE_BEACONS:

        # Simulate RSSI between -90 and -40 dBm
        rssi_values[beacon_id] = random.randint(-90, -40)

    return rssi_values


def find_nearest_beacon(rssi_values):
    """
    Find the beacon with the strongest RSSI.

    Example:
    -45 dBm is stronger than -75 dBm.
    """

    if not rssi_values:
        return None

    nearest_beacon = max(
        rssi_values,
        key=rssi_values.get
    )

    return nearest_beacon


def get_current_location():
    """
    Estimate current indoor location using
    the strongest BLE beacon.
    """

    rssi_values = simulate_rssi()

    nearest_beacon = find_nearest_beacon(rssi_values)

    if nearest_beacon is None:
        return None, None, rssi_values

    location = BLE_BEACONS[nearest_beacon]

    return location, nearest_beacon, rssi_values


def display_ble_information():
    """
    Display simulated BLE information.
    """

    location, beacon, rssi_values = get_current_location()

    print("\nBLE RSSI Values")
    print("----------------")

    for beacon_id, rssi in rssi_values.items():

        location_name = BLE_BEACONS[beacon_id]

        print(
            f"{beacon_id} "
            f"({location_name}) : "
            f"{rssi} dBm"
        )

    print("\nStrongest Beacon :", beacon)

    print("Current Location :", location)


if __name__ == "__main__":

    print("================================")
    print(" BLE Indoor Positioning Module")
    print("================================")

    display_ble_information()
