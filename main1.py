import serial
import requests
import time
import re
import math

millis = int(round(time.time() * 1000))
x = int(millis)
animalId = '5d29ff5479ed0d22e0d25ac4'
localMilli = 20700000 + x

dataSample = "iCAT001t25s20h50p50g2740.746848,N,08515.54059,E"


# When there is whitespace or some special character, then send data to server.

# def readSerialData():
#     ser = serial.Serial('COM8', 9600)
#     while 1:
#         dataSample = ser.read(1)
#         print(dataSample)
#         formatDataProperly(dataSample)


def formatDataProperly(dataSample):
    global bodyTempr
    global geoLocation
    global surrTempr
    global heartBeat
    global geoLocation

    animalId = re.search('i(.*)t', dataSample)
    animalId = animalId.group(1)

    bodyTemperature = re.search('t(.*)s', dataSample)
    bodyTemperature = bodyTemperature.group(1)
    bodyTempr = bodyTemperature

    surroundingTemperature = re.search('s(.*)h', dataSample)
    surroundingTemperature = surroundingTemperature.group(1)
    surrTempr = surroundingTemperature

    humidity = re.search('h(.*)p', dataSample)
    humidity = humidity.group(1)

    pulseRate = re.search('t(.*)s', dataSample)
    pulseRate = pulseRate.group(1)
    heartBeat = pulseRate

    latitude = re.search('g(.*),N,', dataSample)
    latitudeFloat = float(latitude.group(1)) / 100
    afterDecimal, beforeDecimal = math.modf(latitudeFloat)
    latitude = beforeDecimal + afterDecimal * 100 / 60

    longitude = re.search(',N,(.*),E', dataSample)
    longitudeFloat = float(longitude.group(1)) / 100
    afterDecimal, beforeDecimal = math.modf(longitudeFloat)
    longitude = beforeDecimal + afterDecimal * 100 / 60
    geoLocation = [latitude, longitude]

    print("Data from Microcontroller: ", dataSample)
    print("---------------------------------------Output-------------------------------------------------")
    print("animal id = ", animalId)
    print("body temperature = ", bodyTemperature)
    print("surroundingTemperature = ", surroundingTemperature)
    print("humidity = ", humidity)
    print("pulseRate= ", pulseRate)
    print("latitude=  ", latitude)
    print("longitude= ", longitude)
    print("Geo-Lccation", geoLocation)


formatDataProperly(dataSample)
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


def updateAnimal(jsonFromFunction):
    url = "https://animalmonitoringsystem.herokuapp.com/api/updateanimal/" + animalId

    r = requests.put(url, json=jsonFromFunction)
    print(r.status_code, r.reason)


def postHeartBeat(jsonFromFunction):
    url = "https://animalmonitoringsystem.herokuapp.com/api/postheartbeat/"+animalId

    r = requests.post(url, json=jsonFromFunction)
    print(r.status_code, r.reason)


def postbodytempr(jsonFromFunction):
    url = "https://animalmonitoringsystem.herokuapp.com/api/postbodytempr/"+animalId

    r = requests.post(url, json=jsonFromFunction)
    print(r.status_code, r.reason)


def postsurrtempr(jsonFromFunction):
    url = "https://animalmonitoringsystem.herokuapp.com/api/postsurrtempr/"+animalId

    r = requests.post(url, json=jsonFromFunction)
    print(r.status_code, r.reason)


def postgeolocation(jsonFromFunction):
    url = "https://animalmonitoringsystem.herokuapp.com/api/postgeolocation/"+animalId

    r = requests.post(url, json=jsonFromFunction)
    print(r.status_code, r.reason)


updateAnimal(jsonUpdateAnimal)
postbodytempr(jsonPostBodyTempr)
postgeolocation(jsonPostGeoLocation)
postHeartBeat(jsonPostHeartBeat)
postsurrtempr(jsonPostSurrTempr)
