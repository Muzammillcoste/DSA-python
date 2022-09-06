from jovian.pythondsa import evaluate_test_cases

#QUESTION 1: Alice has some cards with numbers written on them. She arranges the 
#cards in decreasing order, and lays them out face down in a sequence on a table. 
# She challenges Bob to pick out the card containing a given number by turning over as 
# few cards as possible. Write a function to help Bob locate the card.

#Here hint is sorted,comparsion so we conclude that binary search algo is apply

# Find the middle element of the list.
# If it matches queried number, return the middle position as the answer.
# If it is less than the queried number, then search the first half of the list
# If it is greater than the queried number, then search the second half of the list
# If no more elements remain, return -1.

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

#[input][cards],[input][query]
# binary_search_algorithm

# def locate_card(cards,query):
#     lo,hi=0,len(cards)-1
#     while hi>=lo:
#         mid=(lo+hi)//2
#         mid_number=cards[mid]
        
#         if mid_number==query:
#             return mid
#         elif mid_number<query:
#             hi=mid-1
#         elif mid_number>query:
#             lo=mid+1
            
#     return -1

# evaluate_test_cases(locate_card, tests)

#[8, 8, 6, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0] above func fail to solve this test
#because 6 found in middle of list but we have to find first occurence


def test_location(cards, query, mid):
    mid_number = cards[mid]
    print('mid:', mid, ', mid_number:', mid_number)
    if mid_number == query:
        if mid-1 >= 0 and cards[mid-1] == query:
            return 'left'
        else:
            return 'found'
    elif mid_number < query:
        return 'left'
    else:
       return 'right'   
    
def locate_card(cards, query):
    lo, hi = 0, len(cards) - 1
    while lo <= hi:
        print('lo:', lo, ',hi:', hi)
        mid = (lo+hi) // 2
        result = test_location(cards, query, mid)
        if result == 'found':
            return mid
        elif result == 'left':
            hi = mid - 1
        elif result == 'right':
            lo = mid + 1
    return -1



evaluate_test_cases(locate_card, tests)

