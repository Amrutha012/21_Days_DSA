def maxArea(height):
    l, r = 0, len(height) - 1
    max_area = 0
    
    while l < r:
        # Calculate area
        width = r - l
        area = min(height[l], height[r]) * width
        max_area = max(max_area, area)
        
        # Move the smaller pointer
        if height[l] < height[r]:
            l += 1
        else:
            r -= 1
    
    return max_area


# Example 1
print(maxArea([1,8,6,2,5,4,8,3,7]))  # Output: 49

# Example 2
print(maxArea([1,1]))  # Output: 1
