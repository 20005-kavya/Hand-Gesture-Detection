from flask import Flask, render_template, Response
import cv2
from hand_tracking import HandTracker
from gesture_controller import GestureController

app = Flask(__name__)

cap = cv2.VideoCapture(0)
tracker = HandTracker()
gesture = GestureController()

def generate_frames():
    while True:
        success, frame = cap.read()
        if not success:
            break

        frame = cv2.flip(frame, 1)

        hands, frame = tracker.find_hands(frame)
        
        if hands:
            gesture.process(hands[0], frame)

        _, buffer = cv2.imencode('.jpg', frame)
        frame = buffer.tobytes()

        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video')
def video():
    return Response(generate_frames(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == "__main__":
    # app.run(host='0.0.0.0', port=7860)
    app.run()