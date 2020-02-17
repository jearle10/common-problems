
// Function that takes in a non-empty array of distinct integers and an integer representing a target sum. If any two numbers in the input array sum up to the target sum, the function should return an empty array.

// Assumption: There will be at least one pair of numbers that sum to yield the target sum


// O(n^2) | o(1)

function twoNumberSum(array, targetSum) {
	let numbers = [];
	for(let i = 0 ; i < array.length -1 ; i++){
		for(let j = i +1 ; j < array.length; j ++){
			if(array[i]+array[j] == targetSum){
				numbers.push(array[i],array[j]);
			}
		};
	} return numbers
} 


