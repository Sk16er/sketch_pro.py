import cv2
import turtle
import numpy as np
import time
import os
from plyer import notification  # ✅ Import plyer for system notifications

# --------- Helper: Generate Unique Filename ---------
def get_unique_filename(base_name, extension):
    counter = 1
    while os.path.exists(f"{base_name}{counter}.{extension}"):
        counter += 1
    return f"{base_name}{counter}.{extension}"

# --------- Step 1: Capture Image from Camera ---------
def capture_image(cap):
    filename = get_unique_filename("captured_image", "jpg")
    ret, frame = cap.read()
    cv2.imwrite(filename, frame)
    return filename  # Just return path, notify will be handled outside

# --------- Step 2: Convert to Sketch ---------
def convert_to_sketch(input_file):
    output_file = get_unique_filename("sketch_image", "jpg")
    img = cv2.imread(input_file)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    inv = 255 - gray
    blur = cv2.GaussianBlur(inv, (21, 21), 0)
    sketch = cv2.divide(gray, 255 - blur, scale=256)
    cv2.imwrite(output_file, sketch)
    return sketch, output_file  # Return both sketch data and path

# --------- Step 3: Turtle Drawing from Sketch ---------
def turtle_draw(sketch_image):
    # Resize image for turtle drawing
    resized = cv2.resize(sketch_image, (100, 100))  # Adjust size for faster drawing
    height, width = resized.shape

    # Set up turtle window
    screen = turtle.Screen()
    screen.bgcolor("white")
    t = turtle.Turtle()
    t.speed(0)
    t.color("black")
    t.width(1)
    t.hideturtle()

    # Position turtle to top-left
    t.penup()
    start_x = -width // 2
    start_y = height // 2
    t.setpos(start_x, start_y)

    # Draw based on pixel brightness
    threshold = 100  # Control drawing detail
    for y in range(height):
        for x in range(width):
            pixel = resized[y, x]
            if pixel < threshold:
                t.goto(start_x + x, start_y - y)
                t.pendown()
                t.dot(2)
                t.penup()

    print("✅ Drawing complete.")
    # Keep window open for 3 seconds then close
    time.sleep(3)
    screen.bye()  # Properly close turtle window

# --------- Step 4: Send Notification ---------
def send_notification(title, message):
    notification.notify(
        title=title,
        message=message,
        timeout=5  # seconds the notification stays
    )

# --------- Main Program ---------
if __name__ == "__main__":
    print("📸 Starting continuous capture & draw mode...")
    cap = cv2.VideoCapture(0)
    print("➡️  Press SPACE to capture, sketch & draw.")
    print("➡️  Press ESC to exit.")

    while True:
        ret, frame = cap.read()
        cv2.imshow('Camera Feed - Press SPACE to Capture & Draw, ESC to Exit', frame)

        key = cv2.waitKey(1)
        if key % 256 == 27:  # ESC pressed
            print("🚪 Exit requested. Closing program...")
            break
        elif key % 256 == 32:  # SPACE pressed
            # Capture and Sketch
            captured_file = capture_image(cap)
            sketch_data, sketch_file = convert_to_sketch(captured_file)

            # ✅ Send system notifications
            send_notification("📸 Image Captured", f"Saved at: {os.path.abspath(captured_file)}")
            send_notification("🎨 Sketch Created", f"Saved at: {os.path.abspath(sketch_file)}")

            # Also print paths in console for reference
            print(f"\n✅ Image captured and saved at: {os.path.abspath(captured_file)}")
            print(f"🎨 Sketch saved at: {os.path.abspath(sketch_file)}\n")

            time.sleep(1)  # Optional pause before drawing
            cv2.destroyAllWindows()  # Close camera feed before drawing
            turtle_draw(sketch_data)  # Start turtle drawing

            # After drawing is done, resume camera feed
            cap = cv2.VideoCapture(0)
            print("\n✅ Ready for next capture! Press SPACE to capture again or ESC to exit.\n")

    cap.release()
    cv2.destroyAllWindows()
