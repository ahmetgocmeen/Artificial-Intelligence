import math
import random
import algorithm as alg

def hillClimbing(cityList, maxIterations=10000):
  currentState = cityList.copy()
  currentDistance = alg.distCircularIC(currentState)

  for _ in range(maxIterations):
    # Generate a random neighbor by swapping two cities
    neighborIndex1 = random.randint(0, len(cityList) - 1)
    neighborIndex2 = random.randint(0, len(cityList) - 1)
    neighbor = alg.swapIC(currentState.copy(), neighborIndex1, neighborIndex2)

    neighborDistance = alg.distCircularIC(neighbor)

    # Improve the solution if a better neighbor is found
    if neighborDistance < currentDistance:
      currentState = neighbor
      currentDistance = neighborDistance

  return currentState

def stochasticHillClimbing(cityList, maxIterations=10000, temperature=0.8):
  currentState = cityList.copy()
  currentDistance = alg.distCircularIC(currentState)

  for _ in range(maxIterations):
    # Generate a random neighbor by swapping two cities
    neighborIndex1 = random.randint(0, len(cityList) - 1)
    neighborIndex2 = random.randint(0, len(cityList) - 1)
    neighbor = alg.swapIC(currentState.copy(), neighborIndex1, neighborIndex2)

    neighborDistance = alg.distCircularIC(neighbor)

    # Accept improvement unconditionally
    if neighborDistance < currentDistance:
      currentState = neighbor
      currentDistance = neighborDistance

    # Accept worse neighbor with a probability based on temperature
    else:
      delta_distance = neighborDistance - currentDistance
      acceptance_probability = math.exp(-delta_distance / temperature)
      if random.random() < acceptance_probability:
        currentState = neighbor
        currentDistance = neighborDistance

    # Gradually decrease temperature to favor better solutions later
    temperature *= 0.95  # You can adjust this cooling rate

  return currentState

def firstChoiceHillClimbing(cityList, maxIterations, num_neighbors):
  currentState = cityList.copy()
  currentDistance = alg.distCircularIC(currentState)

  for _ in range(maxIterations):
    improved = False
    for _ in range(num_neighbors):
      # Generate a random neighbor by swapping two cities
      neighborIndex1 = random.randint(0, len(cityList) - 1)
      neighborIndex2 = random.randint(0, len(cityList) - 1)
      neighbor = alg.swapIC(currentState.copy(), neighborIndex1, neighborIndex2)

      neighborDistance = alg.distCircularIC(neighbor)

      # Accept the first improvement found
      if neighborDistance < currentDistance:
        currentState = neighbor
        currentDistance = neighborDistance
        improved = True
        break  # Stop searching for better neighbors in this iteration

    # If no improvement found in this iteration, terminate
    if not improved:
      break

  return currentState

def restartStochasticHillHlimbing(cityList, maxIterations, temperature, max_restarts):
  bestState = cityList.copy()
  bestDistance = alg.distCircularIC(bestState)

  for _ in range(max_restarts):
    currentState = cityList.copy()
    currentDistance = alg.distCircularIC(currentState)

    for _ in range(maxIterations):
      # Generate a random neighbor by swapping two cities
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

    # Gradually decrease temperature to favor better solutions later
    temperature *= 0.95  # You can adjust this cooling rate

    # Update best solution if current is better
    if currentDistance < bestDistance:
      bestState = currentState.copy()
      bestDistance = currentDistance

  return bestState


