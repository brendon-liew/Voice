# -*- coding: utf-8 -*-
"""
Created on Sun May  9 19:45:23 2021

@author: Brendon
"""


#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  camera_pi.py
#
#
#
import time
import io
import threading
import picamera


class Camera(object):
    thread = None  # background thread that reads frames from camera
    frame = None  # current frame is stored here by background thread
    last_access = 0  # time of last client access to the camera

    def initialize(self):
        if Camera.thread is None:
            # start background frame thread
            Camera.thread = threading.Thread(target=self._thread)
            Camera.thread.start()

            # wait until frames start to be available
            while self.frame is None:
                time.sleep(0)

    def get_frame(self):
        Camera.last_access = time.time()
        self.initialize()
        return self.frame

    @classmethod
    def _thread(cls):
        with picamera.PiCamera() as camera:
            # camera setup
            camera.resolution = (800, 600)
            camera.framerate = 15               # 15 frames/sec



            camera.hflip = False
            camera.vflip = False

            # let camera warm up
            camera.start_preview()

