import time
import datetime
import pyautogui
import cv2
import numpy as np
import os
from tkinter import Tk
from tkinter.filedialog import askopenfilename

def find_image_on_screen(screenshot, template):
    # Convert images to grayscale
    screenshot_gray = cv2.cvtColor(screenshot, cv2.COLOR_BGR2GRAY)
    template_gray = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)

    # Perform template matching
    result = cv2.matchTemplate(screenshot_gray, template_gray, cv2.TM_CCOEFF_NORMED)

    # Define threshold and locate matches
    threshold = 0.99
    locations = np.where(result >= threshold)
    matches = list(zip(*locations[::-1]))

    return matches

def select_image():
    root = Tk()
    root.withdraw()  # Hide the main window

    # Display file selection dialog
    file_path = askopenfilename(title="Select sub-image file", filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])

    return file_path

def main():
    # Select sub-image
    print("Please select the sub-image.")
    template_path = select_image()

    if not template_path:
        print("No sub-image selected. Exiting.")
        return

    # Load template image
    template = cv2.imread(template_path)

    while True:
        # Take screenshot of the screen
        screenshot = np.array(pyautogui.screenshot())

        # Find matches in the screenshot
        matches = find_image_on_screen(screenshot, template)

        if matches:
            # Create a copy of the screenshot to draw rectangles on
            output_img = screenshot.copy()

            for match in matches:
                # Extract the width and height of the template image
                w, h = template.shape[1::-1]
                
                # Calculate the coordinates of the lower right-hand corner
                lower_right = (match[0] + w, match[1] + h)
                
                # Draw a green rectangle
                cv2.rectangle(output_img, match, lower_right, (0, 255, 0), 2)

            # Get current timestamp
            current_time = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

            # Save the resulting image to the Downloads folder with a unique filename
            output_filename = f"sub_image_detected_{current_time}.png"
            output_path = os.path.join(os.path.expanduser("~"), "Downloads", output_filename)
            cv2.imwrite(output_path, output_img)

            print(f"Found the llama on your screen: saved to {output_path}")

        # Wait for 10 seconds before taking the next screenshot
        time.sleep(5)

if __name__ == "__main__":
    main()
