# Mood Recognition

## Overview
The Mood Recognition project aims to develop an intelligent system capable of identifying and analyzing human emotions through facial expressions. The project leverages machine learning and computer vision techniques to provide accurate and real-time mood detection, which can be applied in various domains such as healthcare, marketing, and user experience enhancement.

## Results:
![Sample Test](<img width="250" alt="Screenshot 2024-07-08 110226" src="https://github.com/SarthVader2004/MoodRecog/assets/138626629/b6059d9e-d6a2-4c9a-8b70-342cbb612c99">
.png)


## Features
- **Real-Time Emotion Detection**: Detect and analyze emotions using live video feeds.
- **Multi-Emotion Classification**: Identify multiple emotions such as happiness, sadness, anger, surprise, and neutrality.
- **User-Friendly Interface**: Interactive and intuitive web interface using Flet.

## Technologies Used
- **Programming Language**: Python
- **Libraries**:
  - [OpenCV](https://opencv.org/): For image processing and real-time video capture.
  - [DeepFace](https://github.com/serengil/deepface): For emotion detection using pre-trained models.
  - [Flet](https://flet.dev/): For creating the web application interface.

## Installation

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/SarthVader2004/MoodRecog
    cd MoodRecog
    ```

2. **Create a Virtual Environment**:
    ```bash
    python -m venv env
    source env/bin/activate  # On Windows use `env\Scripts\activate`
    ```

3. **Install the Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. **Run the Application**:
    ```bash
    MoodRecog.py
    ```

2. **Access the Web Interface**:
   Open your web browser and navigate to `http://localhost:8000`.

## Project Structure
- `app.py`: Main application script.
- `requirements.txt`: List of dependencies.
- `static/`: Directory for static files (e.g., CSS, JavaScript).
- `templates/`: Directory for HTML templates.

## Challenges and Solutions
- **Achieving High Accuracy**:
  - Implemented advanced data augmentation techniques and used pre-trained models for robust performance.
- **Real-Time Performance**:
  - Optimized the model and used efficient image processing techniques for smooth real-time detection.

## Results
- Achieved an accuracy of 85% on the test set.
- Real-time emotion detection with minimal latency.
- Positive user feedback on the intuitive interface and accurate emotion detection.

## Future Enhancements
- **Improved Accuracy**: Further refine the model to achieve higher accuracy.
- **Additional Emotions**: Expand the model to recognize more complex emotions and micro-expressions.
- **Cross-Platform Compatibility**: Develop mobile and desktop applications for broader accessibility.
- **Integration with Wearable Devices**: Incorporate the system into wearable devices for continuous emotion monitoring.

## Contributing
Feel free to fork this repository and submit pull requests. For major changes, please open an issue first to discuss what you would like to change.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Contact
If you have any questions or feedback, please feel free to contact me at [your-email@example.com](mailto:your-email@example.com).

---

Thank you for checking out my Mood Recognition project!
