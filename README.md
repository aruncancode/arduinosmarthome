# arduinosmarthome
Cheap smarthome setup via esp8266, python flask and thingspeak. 

- in progress, not completed(expected ~2020)




HOW TO USE IMPORTANT!!! - read in full!

1. go to arduino's website and install the latest arduino IDE. 
2. watch this video # to setup the esp lib 
3. plug in the esp8266 and upload simple blink code, to make sure it's working.
4. locate the aRest.ino file, and add it to arduino IDE as a lib. - watch this vid to help
5. upload the aRest api to your esp8266 dev board and connect it to your home network
6. identify the esp's ip address via the serial monitor and create an esp instance in the mainserver.py code. Alternatively, you can login to your modem's wifi devices page, and find the esp's ip, and continue.
7. create a list of components and status for those components.
8. run the server and access it via localhost:1000.

