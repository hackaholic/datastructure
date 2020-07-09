import sys
import binarytree

MIN_VALUE = -sys.maxsize
def height(node):
  """The height of a tree would be the height of its root node, 
  or equivalently, the depth of its deepest node."""

  if node:
    heightL = height(node.left)
    heightR = height(node.right)
    return (heightR+1, heightL+1)[heightL > heightR]
  else: return -1

# Depth First Traversals

def inorder(node):
  if node:
    inorder(node.left)
    print(node.value, end=" ")
    inorder(node.right)

def preorder(node):
  if node:
    print(root.value, end=" ")
    preorder(root.left)
    preorder(root.right)

def postorder(node):
  if node:
    postorder(root.left)
    postorder(root.right)
    print(root.value, end=" ")

def leafcount(node):
  if node:
    if not node.left and not node.right:
      return 1
    return leafcount(node.left) + leafcount(node.right)
  else: return 0

def leafnodes(node):
  if node:
    if not node.left and not node.right:
      return [node.value]
    return leafnodes(node.left) + leafnodes(node.right)
  else: return []

def max_node(node):
  if node:
    maxL = max_node(node.left)
    maxR = max_node(node.right)
    large = (maxL, maxR)[maxR > maxL]
    return (node.value, large)[ large > node.value]
  else: return MIN_VALUE
  
def max_leaf_node(node):
  if node:
    if not node.left and not node.right:
      return node.value
    maxleafL = max_leaf_node(node.left)
    maxleafR = max_leaf_node(node.right)
    return (maxleafR, maxleafL)[maxleafL > maxleafR]
  else: return MIN_VALUE

def LCAncestor(node, n1, n2):
  if node:
    if node.value == n1 or node.value == n2:
      return node
    nodeL = LCAncestor(node.left, n1, n2)
    nodeR = LCAncestor(node.right, n1, n2)
    if nodeL and nodeR:
      return node
    return LCAncestor(node.left, n1, n2) if nodeL else LCAncestor(node.right, n1, n2)
  else: return None

root = binarytree.tree(height=3, is_perfect=False)
print(root)
print("height:", height(root), end="\n")
inorder(root)
print("\nNumber of leaf nodes:", leafcount(root))
print(max_node(root))
print(max_leaf_node(root))
leaf_nodes = leafnodes(root)
print(leaf_nodes)
k = list(map(int, input("give two node value: ").strip().split()))
print(LCAncestor(root, k[0], k[-1]))
