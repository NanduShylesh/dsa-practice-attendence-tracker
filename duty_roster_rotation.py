def rotateRoster(names, k):
    n = len(names)
    # Remove full turns, as rotating by 'n' places brings the roster back to the start
    effective_k = k % n 
    
    # Create an empty list of the same size
    rotated = [None] * n
    
    # Move each name to its new position
    for i in range(n):
        new_index = (i + effective_k) % n
        rotated[new_index] = names[i]
        
    return rotated

# Example Usage:
# names = ['A', 'B', 'C', 'D', 'E']
# print(rotateRoster(names, 2)) # Expected: ['D', 'E', 'A', 'B', 'C']
# print(rotateRoster(names, 7)) # Expected: ['D', 'E', 'A', 'B', 'C']