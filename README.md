# spirit-week-bot

The spirit-week-bot is a Python script that continuously captures screenshots of your primary monitor every 5 seconds, searching for a llama image. When the program detects a llama on your screen, it notifies you, saves the screenshot with a green box drawn around the llama to your downloads folder, and displays the notification. Don't forget to download this image as the target image for the program:

<img width="61" alt="llama" src="https://github.com/PaulvonRedmont/spirit-week-bot/assets/146851640/47c367c5-2c46-4154-90b6-a590cbbd9e24">


## How it Works

1. **Screenshot Capture**: The script takes a screenshot of your primary monitor every 5 seconds.

2. **Llama Detection**: It searches for a llama image in each screenshot using OpenCV template matching.

3. **Notification**: If a llama is found, the program notifies you and saves the screenshot with a green box drawn around the llama to your downloads folder.

## Customization

You can customize the threshold value used by OpenCV to find a match by modifying the `threshold` variable in the script. Adjusting this value can help improve the accuracy of llama detection. For example, you can decrease or increase the threshold to 0.8 or 0.7 as needed.

## Installation

Make sure to install the following libraries:
- pyautogui
- opencv-python (cv2)
- numpy as np

## Usage

1. Clone or download the repository to your local machine.

2. Navigate to the directory containing the script.

3. Run the script using Python:

