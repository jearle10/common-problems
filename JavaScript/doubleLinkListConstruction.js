// This is an input class. Do not edit.
class Node {
  constructor(value) {
    this.value = value;
    this.prev = null;
    this.next = null;
  }
}

// Feel free to add new properties and methods to the class.
class DoublyLinkedList {
  constructor() {
    this.head = null;
    this.tail = null;
  }

  setHead(node) {
    if (this.head === null) {
      this.head = node;
      this.tail = node;
      return;
    }
    this.insertBefore(this.head, node);
  }

  setTail(node) {
    if (this.tail === null) {
      this.setHead(node);
      return;
    }
    this.insertAfter(this.tail, node);
  }

  insertBefore(node, nodeToInsert) {
    if (nodeToInsert === this.head && nodeToInsert === this.tail) {
      // Check that the node being moved isn't the only node in the linked list
      return;
    }
    this.remove(nodeToInsert); // Remvoe the node from it's current position
    nodeToInsert.prev = node.prev; // Add the previous pointer to the node before
    nodeToInsert.next = node.next; // Add the next pointer to the node after

    if (node.prev === null) {
      // Check the previous node to see if it is null
      this.head = nodeToInsert; // If the previous node is null then set the head of the linked list the newly inserted node
    } else {
      node.prev.next = nodeToInsert; // If the previous node is not null the point it to the newly inserted node
    }
  }

  insertAfter(node, nodeToInsert) {
    if (nodeToInsert === this.head && nodeToInsert === this.tail) {
      return;
    }
    this.remove(nodeToInsert);
    nodeToInsert.prev = node;
  }

  insertAtPosition(position, nodeToInsert) {
    // Write your code here.
  }

  removeNodesWithValue(value) {
    // Write your code here.
  }

  remove(node) {
    if (node === this.head) {
      this.head = this.head.next;
    }
    if (node === this.tail) {
      this.tail = this.tail.prev;
    }
    this.removeNodePointers(node);
  }

  removeNodePointers(node) {
    if (node.prev !== null) {
      // Check that the previous node isnt null
      node.prev.next = node.next; // If node present the point it to skip the current node
    }
    if (node.next !== null) {
      // Check that the next node isnt node
      node.next.prev = node.prev; // If the next node is present then point it to skip the current node
    }
    node.next = null; // Delete the next pointer from the current node
    node.prev = null; // Delete the previous pointer from the current node
  }

  containsNodeWithValue(value) {
    // Write your code here.
  }
}
