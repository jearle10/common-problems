# Average O(log(n)) time | O(log(n))
# Worst O(n) time | O(n) space


def findClosestValueInBst(tree , target):
    return search(tree, target, float("inf"))

def search(tree, target, closest):
    if tree is None:
        return closest
    if abs(target - closest) > abs(target - tree.value):
        closest = tree.value
    if target < tree.value:
        return search(tree.left, target, closest)
    elif target > tree.value:
        return search(tree.right, target, closest)
    else:
        return closest
