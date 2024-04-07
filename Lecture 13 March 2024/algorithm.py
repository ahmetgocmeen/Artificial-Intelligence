import math
import random
import libic as lb

def distIC(city1,city2):
    x1, y1 = city1[0], city1[1]
    x2, y2 = city2[0], city2[1]
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

def changeIC(iCities,p1,p2):
    newList = iCities.copy()
    newList[p1], newList[p2] = newList[p2],newList[p1]
    return newList

def changeifBetterIC(iCities):
    distance = distCircularIC(iCities)
    p1 = random.randint(0,len(iCities)-1)
    p2 = random.randint(0,len(iCities)-1)
    newList = changeIC(iCities,p1,p2)
    newDistance = distCircularIC(newList)
    if(newDistance <= distance):
        return newList
    return iCities

def betterDistCircularIC(iCities, r):
    newList = iCities
    for i in range (r):
        newList = changeifBetterIC(newList)
    return newList

def optDistCircularIC(iCities, r):
    distance = distCircularIC(iCities)
    opt = betterDistCircularIC(iCities,r)
    finalDistance = distCircularIC(opt)
    return distance,finalDistance,opt 

def swap_cities(iCities, p1, p2):
    """
    Swaps two cities in the tour.
    """
    newTour = iCities[:]
    newTour[p1], newTour[p2] = newTour[p2], newTour[p1]
    return newTour

def hill_climb_tsp(iCities):
    """
    Performs hill climbing optimization for the TSP.
    """
    current_distance = distCircularIC(iCities)
    improved = True

    while improved:
        improved = False
        for i in range(len(iCities) - 1):
            for j in range(i + 1, len(iCities)):
                newTour = swap_cities(iCities, i, j)
                new_distance = distCircularIC(newTour)
                if new_distance < current_distance:
                    iCities = newTour
                    current_distance = new_distance
                    improved = True
                    break  # Exit the inner loop to restart search from new base tour
            if improved:
                break  # Restart the outer loop if an improvement was found

    return iCities, current_distance