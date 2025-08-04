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

class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def is_balanced(display):
	
    
    def helper(val):

        if not val:
            return True

        right = val.right 
        left = val.left

        




"""
      🎂
     /  \
   🥮   🍩
       /  \  
     🥖    🧁

"""
# Using build_tree() function included at top of page
baked_goods = ["🎂", "🥮", "🍩", "🥖", "🧁"]
display1 = build_tree(baked_goods)

"""
          🥖
         /  \
       🧁    🧁
       /       \  
      🍪       🍪
     /           \
    🥐           🥐  

"""
baked_goods = ["🥖", "🧁", "🧁", "🍪", None, None, "🍪", "🥐", None, None, "🥐"]
display2 = build_tree(baked_goods)


print(is_balanced(display1)) 
print(is_balanced(display2)) 