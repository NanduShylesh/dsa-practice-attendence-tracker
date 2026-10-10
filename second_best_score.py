def secondHighest(scores):
    highest = -1
    second = -1
    
    for score in scores:
        # If we find a new highest score, the old highest becomes the second highest
        if score > highest:
            second = highest
            highest = score
        # If the score is less than the highest but greater than the current second highest
        # (and distinct from the highest), update the second highest
        elif score > second and score != highest:
            second = score
            
    return second

# Example Usage:
# scores1 = [45, 78, 92, 78, 60]
# print(secondHighest(scores1)) # Expected: 78

# scores2 = [50, 50, 50]
# print(secondHighest(scores2)) # Expected: -1