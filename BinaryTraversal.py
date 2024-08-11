# import queue as qu  # noqa: INP001
# class Node:
#     def __init__(self, data) -> None:
#         self.left = None
#         self.right = None
#         self.data = data
# class BinaryTree(Node):
#     def __init__(self) -> None:
#         self.root = None

#     def insert(self, root, data):
#         if root is None:
#             root = Node(data)
#         elif (data <= root.data):
#             root.left = self.insert(root.left, data)
#         elif (data > root.data):
#             root.right = self.insert(root.right, data)
#         return root
