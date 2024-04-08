import math
import random
import algorithm as alg

def hillClimbing(cityList, maxIterations):
  currentState = cityList.copy()
  currentDistance = alg.distCircularIC(currentState)

  for _ in range(maxIterations):
    neighborIndex1 = random.randint(0, len(cityList) - 1)
    neighborIndex2 = random.randint(0, len(cityList) - 1)
    neighbor = alg.swapIC(currentState.copy(), neighborIndex1, neighborIndex2)

    neighborDistance = alg.distCircularIC(neighbor)
    if neighborDistance < currentDistance:
      currentState = neighbor
      currentDistance = neighborDistance

  return currentState

def stochasticHillClimbing(cityList, maxIterations, temperature):
  currentState = cityList.copy()
  currentDistance = alg.distCircularIC(currentState)

  for _ in range(maxIterations):
    neighborIndex1 = random.randint(0, len(cityList) - 1)
    neighborIndex2 = random.randint(0, len(cityList) - 1)
    neighbor = alg.swapIC(currentState.copy(), neighborIndex1, neighborIndex2)

    neighborDistance = alg.distCircularIC(neighbor)

    if neighborDistance < currentDistance:
      currentState = neighbor
      currentDistance = neighborDistance
    else:
      delta_distance = neighborDistance - currentDistance
      acceptance_probability = math.exp(-delta_distance / temperature)
      if random.random() < acceptance_probability:
        currentState = neighbor
        currentDistance = neighborDistance

    temperature *= 0.95 

  return currentState

def firstChoiceHillClimbing(cityList, maxIterations, numNeighbors):
  currentState = cityList.copy()
  currentDistance = alg.distCircularIC(currentState)

  for _ in range(maxIterations):
    improved = False
    for _ in range(numNeighbors):
      neighborIndex1 = random.randint(0, len(cityList) - 1)
      neighborIndex2 = random.randint(0, len(cityList) - 1)
      neighbor = alg.swapIC(currentState.copy(), neighborIndex1, neighborIndex2)

      neighborDistance = alg.distCircularIC(neighbor)

      if neighborDistance < currentDistance:
        currentState = neighbor
        currentDistance = neighborDistance
        improved = True
        break 

    if not improved:
      break

  return currentState

def restartStochasticHillHlimbing(cityList, maxIterations, temperature, numRestarts):
  bestState = cityList.copy()
  bestDistance = alg.distCircularIC(bestState)

  for _ in range(numRestarts):
    currentState = cityList.copy()
    currentDistance = alg.distCircularIC(currentState)

    for _ in range(maxIterations):
      neighborIndex1 = random.randint(0, len(cityList) - 1)
      neighborIndex2 = random.randint(0, len(cityList) - 1)
      neighbor = alg.swapIC(currentState.copy(), neighborIndex1, neighborIndex2)
      neighborDistance = alg.distCircularIC(neighbor)
      if neighborDistance < currentDistance:
        currentState = neighbor
        currentDistance = neighborDistance
      else:
        delta_distance = neighborDistance - currentDistance
        acceptance_probability = math.exp(-delta_distance / temperature)
        if random.random() < acceptance_probability:
          currentState = neighbor
          currentDistance = neighborDistance

    temperature *= 0.95 

    if currentDistance < bestDistance:
      bestState = currentState.copy()
      bestDistance = currentDistance

  return bestState


