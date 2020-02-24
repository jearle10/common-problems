class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

# O(V + E) time | O(V) space    

    def depthFirstSearch(self, array):
    siblings = self.children 
    array.append(self.name)
    for sibling in siblings:
        sibling.depthFirstSearch(array)
    return array