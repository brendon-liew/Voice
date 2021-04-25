#import speech_recognition as sr

#r = sr.Recognizer()
#with sr.Microphone() as source:
#    print("Speak Anything :")
 #   audio = r.listen(source)
  #  try:
      #  text = r.recognize_google(audio)
   #     print("You said : {}".format(text))
  #  except:
    #    print("Sorry could not recognize what you said")
  #     
import time       
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QCoreApplication
import speech_recognition as sr
from mycroft_bus_client import MessageBusClient, Message
import threading
#from Command import COMMAND as cmd
from Motor import * 

client = MessageBusClient()
PWM=Motor()

class VoiceWorker(QtCore.QObject):
    textChanged = QtCore.pyqtSignal(str)

    @QtCore.pyqtSlot()
    def task(self):
       # r = sr.Recognizer()
       # m = sr.Microphone()
        r = client.on('recognizer_loop:utterance',sr.Recognizer())
        m = client.on('mycroft.mic.listen',sr.Microphone())
        
        while True:
            print("Say something!")
            with m as source:
                audio = r.listen(source)
                print("Got it! Now to recognize it...")
                try:
                    value = r.recognize_google(audio)
                    self.textChanged.emit(value)
                    print("You said: {}".format(value))
                    if(value=="Foward"):
                        PWM.setMotorModel(1000,1000,1000,1000)       #Forward
                        print ("The car is moving forward")
                        time.sleep(1)
                    elif(value=="Back"):
                        PWM.setMotorModel(-1000,-1000,-1000,-1000)   #Back
                        print ("The car is going backwards")
                        time.sleep(1)
                    elif(value=="Left"):
                        PWM.setMotorModel(-1500,-1500,2000,2000)       #Left 
                        print ("The car is turning left")
                        time.sleep(1)
                    elif(value=="Right"):
                        PWM.setMotorModel(2000,2000,-1500,-1500)       #Right 
                        print ("The car is turning right")  
                        time.sleep(1)
                    elif(value=="Stop"): 
                        PWM.setMotorModel(0,0,0,0)                   #Stop
                        print ("\nEnd of program")
                        
                    client.run_forever()      
                except sr.UnknownValueError:
                  print("Oops")
         

    
    
    
    
    
    
    
def Gui():
    app = QtWidgets.QApplication(sys.argv)

    worker = VoiceWorker()
    thread = QtCore.QThread()
    thread.start()
    worker.moveToThread(thread)

    window = QtWidgets.QWidget()
    window.setGeometry(200, 200, 350, 400)
    window.setWindowTitle("Voice Engine") 

    title_label = QtWidgets.QLabel(window)
    title_label.setText("Assistant")
    title_label.move(135,10)
    title_label.setFont(QtGui.QFont("SansSerif", 15))

    programs_says = QtWidgets.QLabel(window)
    programs_says.setText("Programs Says")
    programs_says.move(240,100)

    you_says = QtWidgets.QLabel(window)
    you_says.move(25,100)


    you_text = QtWidgets.QLabel(window)
    worker.textChanged.connect(you_text.setText)
    you_text.move(25,150) 


    start_button = QtWidgets.QPushButton("Start")
    close_button = QtWidgets.QPushButton("Close")


    v_box = QtWidgets.QVBoxLayout()
    v_box.addStretch()
    v_box.addWidget(start_button)
    v_box.addWidget(close_button)
    window.setLayout(v_box)

    start_button.clicked.connect(worker.task)
    close_button.clicked.connect(QCoreApplication.instance().quit)
    window.show()
    sys.exit(app.exec())






    
          
# def test_Motor(): 
#     try:
#         PWM.setMotorModel(1000,1000,1000,1000)       #Forward
#         print ("The car is moving forward")
#         time.sleep(1)
#         PWM.setMotorModel(-1000,-1000,-1000,-1000)   #Back
#         print ("The car is going backwards")
#         time.sleep(1)
#         PWM.setMotorModel(-1500,-1500,2000,2000)       #Left 
#         print ("The car is turning left")
#         time.sleep(1)
#         PWM.setMotorModel(2000,2000,-1500,-1500)       #Right 
#         print ("The car is turning right")  
#         time.sleep(1)
#         PWM.setMotorModel(0,0,0,0)                   #Stop
#         print ("\nEnd of program")
#     except KeyboardInterrupt:
#         PWM.setMotorModel(0,0,0,0)
#         print ("\nEnd of program")
        
        
        
   # def on_btn_ForWard(self):
    #    ForWard=self.intervalChar+str(1500)+self.intervalChar+str(1500)+self.intervalChar+str(1500)+self.intervalChar+str(1500)+self.endChar
    #    self.TCP.sendData(cmd.CMD_MOTOR+ForWard)

   # def on_btn_Turn_Left(self):
    #    Turn_Left=self.intervalChar+str(-1500)+self.intervalChar+str(-1500)+self.intervalChar+str(1500)+self.intervalChar+str(1500)+self.endChar
    #    self.TCP.sendData(cmd.CMD_MOTOR+ Turn_Left)
        
  #  def on_btn_BackWard(self):
     #   BackWard=self.intervalChar+str(-1500)+self.intervalChar+str(-1500)+self.intervalChar+str(-1500)+self.intervalChar+str(-1500)+self.endChar
    #    self.TCP.sendData(cmd.CMD_MOTOR+BackWard)

   # def on_btn_Turn_Right(self):
      #  Turn_Right=self.intervalChar+str(1500)+self.intervalChar+str(1500)+self.intervalChar+str(-1500)+self.intervalChar+str(-1500)+self.endChar
     #   self.TCP.sendData(cmd.CMD_MOTOR+Turn_Right)

    #def on_btn_Stop(self):
      #  Stop=self.intervalChar+str(0)+self.intervalChar+str(0)+self.intervalChar+str(0)+self.intervalChar+str(0)+self.endChar
       # self.TCP.sendData(cmd.CMD_MOTOR+Stop)       
        
        
        
        
Gui()
