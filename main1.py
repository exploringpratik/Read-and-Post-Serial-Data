import serial
import requests
import time

millis = int(round(time.time() * 1000))
x = int(millis)

localMilli = 20700000 + x

heartBeat = 0
bodyTempr = 0
geoLocation = []
surrTempr = 0
dataSample = "iCAT001t25s20h50p50g2740.746848,N,0851554059,E"

jsonUpdateAnimal = {
    "heart_beat": heartBeat,
    "body_tempr": bodyTempr,
    "surr_tempr": surrTempr,
    "geo_location": geoLocation,
    "timestramp": localMilli
}

jsonPostHeartBeat = {
    "timestramp": localMilli,
    "heart_beat": heartBeat
}

jsonPostBodyTempr = {
    "timestramp": localMilli,
    "body_tempr": bodyTempr
}

jsonPostSurrTempr = {
    "timestramp": localMilli,
    "surr_tempr": surrTempr
}

jsonPostGeoLocation = {
    "timestramp": localMilli,
    "geo_location": geoLocation
}


def readSerialData():
    ser = serial.Serial('COM8', 9600)
    while 1:
        alldata = ser.read(1)


def updateAnimal(jsonFromFunction):
    url = "https://animalmonitoringsystem.herokuapp.com/api/updateanimal/5d29fe2e79ed0d22e0d25ac3"

    r = requests.put(url, json=jsonFromFunction)
    print(r.status_code, r.reason)


def postHeartBeat(jsonFromFunction):
    url = "https://animalmonitoringsystem.herokuapp.com/api/postheartbeat/5d29fe2e79ed0d22e0d25ac3"

    r = requests.post(url, json=jsonFromFunction)
    print(r.status_code, r.reason)


def postbodytempr(jsonFromFunction):
    url = "https://animalmonitoringsystem.herokuapp.com/api/postbodytempr/5d29fe2e79ed0d22e0d25ac3"

    r = requests.post(url, json=jsonFromFunction)
    print(r.status_code, r.reason)


def postsurrtempr(jsonFromFunction):
    url = "https://animalmonitoringsystem.herokuapp.com/api/postsurrtempr/5d29fe2e79ed0d22e0d25ac3"

    r = requests.post(url, json=jsonFromFunction)
    print(r.status_code, r.reason)


def postgeolocation(jsonFromFunction):
    url = "https://animalmonitoringsystem.herokuapp.com/api/postgeolocation/5d29fe2e79ed0d22e0d25ac3"

    r = requests.post(url, json=jsonFromFunction)
    print(r.status_code, r.reason)


updateAnimal(jsonUpdateAnimal)
postbodytempr(jsonPostBodyTempr)
postgeolocation(jsonPostGeoLocation)
postHeartBeat(jsonPostHeartBeat)
postsurrtempr(jsonPostSurrTempr)
