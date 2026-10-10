def countInBand(scores, low, high):
    # Helper to find the first index where score >= target
    def first_ge(target):
        left, right = 0, len(scores)
        while left < right:
            mid = (left + right) // 2
            if scores[mid] < target:
                left = mid + 1
            else:
                right = mid
        return left

    # Helper to find the first index where score > target
    def first_gt(target):
        left, right = 0, len(scores)
        while left < right:
            mid = (left + right) // 2
            if scores[mid] <= target:
                left = mid + 1
            else:
                right = mid
        return left

    start_index = first_ge(low)
    end_index = first_gt(high)
    
    return end_index - start_index

# Example Usage:
# scores = [35, 42, 42, 50, 58, 58, 58, 63, 71, 88]
# print(countInBand(scores, 42, 58)) # Expected: 6
# print(countInBand(scores, 90, 100)) # Expected: 0