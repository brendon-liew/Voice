# Robot Car Control with Live Streaming, Button Control and Voice Control

Download Putty to use ssh
https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html

Install xrdp service which is an open source remote desktop protocol(xdrp) server in RPI.
sudo apt-get install xrdp


Install the requirement1.txt package
sudo pip install -r requirements1.txt

Check python version make sure it is 3.7.3 
python --version

Check device ip address
ifconfig eth0- using ethernet
ifconfig wlan0- using wireless


Check raspberry pi type
gpio readall
If not working use below link 
http://wiringpi.com/wiringpi-updated-to-2-52-for-the-raspberry-pi-4b/


Make sure camera,ssh,vnc,i2c and spi is turn enable
Check i2c module is enabled if yes then it will show 2 value
lsmod | grep i2c

If no go check the RPI configuration or RPI not connect succesfully

Go in Voice folder
It will start the flask server and the port is ip address:5000
python3 main.py

Open browser go to the ip address:5000 and it will show the web page connect to flask server.

To allow microphone access go to the link below and set the website link to the insecure origins place and turn on enable.
chrome://flags/#unsafely-treat-insecure-origin-as-secure 

The website will allow to use voice engine and access your microphone


## Structure of the system
![Process ](https://user-images.githubusercontent.com/60971135/125146791-ad243880-e11f-11eb-81dc-98247421fb13.png)

## Functionality overview
![Design](https://user-images.githubusercontent.com/60971135/125146807-c4fbbc80-e11f-11eb-8c62-626f2ec3e574.PNG)

## Mobile Overview
Iphone
![iphone](https://user-images.githubusercontent.com/60971135/125146797-b6150a00-e11f-11eb-859b-746dfa2fc1e6.jpg)

Xiao Mi
![xiao mi](https://user-images.githubusercontent.com/60971135/125146800-ba412780-e11f-11eb-97c2-6c80e4774090.jpg)
