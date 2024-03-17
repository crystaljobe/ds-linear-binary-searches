# Write two functions to find a specific number in an unsorted list on int
# 1. linear search 
# 2. binary search 
# - return the answer and the number of steps the program took to encounter the answer

def linear_search_unsorted(arr, target):
    steps = 0 # set steps to 0
    
    for num in arr:
        steps += 1
        if num == target:
            index = arr.index(num)
            return f"Scenario 1 (Linear Search): Target {target_1} found at index {index} in {steps} steps."
            
def binary_search_unsorted(arr, target):
    steps = 0 
    
    left = 0
    right = len(arr) - 1
    
    while left <= right: 
        steps += 1 
        middle = (left + right) // 2
        
        if target == arr[middle]:
            index = middle
            return f"Scenario 1 (Binary Search): Target {target} found at index {index} in {steps} steps."
        elif target > arr[middle]:
            left = middle + 1
        else:
            right = middle - 1        
            
    return f"Scenario 1 (Binary Search): Target {target} found at index -1 in {steps} steps." 

    
unsorted_list = [42, 15, 7, 30, 22, 10, 18]
target_1 = 30

result_linear_search_1 = linear_search_unsorted(unsorted_list, target_1)
result_binary_search_1 = binary_search_unsorted(sorted(unsorted_list), target_1)

# print(result_linear_search_1)
# print(result_binary_search_1)

# =================== SCENARIO 2 ==================== # 
# Write 2 functions to find a specific word in the list 
# 1. Linear
# 2. Binary
# return that includes the answer and num of steps program took to encounter the answer

def linear_search_sorted_words(word_list, target_word):
    steps = 0
    
    for item in word_list:
        steps += 1
        if item == target_word:
            index = word_list.index(item)
            return f"Scenario 2 (Linear Search): Target {target_word} found at index {index} in {steps} steps."
        

def binary_search_sorted_words(word_list, target_word):
    steps = 0 
    left = 0
    right = len(word_list) - 1  
        
    while left <= right: 
        middle = (left + right)//2
        steps += 1
        
        if word_list[middle] == target_word:
            index = middle
            return f"Scenario 2 (Binary Search): Target {target_word} found at index {index} in {steps} steps."
        elif word_list[middle] < target_word:
            left = middle + 1
        else:
            right = middle - 1
    return f"Scenario 2 (Binary Search): Target {target_word} found at index -1 in {steps} steps."

sorted_word_list = ['apple', 'banana', 'cherry', 'grape', 'orange', 'strawberry']
target_2 = 'orange'
result_linear_search_2 = linear_search_sorted_words(sorted_word_list, target_2)
result_binary_search_2 = binary_search_sorted_words(sorted_word_list, target_2)
# print(result_binary_search_2) # output: Scenario 2 (Binary Search): Target orange found at index 4 in 2 steps.
# print(result_linear_search_2) # output: Scenario 2 (Linear Search): Target orange found at index 4 in 5 steps.

# Scenario 3 
# - create 2 functions that take a list of int to find last occurance of a specific num in the list 
# 1. Linear Search 
# 2. Binary Search 
# - return answer and num of steps program took 


def linear_search_last_occurrence(arr, target):
    steps = 0 
    
    i = len(arr) - 1
    while i >= 0: 
        steps += 1
        if arr[i] == target:
            index = i
            return f"Scenario 3 (Linear Search): Last occurrence of {target} found at index {index} in {steps} steps."
        else: 
            i -= 1
    return f"Scenario 3 (Linear Search): Last occurrence of {target} found at index {index} in {steps} steps."
        

def binary_search_last_occurrence(arr, target):
    steps = 0 
    left = 0
    right = len(arr) - 1
    print(arr)
    
    while left <= right: 
        middle = (left + right)//2
        steps += 1
        if arr[middle] == target:
            print(middle)
            i = 1
            found = False
            # TODO: change while statement to find last item
            while found == False: 
                if arr[middle + i] == target:
                    i += 1
                else: 
                    middle += i
                    found == True

            return f"Scenario 3 (Binary Search): Last occurrence of {target} found at index {middle} in {steps} steps."
        elif arr[middle] < target:
            left = middle + 1
        else: 
            right = middle - 1
            
    return f"Scenario 3 (Binary Search): Last occurrence of {target} found at index -1 in {steps} steps."


# Scenario 3 Test
occurrence_list = [5, 10, 15, 20, 10, 25, 30, 35, 10, 40]
target_3 = 10
result_linear_search_3 = linear_search_last_occurrence(occurrence_list, target_3)
# print(result_linear_search_3)
result_binary_search_3 = binary_search_last_occurrence(sorted(occurrence_list), target_3)
print(result_binary_search_3)

