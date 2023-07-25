# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

# You must write an algorithm that runs in O(n) time and without using the division operation.

def product_except_self(nums):
    n = len(nums)
    
    # Initialize prefix_products and suffix_products arrays
    prefix_products = [1] * n
    suffix_products = [1] * n
    
    # Calculate prefix_products
    prefix_product = 1
    for i in range(1, n):
        prefix_product *= nums[i - 1]
        prefix_products[i] = prefix_product
    
    # Calculate suffix_products
    suffix_product = 1
    for i in range(n - 2, -1, -1):
        suffix_product *= nums[i + 1]
        suffix_products[i] = suffix_product
    
    # Calculate answer array
    answer = [prefix_products[i] * suffix_products[i] for i in range(n)]
    
    return answer