import cv2
from pyzbar.pyzbar import decode

def read_qr_code_from_camera():
    # Open the webcam
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Error: Could not open camera.")
        return

    while True:
        # Capture a single frame
        ret, frame = cap.read()

        if not ret:
            print("Error: Failed to capture frame.")
            break

        # Convert the frame to grayscale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Use the decode function from the pyzbar library to detect QR codes
        qr_codes = decode(gray)

        # Loop through the detected QR codes and print their data
        for qr_code in qr_codes:
            data = qr_code.data.decode('utf-8')
            print(f"QR Code Data: {data}")

            # Draw a rectangle around the QR code
            rect = qr_code.rect
            cv2.rectangle(frame, (rect.left, rect.top), (rect.left + rect.width, rect.top + rect.height), (0, 255, 0), 2)

        # Display the frame with rectangles around the detected QR codes
        cv2.imshow('QR Code Reader', frame)

        # Break the loop when 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the webcam and close all windows
    cap.release()
    cv2.destroyAllWindows()

# Call the function to start reading QR codes from the camera
read_qr_code_from_camera()
