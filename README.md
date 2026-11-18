# 📚 Data Structures in Python

A comprehensive collection of data structure implementations in Python. Perfect for learning, interview preparation, and understanding fundamental computer science concepts.

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Data Structures](https://img.shields.io/badge/Data%20Structures-Algorithms-green)
![Educational](https://img.shields.io/badge/Purpose-Educational-orange)

## 🎯 Overview

This repository contains clean, well-documented implementations of common data structures in Python. Each data structure includes:
- Clear implementation code
- Time and space complexity analysis
- Common operations
- Example usage
- Practice problems

## 📋 Implemented Data Structures

### Linear Data Structures
- ✅ **Arrays** - Fixed and dynamic arrays
- ✅ **Linked Lists** - Singly, doubly, and circular
- ✅ **Stacks** - LIFO implementation
- ✅ **Queues** - FIFO, circular, priority, deque

### Non-Linear Data Structures
- ✅ **Trees** - Binary tree, BST, AVL tree
- ✅ **Heaps** - Min heap, max heap
- ✅ **Graphs** - Adjacency list/matrix representation
- ✅ **Tries** - Prefix tree implementation

### Hash-Based Structures
- ✅ **Hash Tables** - Custom hash map
- ✅ **Hash Sets** - Unique element storage

### Advanced Structures
- ✅ **Bloom Filter** - Probabilistic data structure
- ✅ **Disjoint Set (Union-Find)** - Connected components
- ✅ **Segment Tree** - Range queries
- ✅ **Fenwick Tree (BIT)** - Prefix sum queries

## 🚀 Quick Start

### Clone the Repository
```bash
git clone https://github.com/PURON98/Data-Structure-Python.git
cd Data-Structure-Python
```

### Run Examples
```python
# Example: Using a Stack
from structures.stack import Stack

stack = Stack()
stack.push(10)
stack.push(20)
print(stack.pop())  # Output: 20
```

## 📁 Project Structure

```
Data-Structure-Python/
├── arrays/
│   ├── dynamic_array.py
│   └── examples.py
├── linked_lists/
│   ├── singly_linked_list.py
│   ├── doubly_linked_list.py
│   └── circular_linked_list.py
├── stacks/
│   ├── stack.py
│   └── applications.py
├── queues/
│   ├── queue.py
│   ├── priority_queue.py
│   └── deque.py
├── trees/
│   ├── binary_tree.py
│   ├── bst.py
│   ├── avl_tree.py
│   └── tree_traversals.py
├── graphs/
│   ├── graph.py
│   ├── bfs.py
│   ├── dfs.py
│   └── shortest_path.py
├── heaps/
│   ├── min_heap.py
│   └── max_heap.py
├── hash_structures/
│   ├── hash_table.py
│   └── hash_set.py
├── advanced/
│   ├── trie.py
│   ├── union_find.py
│   ├── segment_tree.py
│   └── fenwick_tree.py
└── README.md
```

## 📊 Complexity Analysis

### Time Complexities

| Data Structure | Access | Search | Insertion | Deletion |
|---------------|--------|--------|-----------|----------|
| Array | O(1) | O(n) | O(n) | O(n) |
| Linked List | O(n) | O(n) | O(1) | O(1) |
| Stack | O(n) | O(n) | O(1) | O(1) |
| Queue | O(n) | O(n) | O(1) | O(1) |
| Hash Table | N/A | O(1)* | O(1)* | O(1)* |
| Binary Tree | O(n) | O(n) | O(n) | O(n) |
| BST | O(log n) | O(log n) | O(log n) | O(log n) |
| AVL Tree | O(log n) | O(log n) | O(log n) | O(log n) |
| Heap | N/A | O(n) | O(log n) | O(log n) |

*Average case; O(n) worst case

## 🛠️ Technologies Used

- **Python 3.x** - Programming language
- **Type Hints** - Better code documentation
- **Docstrings** - Comprehensive documentation
- **Unit Tests** - pytest for testing

## 🎓 Learning Resources

### For Each Data Structure:
1. **Concept Explanation** - What and why
2. **Implementation** - Clean, readable code
3. **Operations** - Common methods
4. **Complexity** - Time and space analysis
5. **Use Cases** - Real-world applications
6. **Practice Problems** - Coding challenges

## 💡 Example Implementations

### Stack Example
```python
class Stack:
    def __init__(self):
        self.items = []
    
    def push(self, item):
        """Add item to top of stack - O(1)"""
        self.items.append(item)
    
    def pop(self):
        """Remove and return top item - O(1)"""
        if not self.is_empty():
            return self.items.pop()
        raise IndexError("Stack is empty")
    
    def peek(self):
        """Return top item without removing - O(1)"""
        if not self.is_empty():
            return self.items[-1]
        raise IndexError("Stack is empty")
    
    def is_empty(self):
        """Check if stack is empty - O(1)"""
        return len(self.items) == 0
```

### Binary Search Tree Example
```python
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None
    
    def insert(self, value):
        """Insert value into BST - O(log n) average"""
        if not self.root:
            self.root = TreeNode(value)
        else:
            self._insert_recursive(self.root, value)
    
    def _insert_recursive(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = TreeNode(value)
            else:
                self._insert_recursive(node.left, value)
        else:
            if node.right is None:
                node.right = TreeNode(value)
            else:
                self._insert_recursive(node.right, value)
```

## 🎯 Use Cases

### Stacks
- Function call management
- Undo/Redo operations
- Expression evaluation
- Browser history

### Queues
- Task scheduling
- Breadth-first search
- Print job management
- Request handling

### Trees
- File systems
- Database indexing
- Decision trees
- HTML DOM

### Graphs
- Social networks
- Maps and navigation
- Network routing
- Recommendation systems

### Hash Tables
- Caching
- Database indexing
- Symbol tables
- Frequency counting

## 🎓 Interview Topics Covered

- ✅ Array manipulation
- ✅ Two pointers technique
- ✅ Sliding window
- ✅ Linked list operations
- ✅ Stack applications
- ✅ Queue applications
- ✅ Tree traversals
- ✅ Graph algorithms (BFS, DFS)
- ✅ Dynamic programming basics
- ✅ Sorting and searching

## 🔧 Running Tests

```bash
# Install pytest
pip install pytest

# Run all tests
pytest tests/

# Run specific test file
pytest tests/test_stack.py

# Run with coverage
pytest --cov=structures tests/
```

## 🎯 Future Additions

- [ ] Red-Black Trees
- [ ] B-Trees
- [ ] Skip Lists
- [ ] Splay Trees
- [ ] Suffix Arrays
- [ ] KD Trees
- [ ] More graph algorithms
- [ ] Advanced heap variations

## 📚 Learning Path

### Beginner
1. Arrays
2. Linked Lists
3. Stacks
4. Queues

### Intermediate
5. Hash Tables
6. Trees (Binary Tree, BST)
7. Heaps
8. Basic Graphs

### Advanced
9. AVL Trees
10. Tries
11. Union-Find
12. Segment Trees
13. Advanced Graph Algorithms

## 🤝 Contributing

Contributions welcome! You can help by:
- Adding new data structures
- Improving documentation
- Adding more examples
- Writing tests
- Fixing bugs

## 📖 Resources

- **Books**
  - Introduction to Algorithms (CLRS)
  - Data Structures and Algorithms in Python
  - Cracking the Coding Interview

- **Online Platforms**
  - LeetCode
  - HackerRank
  - GeeksforGeeks

## 📝 License

This project is open source and available for educational purposes.

## 👨‍💻 Author

**Tabiul Mursalin Puron**
- GitHub: [@PURON98](https://github.com/PURON98)

## 🙏 Acknowledgments

- Computer science community
- Open-source contributors
- Interview preparation platforms

---

⭐ If this repository helped you learn data structures, please star it!

<p align="center">
  📚 Master the fundamentals of computer science! 📚
</p>