# Set: A
# Problem 1
from collections import deque


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


root = TreeNode("Trunk")
root.left = TreeNode("Mcintosh")
root.right = TreeNode("Granny Smith")
mcintosh = root.left
mcintosh.right = TreeNode("Opal")
mcintosh.left = TreeNode("Fiji")
granny = root.right
granny.right = TreeNode("Gala")
granny.left = TreeNode("Crab")


print_tree(root)

# Problem 2

class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def calculate_yield(root):
    if root.val == "+":
       return root.left.val + root.right.val
    elif root.val == "-":
        return root.left.val - root.right.val
    elif root.val == "*":
        return root.left.val * root.right.val
    

apple_tree = TreeNode("+", TreeNode(7), TreeNode(5))

print(calculate_yield(apple_tree))

# Problem 3
class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def right_vine(root):
    # list for all the right node
    ivy = []
    # start at the root
    curr = root
    # append the root to the list
    ivy.append(root.val)
    while curr.right:
    # traverse every right most node
        ivy.append(curr.right.val)
    # append it to a list
        curr = curr.right
    # return the lsit
    return ivy

ivy1 = TreeNode("Root", 
                TreeNode("Node1", TreeNode("Leaf1")),
                TreeNode("Node2", TreeNode("Leaf2"), TreeNode("Leaf3")))


ivy2 = TreeNode("Root", TreeNode("Node1", TreeNode("Leaf1")))

print(right_vine(ivy1))
print(right_vine(ivy2))

# Problem 4
# recursive
def right_vine2(root):
  if root is None:
      return []
  return [root.val] + right_vine2(root.right)

# a different way to approach the problem, with a recursive helper
def right_vine_recursive(root):
    res = []
    def traverse_right_nodes(curr, res):
        if not curr: # base case
            return res
        res.append(curr.val)
        return traverse_right_nodes(curr.right, res)
    return traverse_right_nodes(root, res)


"""
Example right_vine2(ivy2)
        Root
      /  
    Node1
    /
  Leaf1 


  return ["Root"] + [Node1, Leaf1] = [Root, Node1, Leaf1]
  
  """


print(right_vine2(ivy1))
print(right_vine2(ivy2))
