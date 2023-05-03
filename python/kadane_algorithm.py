def maxSubArraySum(a, size):
 
    max_so_far = -1e5 - 1
    max_ending_here = 0
 
    for i in range(0, size):
        max_ending_here = max_ending_here + a[i] # stores the maximum sum contiguous subarray ending at current index
        if (max_so_far < max_ending_here):
            max_so_far = max_ending_here # find the max sum contiguous subarray for the whole arrray
 
        if max_ending_here < 0: # if the max_ending_here < 0 then doesn't count, also can handle the array of negative num
            max_ending_here = 0 
    return max_so_far
 
# Driver function to check the above function
 
# a = [-2, -3, 4, -1, -2, 1, 5, -3]
a = [-1, 1, -3, -4, -5]
 
print("Maximum contiguous sum is", maxSubArraySum(a, len(a)))