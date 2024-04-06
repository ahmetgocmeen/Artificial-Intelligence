import math
import random
import libic as lb
import algorithm as alg

w = lb.windowIC(800)
cityList = lb.readTSP2ListIC("eil51.tsp")


print(f"\nCircular distance between random iCities: {alg.distCircularIC(cityList)}")
lb.drawIC(cityList,w) 
input("Enter para continuar... ")
