# from flask import Flask, render_template, request, redirect, url_for
# import cv2
# import os

# # Initialize the Flask app
# app = Flask(__name__)
# UPLOAD_FOLDER = 'static/uploads'
# app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# # Load pre-trained classifiers
# face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
# eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

# # Function to detect sleep/awake status in video
# def detect_sleep_in_video(video_path):
#     cap = cv2.VideoCapture(video_path)
#     if not cap.isOpened():
#         print("Error: Could not open video file.")
#         return

#     while True:
#         ret, frame = cap.read()
#         if not ret:
#             break

#         # Convert to grayscale and apply histogram equalization
#         gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#         gray = cv2.equalizeHist(gray)

#         faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

#         for (x, y, w, h) in faces:
#             cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
#             roi_gray = gray[y:y + h, x:x + w]
#             roi_color = frame[y:y + h, x:x + w]

#             eyes = eye_cascade.detectMultiScale(roi_gray, scaleFactor=1.1, minNeighbors=5)
#             if len(eyes) == 0:
#                 status = "Sleeping"
#             else:
#                 status = "Engaged"

#             cv2.putText(frame, status, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
#             print(f"Student Status: {status}")

#         cv2.imshow('Student Engagement Detection', frame)

#         if cv2.waitKey(1) & 0xFF == ord('q'):
#             break

#     cap.release()
#     cv2.destroyAllWindows()


# # Function for live video detection
# def detect_sleep_in_live_camera():
#     cap = cv2.VideoCapture(0)  # Open the default camera
#     if not cap.isOpened():
#         print("Error: Could not access the camera.")
#         return

#     while True:
#         ret, frame = cap.read()
#         if not ret:
#             break

#         gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#         faces = face_cascade.detectMultiScale(gray, 1.3, 5)

#         for (x, y, w, h) in faces:
#             cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
#             roi_gray = gray[y:y + h, x:x + w]
#             roi_color = frame[y:y + h, x:x + w]

#             eyes = eye_cascade.detectMultiScale(roi_gray)
#             if len(eyes) == 0:
#                 status = "Sleeping"
#             else:
#                 status = "Engaged"

#             cv2.putText(frame, status, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
#             print(f"Student Status: {status}")

#         cv2.imshow('Live Student Engagement Detection', frame)

#         if cv2.waitKey(1) & 0xFF == ord('q'):
#             break

#     cap.release()
#     cv2.destroyAllWindows()

# # Route for the home page
# @app.route('/')
# def index():
#     return render_template('index.html')

# # Route to handle file upload
# @app.route('/upload', methods=['POST'])
# def upload_file():
#     if 'file' not in request.files:
#         return "No file part"

#     file = request.files['file']
#     if file.filename == '':
#         return "No selected file"

#     if file:
#         file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
#         file.save(file_path)
#         detect_sleep_in_video(file_path)
#         return render_template('index2.html')

# # Route for live video detection
# @app.route('/live')
# def live_detection():
#     detect_sleep_in_live_camera()
#     return redirect(url_for('index'))

# if __name__ == '__main__':
#     if not os.path.exists(UPLOAD_FOLDER):
#         os.makedirs(UPLOAD_FOLDER)
#     app.run(debug=True)

# import cv2
# from flask import Flask, render_template, request, redirect, url_for
# import os

# # Initialize the Flask app
# app = Flask(__name__)
# UPLOAD_FOLDER = 'static/uploads'
# app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# # Load pre-trained classifiers
# face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
# eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

# def detect_sleep_in_video(video_path):
#     cap = cv2.VideoCapture(video_path)
#     if not cap.isOpened():
#         print("Error: Could not open video file.")
#         return

#     while True:
#         ret, frame = cap.read()
#         if not ret:
#             break

#         # Convert to grayscale and apply histogram equalization
#         gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#         gray = cv2.equalizeHist(gray)

#         # Adjust detection parameters for top-down angle
#         faces = face_cascade.detectMultiScale(gray, scaleFactor=1.05, minNeighbors=4, minSize=(30, 30))

#         for (x, y, w, h) in faces:
#             cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
#             roi_gray = gray[y:y + h, x:x + w]
#             roi_color = frame[y:y + h, x:x + w]

#             eyes = eye_cascade.detectMultiScale(roi_gray, scaleFactor=1.05, minNeighbors=5)
#             if len(eyes) == 0:
#                 status = "Sleeping"
#             else:
#                 status = "Engaged"

#             cv2.putText(frame, status, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
#             print(f"Student Status: {status}")

#         cv2.imshow('Student Engagement Detection', frame)

#         if cv2.waitKey(1) & 0xFF == ord('q'):
#             break

#     cap.release()
#     cv2.destroyAllWindows()

# def detect_sleep_in_live_camera():
#     cap = cv2.VideoCapture(0)  # Open the default camera
#     if not cap.isOpened():
#         print("Error: Could not access the camera.")
#         return

#     while True:
#         ret, frame = cap.read()
#         if not ret:
#             break

#         gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#         gray = cv2.equalizeHist(gray)
#         faces = face_cascade.detectMultiScale(gray, scaleFactor=1.05, minNeighbors=4)

#         for (x, y, w, h) in faces:
#             cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
#             roi_gray = gray[y:y + h, x:x + w]
#             roi_color = frame[y:y + h, x:x + w]

#             eyes = eye_cascade.detectMultiScale(roi_gray, scaleFactor=1.05, minNeighbors=5)
#             if len(eyes) == 0:
#                 status = "Sleeping"
#             else:
#                 status = "Engaged"

#             cv2.putText(frame, status, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
#             print(f"Student Status: {status}")

#         cv2.imshow('Live Student Engagement Detection', frame)

#         if cv2.waitKey(1) & 0xFF == ord('q'):
#             break

#     cap.release()
#     cv2.destroyAllWindows()

# # Route for the home page
# @app.route('/')
# def index():
#     return render_template('index.html')

# # Route to handle file upload
# @app.route('/upload', methods=['POST'])
# def upload_file():
#     if 'file' not in request.files:
#         return "No file part"

#     file = request.files['file']
#     if file.filename == '':
#         return "No selected file"

#     if file:
#         file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
#         file.save(file_path)
#         detect_sleep_in_video(file_path)
#         return render_template('index2.html')

# # Route for live video detection
# @app.route('/live')
# def live_detection():
#     detect_sleep_in_live_camera()
#     return redirect(url_for('index'))

# if __name__ == '__main__':
#     if not os.path.exists(UPLOAD_FOLDER):
#         os.makedirs(UPLOAD_FOLDER)
#     app.run(debug=True)


############ original code

# from flask import Flask, render_template, request, redirect, url_for
# import cv2
# import os

# # Initialize the Flask app
# app = Flask(__name__)
# UPLOAD_FOLDER = 'static/uploads'
# app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# # Load pre-trained classifiers
# face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
# eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

# # Function to detect sleep/awake status in video
# def detect_sleep_in_video(video_path):
#     cap = cv2.VideoCapture(video_path)
#     if not cap.isOpened():
#         print("Error: Could not open video file.")
#         return

#     while True:
#         ret, frame = cap.read()
#         if not ret:
#             break

#         gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#         faces = face_cascade.detectMultiScale(gray, 1.3, 5)

#         for (x, y, w, h) in faces:
#             cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
#             roi_gray = gray[y:y + h, x:x + w]
#             roi_color = frame[y:y + h, x:x + w]

#             eyes = eye_cascade.detectMultiScale(roi_gray)
#             if len(eyes) == 0:
#                 status = "Sleeping"
#             else:
#                 status = "Engaged"

#             cv2.putText(frame, status, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
#             print(f"Student Status: {status}")

#         cv2.imshow('Student Engagement Detection', frame)

#         if cv2.waitKey(1) & 0xFF == ord('q'):
#             break

#     cap.release()
#     cv2.destroyAllWindows()

# # Function for live video detection
# def detect_sleep_in_live_camera():
#     cap = cv2.VideoCapture(0)  # Open the default camera
#     if not cap.isOpened():
#         print("Error: Could not access the camera.")
#         return

#     while True:
#         ret, frame = cap.read()
#         if not ret:
#             break

#         gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#         faces = face_cascade.detectMultiScale(gray, 1.3, 5)

#         for (x, y, w, h) in faces:
#             cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
#             roi_gray = gray[y:y + h, x:x + w]
#             roi_color = frame[y:y + h, x:x + w]

#             eyes = eye_cascade.detectMultiScale(roi_gray)
#             if len(eyes) == 0:
#                 status = "Sleeping"
#             else:
#                 status = "Engaged"

#             cv2.putText(frame, status, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
#             print(f"Student Status: {status}")

#         cv2.imshow('Live Student Engagement Detection', frame)

#         if cv2.waitKey(1) & 0xFF == ord('q'):
#             break

#     cap.release()
#     cv2.destroyAllWindows()

# # Route for the home page
# @app.route('/')
# def index():
#     return render_template('index.html')

# # Route to handle file upload
# @app.route('/upload', methods=['POST'])
# def upload_file():
#     if 'file' not in request.files:
#         return "No file part"

#     file = request.files['file']
#     if file.filename == '':
#         return "No selected file"

#     if file:
#         file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
#         file.save(file_path)
#         detect_sleep_in_video(file_path)
#         return render_template('index2.html')

# # Route for live video detection
# @app.route('/live')
# def live_detection():
#     detect_sleep_in_live_camera()
#     return redirect(url_for('index'))

# if __name__ == '__main__':
#     if not os.path.exists(UPLOAD_FOLDER):
#         os.makedirs(UPLOAD_FOLDER)
#     app.run(debug=True)


from flask import Flask, render_template, request, redirect, url_for
import cv2
import os

# Initialize the Flask app
app = Flask(__name__)
UPLOAD_FOLDER = 'static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Load pre-trained classifiers
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

def detect_sleep(frame):
    """
    Detect whether a person is sleeping or engaged in a given frame.
    Returns the updated frame with detection status.
    """
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
        roi_gray = gray[y:y + h, x:x + w]
        roi_color = frame[y:y + h, x:x + w]

        eyes = eye_cascade.detectMultiScale(roi_gray)
        if len(eyes) < 1:  # Assuming no eyes means sleeping
            status = "Sleeping"
        else:
            status = "Engaged"

        cv2.putText(frame, status, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

    return frame

def process_video(video_path):
    """
    Process a video to detect sleep/awake status and display results.
    """
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print("Error: Could not open video file.")
        return

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        processed_frame = detect_sleep(frame)
        cv2.imshow('Student Engagement Detection', processed_frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

def process_live_camera():
    """
    Process live camera feed to detect sleep/awake status.
    """
    cap = cv2.VideoCapture(0)  # Open the default camera
    if not cap.isOpened():
        print("Error: Could not access the camera.")
        return

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        processed_frame = detect_sleep(frame)
        cv2.imshow('Live Student Engagement Detection', processed_frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

# Route for the home page
@app.route('/')
def index():
    return render_template('index.html')

# Route to handle file upload
@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return "No file part"

    file = request.files['file']
    if file.filename == '':
        return "No selected file"

    if file:
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(file_path)
        process_video(file_path)
        return render_template('index2.html')

# Route for live video detection
@app.route('/live')
def live_detection():
    process_live_camera()
    return redirect(url_for('index'))

if __name__ == '__main__':
    if not os.path.exists(UPLOAD_FOLDER):
        os.makedirs(UPLOAD_FOLDER)
    app.run(debug=True)
