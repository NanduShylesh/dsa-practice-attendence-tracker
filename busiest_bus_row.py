def busiestRow(grid):
    max_total = -1
    best_row = -1
    
    # Outer loop for the rows
    for r in range(len(grid)):
        current_total = 0
        
        # Inner loop to add up the seats in the current row
        for c in range(len(grid[r])):
            current_total += grid[r][c]
            
        # Update the best row ONLY if the new total is strictly larger
        if current_total > max_total:
            max_total = current_total
            best_row = r
            
    return f"Row {best_row}, Total {max_total}"

# Example Usage:
# grid = [
#     [2, 0, 1],
#     [3, 3, 1],
#     [1, 1, 1]
# ]
# print(busiestRow(grid)) # Expected: Row 1, Total 7