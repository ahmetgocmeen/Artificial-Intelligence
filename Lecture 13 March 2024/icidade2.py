import sys
import time
import math
import libic as lb
import algorithm as alg
import greedy as grd
import gemini as gem
w = lb.windowIC(800)
cityList = lb.readTSP2ListIC("berlin52.tsp")
#cityList = lb.readTSP2ListICOpt("berlin52.tsp", "berlin52.opt.tour")

print(f"\nFirst Distance: {alg.distCircularIC(cityList)}")
lb.drawIC(cityList,w) 
input("Press Enter to Continue...")
print("Optimising...")

def euclidean_distance(city1, city2):
    """Compute the Euclidean distance between two cities."""
    return math.sqrt((city1[1] - city2[1])**2 + (city1[2] - city2[2])**2)

def create_distance_matrix(cities):
    """Create a distance matrix for a list of cities."""
    n = len(cities)
    dist_matrix = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(i + 1, n):  # Distance matrix is symmetric
            dist = euclidean_distance(cities[i], cities[j])
            dist_matrix[i][j] = dist_matrix[j][i] = dist
    return dist_matrix

#dist_matrix = create_distance_matrix(cityList)
iter = 10000
if len(sys.argv) > 1:
    iter = int(sys.argv[1])

st = time.process_time()
final = grd.hill_climbing(cityList)
#(ci,cf,optList) = alg.optDistCircularIC(cityList,iter)
#(optList,distance) = grd.hill_climbing_greedy(cityList,dist_matrix)
#optList = gem.hill_climbing(cityList)
#optList = cityList
#for i in range(iter):
#    optList = alg.mehoraDistCircularIC(optList,1)
et = time.process_time()
print("CPU Time: ", (et - st)*1000, "ms")

#lb.drawIC(optList,w)
#print("Optimized route:", optList)
#print("Total distance:", gem.total_distance(optList))
print("Distance: ", final[0])
#print("Final Distance: ", alg.distCircularIC(optList))
input("Press Enter")