// Average O(log(n)) time | O(log(n)) space

// Worst O(n) time | O(n) space

function findClosestValueInBst(tree, target) {
	return searchTree(tree, target , Infinity);
}

function searchTree(tree, target, closestNode){
	if(tree === null) {
		return closestNode;
	}
	if(Math.abs(target - closestNode) > Math.abs(target - tree.value)){
		closestNode = tree.value;
	}
	if(target < tree.value){
		return searchTree(tree.left, target, closestNode);
	} else if (target > tree.value){
		return searchTree(tree.right , target , closestNode);
	} else {
		return closestNode;
	}
	
}

