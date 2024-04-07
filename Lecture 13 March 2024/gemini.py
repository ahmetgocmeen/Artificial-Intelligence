import math
import random

def distance(city1, city2):
  """Calculates the Euclidean distance between two cities."""
  x1, y1 = city1
  x2, y2 = city2
  return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def total_distance(city_list):
  """Calculates the total distance of a circular route."""
  total_dist = 0
  for i in range(len(city_list)):
    city1 = city_list[i]
    if i < len(city_list) - 1:
      city2 = city_list[i + 1]
    else:
      city2 = city_list[0]  # Connect last city to first for circular route
    total_dist += distance(city1, city2)
  return total_dist

def swap_cities(city_list, i, j):
  """Swaps the positions of two cities in the list."""
  new_list = city_list.copy()
  new_list[i], new_list[j] = new_list[j], new_list[i]
  return new_list

def hill_climbing(city_list, max_iterations=10000):
  """Performs hill climbing search to find a local optimum."""
  current_state = city_list.copy()
  current_distance = total_distance(current_state)

  for _ in range(max_iterations):
    # Generate a random neighbor by swapping two cities
    neighbor_index1 = random.randint(0, len(city_list) - 1)
    neighbor_index2 = random.randint(0, len(city_list) - 1)
    neighbor = swap_cities(current_state.copy(), neighbor_index1, neighbor_index2)

    neighbor_distance = total_distance(neighbor)

    # Improve the solution if a better neighbor is found
    if neighbor_distance < current_distance:
      current_state = neighbor
      current_distance = neighbor_distance

  return current_state