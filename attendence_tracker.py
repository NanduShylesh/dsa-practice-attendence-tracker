def attendanceSummary(days):
    present_count = 0
    max_streak = 0
    current_streak = 0
    
    for day in days:
        if day == 1:
            present_count += 1
            current_streak += 1
            if current_streak > max_streak:
                max_streak = current_streak
        else:
            current_streak = 0
            
    return {"Present": present_count, "Longest streak": max_streak}

# Example Usage:
# days = [1, 1, 0, 1, 1, 1, 0, 1]
# print(attendanceSummary(days))