# O(n^2) time | O(1) space

def twoNumberSum(array, targetSum):
    for i in range(0, len(array) - 1):																																
        NumberOne = array[i]
        for j in range(i +1, len(array)):
            NumberTwo = array[j]
            if NumberOne + NumberTwo == targetSum:
                return [NumberOne, NumberTwo]
    return  []


# O(n) time | O(n) space

def twoNumberSum(array, targetSum):
    numbers = {}
    for i in range(0 , len(array)):
        potentialMatch = targetSum - array[i]
        if potentialMatch in numbers:
            return [potentialMatch, array[i]]
		else:
			numbers[array[i]]= True
    return []
    
# O(n) time | O(1) space

def twoNumberSum(array, targetSum):
    array.sort()
    left = 0
    right = len(array) -1
    while left < right:
		currentSum = array[left] + array[right]
		if currentSum == targetSum:
            return [array[left], array[right]]
        elif currentSum < targetSum:
            left+=1
        elif currentSum > targetSum:
            right -=1  
	return []     
