// Search through a tree using depth first search and return a list of node names

class Node {
  constructor(name) {
    this.name = name;
    this.children = [];
  }

  addChild(name) {
    this.children.push(new Node(name));
    return this;
  }

  // O(V + E) time | O(V) space

  depthFirstSearch(array) {
    let siblings = this.children;
    array.push(this.name);
    for (const sibling of siblings) {
      sibling.depthFirstSearch(array);
    }
    return array;
  }
}
