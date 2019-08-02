import re
import math

dataSample = "iCAT001t25s20h50p50g2740.746848,N,08515.54059,E"
# dataSample = "iCAT00001s28h712t282"
animalId = re.search('i(.*)t', dataSample)
animalId = animalId.group(1)

bodyTemperature = re.search('t(.*)s', dataSample)
bodyTemperature = bodyTemperature.group(1)

surroundingTemperature = re.search('s(.*)h', dataSample)
surroundingTemperature = surroundingTemperature.group(1)

humidity = re.search('h(.*)p', dataSample)
humidity = humidity.group(1)

pulseRate = re.search('t(.*)s', dataSample)
pulseRate = pulseRate.group(1)

latitude = re.search('g(.*),N,', dataSample)
latitudeFloat = float(latitude.group(1)) / 100
afterDecimal, beforeDecimal = math.modf(latitudeFloat)
latitude = beforeDecimal + afterDecimal * 100 / 60

longitude = re.search(',N,(.*),E', dataSample)
longitudeFloat = float(longitude.group(1)) / 100
afterDecimal, beforeDecimal = math.modf(longitudeFloat)
longitude = beforeDecimal + afterDecimal * 100 / 60

print("Data from Microcontroller: ", dataSample)
print("---------------------------------------Output-------------------------------------------------")
print("animal id = ", animalId)
print("body temperature = ", bodyTemperature)
print("surroundingTemperature = ", surroundingTemperature)
print("humidity = ", humidity)
print("pulseRate= ", pulseRate)
print("latitude=  ", latitude)
print("longitude= ", longitude)
