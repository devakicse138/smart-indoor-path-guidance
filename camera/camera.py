import cv2


def start_camera():
    # Open the default camera
    camera = cv2.VideoCapture(0)

    if not camera.isOpened():
        print("Error: Camera could not be opened.")
        return

    print("Camera started successfully.")
    print("Press Q to quit.")

    while True:
        # Read a frame
        ret, frame = camera.read()

        if not ret:
            print("Error: Could not read frame.")
            break

        # Display the camera frame
        cv2.imshow("Smart Indoor Navigation - Camera", frame)

        # Press Q to exit
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    # Release camera
    camera.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    start_camera()
