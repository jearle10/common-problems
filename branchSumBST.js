// Sum the total of each branch within a binary search tree

// Class of the input root

// O(n) time | O(n) space

class BinaryTree {
  constructor(value) {
    this.value = value;
    this.left = null;
    this.right = null;
  }
}

function branchSums(root) {
  const sums = [];
  sum(root, 0, sums);
  return sums;
}

function sum(node, currentSum, sums) {
  if (!node) {
    return;
  }
  currentSum += node.value;
  if (!node.left && !node.right) {
    sums.push(currentSum);
    return;
  }
  sum(node.left, currentSum, sums);
  sum(node.right, currentSum, sums);
}
