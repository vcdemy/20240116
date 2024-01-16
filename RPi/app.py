from flask import Flask, send_file
from picamera2 import Picamera2

app = Flask(__name__)

camera = Picamera2()

@app.route('/')
def index():
    return "Hello Raspberry Pi!"

@app.route('/snapshot')
def get_image():
    camera.start()
    filename = '/home/pi/code/static/captured.jpg'
    camera.capture_file(filename)
    camera.stop()
    return send_file(filename, mimetype='image/jpeg')

if __name__=="__main__":
    app.run(host='0.0.0.0')