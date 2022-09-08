from jovian.pythondsa import evaluate_test_cases

#these are all test cases
tests=[{'input': {'cards': [13, 11, 10, 7, 4, 3, 1, 0], 'query': 7}, 'output': 3},
 {'input': {'cards': [13, 11, 10, 7, 4, 3, 1, 0], 'query': 1}, 'output': 6},
 {'input': {'cards': [4, 2, 1, -1], 'query': 4}, 'output': 0},
 {'input': {'cards': [3, -1, -9, -127], 'query': -127}, 'output': 3},
 {'input': {'cards': [6], 'query': 6}, 'output': 0},
 {'input': {'cards': [9, 7, 5, 2, -9], 'query': 4}, 'output': -1},
 {'input': {'cards': [], 'query': 7}, 'output': -1},
 {'input': {'cards': [8, 8, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0], 'query': 3},'output': 7},
 {'input': {'cards': [8, 8, 6, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0],'query': 6},'output': 2}]

#generic binary search 

# def binary_search(lo,hi,condition):
#     while lo<=hi:
#         mid=(lo+hi)//2
#         print('hi',hi,'lo',lo,'mid',mid)
#         result=condition(mid)
#         if result =='found':
#             return mid
#         elif result=='left':
#             hi=mid-1
#         else:
#             lo=mid+1
#     return -1

# def locate_card(cards,query):
#     def condition(mid):
#         if cards[mid]==query:
#             if mid >0 and cards[mid-1]==query:
#                 return 'left'
#             else:
#                 return 'found'
#         elif cards[mid]<query:
#             return 'left'
#         else:
#             return 'right'
#     return binary_search(0, len(cards)-1, condition)

# evaluate_test_cases(locate_card, tests)
    
        
        

            
# Question 2 : Given an array of integers nums sorted in ascending order, 
# find the starting and ending position of a given number.

def binary_search(lo,hi,condition):
    while hi>=lo:
        mid=(hi+lo)//2
        result=condition(mid)
        if result=='found':
            return mid
        elif result=='left':
            hi=mid-1
        elif result=='right':
            lo=mid+1
    return -1

def first_position(nums,target):
    def condition(mid):
        if nums[mid]==target:
            if mid >0 and nums[mid-1]==target:
                return 'left'
            return 'found'
        elif nums[mid]<target:
            return 'right'
        return 'left'
    return binary_search(0,len(nums)-1, condition)
    
def last_position(nums,target):
    def condition(mid):
        if nums[mid]==target:
            if mid <len(nums)-1 and nums[mid+1]==target:
                return 'right'
            return 'found'
        elif nums[mid]<target:
            return 'right'
        return 'left'
    return binary_search(0,len(nums)-1, condition)
            
            

def first_last_position(nums, target):
    return first_position(nums, target), last_position(nums, target)


print(first_last_position([1,2,3,4,4,4],4))

