import random
import algorithm as alg

def calculate_total_distance(tour, dist_matrix):
    """Calculate the total distance of the tour using a precomputed distance matrix."""
    total_distance = sum(dist_matrix[tour[i]][tour[(i + 1) % len(tour)]] for i in range(len(tour)))
    return total_distance

def attempt_improvement(tour, dist_matrix):
    """Attempt to find a single improvement by swapping two cities if it results in a shorter tour."""
    n = len(tour)
    for _ in range(n * (n - 1) // 2):  # Max number of unique pairs
        i, j = random.sample(range(n), 2)  # Choose two indices at random
        if i > j:
            i, j = j, i  # Ensure i < j for simplicity
        
        # Calculate the difference in distance if cities at i and j are swapped
        before_swap = dist_matrix[tour[i - 1]][tour[i]] + dist_matrix[tour[j]][tour[(j + 1) % n]]
        after_swap = dist_matrix[tour[i - 1]][tour[j]] + dist_matrix[tour[i]][tour[(j + 1) % n]]
        
        if after_swap < before_swap:
            tour[i:j+1] = reversed(tour[i:j+1])  # Perform the swap if it improves the total distance
            return True  # Indicate that an improvement was made
    return False  # No improvement found

def hill_climbing_greedy(tour, dist_matrix):
    """Optimize the tour using a greedy hill-climbing algorithm."""
    while attempt_improvement(tour, dist_matrix):
        pass  # Keep trying to improve the tour until no further improvements can be found
    return tour, calculate_total_distance(tour, dist_matrix)
