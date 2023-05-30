# Take your hand off
[English](README.md) | [Türkçe](README_TR.md)

This project is aimed at helping individuals break the habit of pulling their beard or touching their face, which can lead to headaches. The project utilizes computer vision techniques to detect hand movements near the face and trigger a notification sound as a reminder.

## Features

- Uses Python 3 and OpenCV for camera access and hand detection
- Utilizes the MediaPipe library for hand landmark detection
- Plays a notification sound when a specific hand movement is detected
- Runs in the background, allowing the program to be used while performing other tasks

## Requirements

- Python 3.x
- OpenCV
- MediaPipe
- playsound

## Installation

1. Clone the repository:

git clone https://github.com/rifatdinc/Take-your-hand-off.git

2. Install the required packages:

pip install -r requirements.txt

## Usage

1. Run the program:

python3 main.py

2. The camera will start in the background, and hand movements will be continuously monitored.
3. If a specific hand movement, such as pulling the beard, is detected, a notification sound will be played.

## Contributing

Contributions are welcome! If you have any suggestions or improvements, please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
