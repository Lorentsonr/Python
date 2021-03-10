#1  Biggie Size - Given a list, write a function that changes all positive numbers in the 
# list to "big".
# Example: biggie_size([-1, 3, 5, -5]) returns that same list, 
# but whose values are now [-1, "big", "big", -5]

def one(list):
    for i in range(0, len(list)):
        if list[i] > 0:
            list[i] = "big"
    return list

# print(one([1,3,-4,7,-8,0]))

#2 Count Positives - Given a list of numbers, create a function to replace the last 
# value with the number of positive values. (Note that zero is not considered to be 
# a positive number).
# Example: count_positives([-1,1,1,1]) changes the original list to [-1,1,1,3] and 
# returns it
# Example: count_positives([1,6,-4,-2,-7,-2]) changes the list to [1,6,-4,-2,-7,2] and 
# returns it

def two(list):
    sum = 0
    for i in range(0, len(list)):
        if list[i] > 0:
            sum += 1
    list[len(list)-1] = sum
    return list

# print(two([3,-2,7,-1,6,2,-5]))

#3 Sum Total - Create a function that takes a list and returns the sum of all 
# the values in the list.
# Example: sum_total([1,2,3,4]) should return 10
# Example: sum_total([6,3,-2]) should return 7

def three(list):
    sum = 0
    for i in range(0, len(list)):
        sum += list[i]
    return sum
# print(three([1,2,3,4]))

#4 Average - Create a function that takes a list and returns the average of 
# all the values.x
# Example: average([1,2,3,4]) should return 2.5

def four(list):
    sum = 0
    for i in range(0, len(list)):
        sum += list[i]
    avg = (sum / len(list))
    return avg

# print(four([1,2,3,4]))

# #5 Length - Create a function that takes a list and returns the length of the list.
# # Example: length([37,2,1,-9]) should return 4
# # Example: length([]) should return 0

def five(list):
    return len(list)
# print(five([3,2,-5,7,8]))

# #6 Minimum - Create a function that takes a list of numbers and returns the minimum value in the list. If the list is empty, have the function return False.
# # Example: minimum([37,2,1,-9]) should return -9
# # Example: minimum([]) should return False

# def six(list):
#     if len(list) < 1:
#         return False
#     return min(list)
# print(six([4,3,6,9,5,1]))

def six(list):
    min = list[0]
    for i in range(0,len(list)):
        if min > list[i]:
            min = list[i]
    return min
# print(six([5,3,-4,6,7,1]))

# 7 Maximum - Create a function that takes a list and returns the maximum value in the list. 
# If the list is empty, have the function return False.
# Example: maximum([37,2,1,-9]) should return 37
# Example: maximum([]) should return False

# def seven(list):
#     if len(list) < 1:
#         return False
#     return max(list)
# print(seven([5,3,7,87,42]))

def seven(list):
    max = list[0]
    for i in range(0,len(list)):
        if max < list[i]:
            max = list[i]
    return max
# print(seven([5,3,-4,6,7,1]))



# 8 Ultimate Analysis - Create a function that takes a list and returns a dictionary 
# that has the sumTotal, average, minimum, maximum and length of the list.
# Example: ultimate_analysis([37,2,1,-9]) should return {'sumTotal': 31, 'average': 7.75, 
# 'minimum': -9, 'maximum': 37, 'length': 4 }

def eight(list):
    dict = {}
    average = 0

    dict['sumTotal'] = sum(list)
    average = sum(list) / len(list)
    dict['average'] = average
    dict['min'] = min(list)
    dict['max'] = max(list)
    dict['length'] = len(list)

    return dict

# print(eight([37,2,1,-9]))

def ultimate(arr):
    myDict = {
        'sumTotal' : three(arr),
        'average' : four(arr),
        'min' : six(arr),
        'max' : seven(arr),
        'length' : five(arr)
    }
    return myDict
# print(ultimate([5,7,5,3,1,5,9]))
# 9 Reverse List - Create a function that takes a list and return that list with values reversed. 
#  Do this without creating a second list. (This challenge is known to appear during basic technical interviews.)
#  Example: reverse_list([37,2,1,-9]) should return [-9,1,2,37]

def nine(list):
    for i in range(0, len(list) // 2):
        temp = list[i]
        list[i] = list[len(list)-1-i]
        list[len(list)-1-i] = temp
    return list

print(nine([7,5,-7,2,3,5, 20, 5,1]))
