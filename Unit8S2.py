# Set Version 2
# Problem 1

from collections import deque 

# Tree Node class
class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def print_tree(root):
    if not root:
        return "Empty"
    result = []
    queue = deque([root])
    while queue:
        node = queue.popleft()
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)
    while result and result[-1] is None:
        result.pop()
    print(result)

def build_tree(values):
  if not values:
      return None

  def get_key_value(item):
      if isinstance(item, tuple):
          return item[0], item[1]
      else:
          return None, item

  key, value = get_key_value(values[0])
  root = TreeNode(value, key)
  queue = deque([root])
  index = 1

  while queue:
      node = queue.popleft()
      if index < len(values) and values[index] is not None:
          left_key, left_value = get_key_value(values[index])
          node.left = TreeNode(left_value, left_key)
          queue.append(node.left)
      index += 1
      if index < len(values) and values[index] is not None:
          right_key, right_value = get_key_value(values[index])
          node.right = TreeNode(right_value, right_key)
          queue.append(node.right)
      index += 1

  return root
         
def count_odd_splits(root):
    # return the total of odd values in the nodes 
    if not root:
        return 0
    
    total = 0
    if root.val % 2 == 1:
        total += 1
            
    total += count_odd_splits(root.left)
    total += count_odd_splits(root.right)

    return total 

"""   2
     / \
    /   \
   3     5
  / \     \
 6   7     12
"""

values = [2, 3, 5, 6, 7, None, 12]
monstera = build_tree(values)

print(count_odd_splits(monstera))
print(count_odd_splits(None))


# Problem 2: Flower Finding

class TreeNode():
     def __init__(self, value, left=None, right=None):
         self.val = value
         self.left = left
         self.right = right
         
def find_flower(inventory, name):
    current = inventory

    while current:
        if current.val == name:
            return True
        elif name < current.val:
            current = current.left
        else: 
            current = current.right

    return False

# using build_tree() function at top of page
values = ["Rose", "Lilac", "Tulip", "Daisy", "Lily", None, "Violet"]
garden = build_tree(values)

print(find_flower(garden, "Lilac"))  
print(find_flower(garden, "Sunflower")) 


# Problem 3: Flower Finding II
def non_bst_find_flower(root, name):
    if root is None:
        return False
    
    if root.val == name:
        return True

    return non_bst_find_flower(root.left, name) or non_bst_find_flower(root.right, name)


"""
         Daisy
        /    \
      Lily   Tulip
     /  \       \
  Rose  Violet  Lilac
"""

# using build_tree() function at top of page
values = ["Rose", "Lily", "Tulip", "Daisy", "Lilac", None, "Violet"]
garden = build_tree(values)

print(non_bst_find_flower(garden, "Lilac"))  
print(non_bst_find_flower(garden, "Sunflower"))  


# Compare your solution to find_flower() in Problem 2 to the following solution. 
# Discuss with your group: How is the code different? Why?
# - 1st solution has o(log n) and 2nd has o(n) [searchs every node]


# What is the time complexity of non_bst_find_flower()? 
# How does it compare to the time complexity of find_flower() in Problem 2?
# - It is not alphabetically ordered, so it has a time complexity of O(n) as it may have to traverse every node in the tree.

  
# How would the time complexity of find_flower()
# from Problem 2 change if the tree inventory was not balanced?
# - If the tree is not balanced, the time complexity could degrade to O(n) in the worst case, similar to a linked list, as it may have to traverse all nodes in a skewed tree.

