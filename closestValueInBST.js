// Find the closest value in a Binary search tree - Assume there will only be one closest value 


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

 // Best O(log(n)) time | O(1) space 
 // Worst O(n) time | O(1) space

function findClosestValueInBst(tree, target){
    return searchTree(tree, target, Infinity)
}
function searchTree(tree, target , closestNode)
        while (tree != null){
            if(Math.abs(target - closestNode) > Math.abs(target - tree.value)){
                closestNode = tree.value
            }
            if(target < tree.value){
                tree = tree.left
            } else if ( target > tree.value){
                tree = tree.right
            } else{
                break
            }
        }
    }
    return closestNode
}

