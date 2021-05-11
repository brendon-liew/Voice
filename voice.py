# -*- coding: utf-8 -*-
"""
Created on Sun May  9 19:48:47 2021

@author: Brendon
"""

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

def init_webhooks(base_url):
     #Update inbound traffic via APIs to use the public-facing ngrok URL
 pass

def start_ngrok():
     #pyngrok will only be installed, and should only ever be initialized, in a dev environment
     from pyngrok import ngrok
     #Initialize our ngrok settings into Flask
     app.config.from_mapping(
         BASE_URL="https://test:5000",
         USE_NGROK=os.environ.get("USE_NGROK", "False") == "True" and os.environ.get("WERKZEUG_RUN_MAIN") != "true"
     )
    # Get the dev server port (defaults to 5000 for Flask, can be overridden with `--port`
    # when starting the server
     port = sys.argv[sys.argv.index("--port") + 1] if "--port" in sys.argv else 5000
     url = ngrok.connect(port).public_url
    # Update any base URLs or webhooks to use the public ngrok URL
     app.config["BASE_URL"] = url
     print(' * Tunnel URL:', url)
     init_webhooks(url)


@app.route("/")
def index():
    """Video streaming home page."""

    return render_template('index.html')

def gen(camera):
 """Video streaming generator function."""
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/video_feed')
def video_feed():
    """Video streaming route. Put this in the src attribute of an img tag."""
    return Response(gen(Camera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')



# endChar='\n'
# intervalChar='#'
@app.route("/forward")
def forward():

        PWM.setMotorModel(1500,1500,1500,1500)
        time.sleep(3)
        PWM.setMotorModel(0,0,0,0)
        return redirect("/")

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

# @app.route("/result",methods=["GET", "POST"])
# def result():
#     if request.method == 'POST':
#       result = request.form
#       return render_template("result.html",result = result)







if __name__ == '__main__':
    app.run(ssl_context=('cert.pem', 'key.pem'))
    #app.run(start_ngrok())
    #app.run(host='0.0.0.0', port=8080, debug=True)
