import sys
import time
import libic as lb
import algorithm as alg

w = lb.windowIC(800)
#cityList = lb.readTSP2ListIC("berlin52.tsp")
cityList = lb.readTSP2ListICOpt("berlin52.tsp", "berlin52.opt.tour")

print(f"\nFirst Distance: {alg.distCircularIC(cityList)}")
lb.drawIC(cityList,w) 
input("Press Enter to Continue...")
print("Optimising...")

iter = 10000
if len(sys.argv) > 1:
    iter = int(sys.argv[1])

st = time.process_time()
(ci,cf,optList) = alg.optDistCircularIC(cityList,iter)
#optList = cityList
#for i in range(iter):
#    optList = alg.mehoraDistCircularIC(optList,1)
et = time.process_time()
print("CPU Time: ", (et - st)*1000, "ms")

lb.drawIC(optList,w)
print("Final Distance: ", alg.distCircularIC(optList))
input("Press Enter")