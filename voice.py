
from flask import Flask, render_template, Response,request,redirect
import io
import socket
from threading import Thread
import sys
import time
from Motor import *
import cv2
import os
from camera import Camera


app = Flask(__name__)

PWM = Motor()


@app.route("/")
def index():
    """Video streaming home page."""

    return render_template('index.html')


def gen(camera):
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/video_feed')
def video_feed():
    """Video streaming route. Put this in the src attribute of an img tag."""
    return Response(gen(Camera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')




@app.route("/forward")
def forward():
        PWM.setMotorModel(1500,1500,1500,1500)
        time.sleep(3)
        PWM.setMotorModel(0,0,0,0)
        return redirect("/")
 
 
@app.route("/backwards") 
@app.route("/backward")
def backward():
        PWM.setMotorModel(-1500,-1500,-1500,-1500)
        time.sleep(3)
        PWM.setMotorModel(0,0,0,0)
        return redirect("/")


@app.route("/left")
def left():
        PWM.setMotorModel(-1500,-1500,1500,1500)
        time.sleep(3)
        PWM.setMotorModel(0,0,0,0)
        return redirect("/")


@app.route("/right")
def right():
        PWM.setMotorModel(1500,1500,-1500,-1500)
        time.sleep(3)
        PWM.setMotorModel(0,0,0,0)
        return redirect("/")


@app.route("/stop")
def stop():
        PWM.setMotorModel(0,0,0,0)
        return redirect("/")


if __name__ == '__main__':

    app.run(host='0.0.0.0',debug=True)
 
