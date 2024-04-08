import sys
import time
import libic as lb
import algorithm as alg
import greedy as grd
w = lb.windowIC(800)
cityList = lb.readTSP2ListIC("berlin52.tsp")
#cityList = lb.readTSP2ListICOpt("berlin52.tsp", "berlin52.opt.tour")

print(f"\nFirst Distance: {alg.distCircularIC(cityList)}")
lb.drawIC(cityList,w) 
input("Press Enter to Continue...")
print("Optimising...")

iter = 10000
numNeigbors = 10000
temperature = 0.8
numRestarts = 2000
if len(sys.argv) > 1:
    iter = int(sys.argv[1])

st = time.process_time()
(ci,cf,optList) = alg.optDistCircularIC(cityList,iter)
#optList = grd.hillClimbing(cityList,iter)
#optList = grd.stochasticHillClimbing(cityList,iter,temperature)
#optList = grd.firstChoiceHillClimbing(cityList,iter,numNeigbors)
#optList = grd.restartStochasticHillHlimbing(cityList,iter,temperature,numRestarts)
#optList = cityList
#for i in range(iter):
#    optList = alg.betterDistCircularIC(optList,1)
et = time.process_time()
print("CPU Time: ", (et - st)*1000, "ms")
lb.drawIC(optList,w)
print("Final Distance: ", alg.distCircularIC(optList))
input("Press Enter")