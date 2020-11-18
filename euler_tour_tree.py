from __future__ import annotations
from typing import List


class Node:
    def __init__(self, val: int, left: Node = None, right: Node = None):
        self.val = val
        self.left = left
        self.right = right


def euler_tour_tree(node: Node) -> List[int]:
    if not node:
        return []
    res = []

    def euler_tour(n, arr):
        arr.append(n.val)
        if not n.right and not n.left:
            return
        euler_tour(n.left, arr)
        arr.append(n.val)
        euler_tour(n.right, arr)
        arr.append(n.val)
    euler_tour(node, res)

    return res


if __name__ == "__main__":
    tree = Node(1, Node(2, Node(3), Node(4)), Node(5))
    print(euler_tour_tree(tree))
