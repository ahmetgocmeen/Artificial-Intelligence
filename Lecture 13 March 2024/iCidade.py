import math
import random
import libic as lb

def distIC(city1,city2):
    x1, y1 = city1[1], city1[2]
    x2, y2 = city2[1], city2[2]
    return math.sqrt((x2-x1)**2 + (y2-y1)**2)

def distCircularIC(iCities):
    sumDistance = 0
    for i in range(len(iCities)):
        city1 = iCities[i]
        if i < len(iCities) - 1:
            city2 = iCities[i+1]
        else:
            city1 = iCities[0]
        sumDistance += distIC(city1,city2) 
    return sumDistance

def swapIC(iCities,pos1,pos2):
    iCities[pos1], iCities[pos2] = iCities[pos2], iCities[pos1]
    return iCities

def swapBestIC(iCities):
    orgDistance = distCircularIC(iCities)
    pos1, pos2 = random.sample(range(len(iCities)),2)
    newICities = swapIC(iCities[:],pos1,pos2)
    newDistance = distCircularIC(newICities)
    if newDistance <= orgDistance:
        return newICities
    else:
        return iCities

w = lb.windowIC(800)
cityList = lb.readTSP2ListIC("berlin52.tsp")


print(f"\nCircular distance between random iCities: {distCircularIC(cityList)}")
lb.drawIC(cityList,w) 
input("Enter para continuar... ")
