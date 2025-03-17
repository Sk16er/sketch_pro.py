import cv2
import turtle
import numpy as np
import time
import os
from plyer import notification  # ✅ System notification

# --------- Helper: Find Next Available Number ---------
def get_next_file_number(base_name, extension):
    max_number = 0
    for filename in os.listdir():
        if filename.startswith(base_name) and filename.endswith(f".{extension}"):
            num_part = filename[len(base_name):-len(f".{extension}")]
            if num_part.isdigit():
                num = int(num_part)
                if num > max_number:
                    max_number = num
    return max_number + 1  # Next available number

# --------- Capture Image from Camera ---------
def capture_image(cap, image_number):
    filename = f"captured_image{image_number}.jpg"
    ret, frame = cap.read()
    cv2.imwrite(filename, frame)
    return filename

# --------- Convert Image to Sketch ---------
def convert_to_sketch(input_file, sketch_number):
    output_file = f"sketch_image{sketch_number}.jpg"
    img = cv2.imread(input_file)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    inv = 255 - gray
    blur = cv2.GaussianBlur(inv, (21, 21), 0)
    sketch = cv2.divide(gray, 255 - blur, scale=256)
    cv2.imwrite(output_file, sketch)
    return sketch, output_file

# --------- Turtle Drawing from Sketch ---------
def turtle_draw(sketch_image):
    # Resize image for turtle drawing
    resized = cv2.resize(sketch_image, (100, 100))  # Smaller for quicker drawing
    height, width = resized.shape

    # Set up turtle window
    screen = turtle.Screen()
    screen.bgcolor("white")
    t = turtle.Turtle()
    t.speed(0)
    t.color("black")
    t.width(1)
    t.hideturtle()

    # Move to start position
    t.penup()
    start_x = -width // 2
    start_y = height // 2
    t.setpos(start_x, start_y)

    # Draw based on pixels
    threshold = 100
    for y in range(height):
        for x in range(width):
            pixel = resized[y, x]
            if pixel < threshold:
                t.goto(start_x + x, start_y - y)
                t.pendown()
                t.dot(2)
                t.penup()

    print("✅ Drawing complete.")
    time.sleep(3)
    screen.bye()  # Close turtle window

# --------- System Notification ---------
def send_notification(title, message):
    notification.notify(
        title=title,
        message=message,
        timeout=5
    )

# --------- Main Program ---------
if __name__ == "__main__":
    print("📸 Starting continuous capture & draw mode...")
    cap = cv2.VideoCapture(0)
    print("➡️  Press SPACE to capture, sketch & draw.")
    print("➡️  Press ESC to exit.")

    # 🔑 Find where to start numbering
    image_counter = get_next_file_number("captured_image", "jpg")
    sketch_counter = get_next_file_number("sketch_image", "jpg")

    while True:
        ret, frame = cap.read()
        cv2.imshow('Camera Feed - Press SPACE to Capture & Draw, ESC to Exit', frame)

        key = cv2.waitKey(1)
        if key % 256 == 27:  # ESC
            print("🚪 Exit requested. Closing program...")
            break
        elif key % 256 == 32:  # SPACE
            # Capture and Sketch
            captured_file = capture_image(cap, image_counter)
            sketch_data, sketch_file = convert_to_sketch(captured_file, sketch_counter)

            # Send Notifications
            send_notification("📸 Image Captured", f"Saved at: {os.path.abspath(captured_file)}")
            send_notification("🎨 Sketch Created", f"Saved at: {os.path.abspath(sketch_file)}")

            # Print Paths
            print(f"\n✅ Image captured and saved at: {os.path.abspath(captured_file)}")
            print(f"🎨 Sketch saved at: {os.path.abspath(sketch_file)}\n")

            time.sleep(1)  # Optional pause
            cv2.destroyAllWindows()
            turtle_draw(sketch_data)

            # Increment counters for next capture
            image_counter += 1
            sketch_counter += 1

            # Resume camera feed
            cap = cv2.VideoCapture(0)
            print("\n✅ Ready for next capture! Press SPACE to capture again or ESC to exit.\n")

    cap.release()
    cv2.destroyAllWindows()
