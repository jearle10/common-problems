def branchSums(root):
    sums = []
    sum(root,0,sums)
	return sums

def sum(node,currentSum,sums):
    if node is None:
		return
    currentSum += node.value
    if node.left is None and node.right is None:
        sums.append(currentSum)
        return  
    sum(node.left, currentSum, sums)
    sum(node.right, currentSum, sums)   