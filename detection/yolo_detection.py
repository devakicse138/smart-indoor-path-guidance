import cv2
from ultralytics import YOLO


def start_detection():

    # Load YOLOv8n model
    model = YOLO("yolov8n.pt")

    # Open laptop camera
    camera = cv2.VideoCapture(0)

    if not camera.isOpened():
        print("Error: Camera could not be opened.")
        return

    print("YOLOv8n object detection started.")
    print("Press Q to quit.")

    while True:

        # Capture frame
        ret, frame = camera.read()

        if not ret:
            print("Error: Could not read camera frame.")
            break

        # Detect objects
        results = model(frame, verbose=False)

        # Draw detection results
        annotated_frame = results[0].plot()

        # Display result
        cv2.imshow(
            "Smart Indoor Navigation - YOLOv8n",
            annotated_frame
        )

        # Press Q to exit
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    # Release resources
    camera.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    start_detection()
