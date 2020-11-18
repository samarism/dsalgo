from __future__ import annotations
from typing import List


class Node:
    def __init__(self, val, left: Node = None, right: Node = None):
        self.val = val
        self.left = left
        self.right = right


def createCartesianTree(arr: List[int]) -> Node:
    if not arr:
        return None
    stack: List[Node] = [Node(arr[0])]
    i: int = 1
    while i < len(arr):
        node = Node(arr[i])
        if arr[i] > stack[-1].val:
            stack[-1].right = node
            stack.append(node)
        else:
            while stack and stack[-1].val > arr[i]:
                popped = stack.pop()
            node.left = popped
            if stack:
                stack[-1].right = node
            stack.append(node)
        i += 1

    return stack[0]


def print_tree_indented(tree, level=0):
    if not tree: return
    print_tree_indented(tree.right, level+1)
    print('  ' * level + str(tree.val))
    print_tree_indented(tree.left, level+1)


if __name__ == "__main__":
    arr = [2, 4, 1, 10, 3, 5, 7, 15]
    print_tree_indented(createCartesianTree(arr))

