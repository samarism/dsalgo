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
    res1 = []

    def euler_tour_node_val(n, arr):
        arr.append(n.val)
        if not n.right and not n.left:
            return
        if n.left:
            euler_tour_node_val(n.left, arr)
            arr.append(n.val)
        if n.right:
            euler_tour_node_val(n.right, arr)
            arr.append(n.val)

    def euler_tour_depth(n, arr, level):
        arr.append(level)
        if not n.right and not n.left:
            return
        if n.left:
            euler_tour_depth(n.left, arr, level+1)
            arr.append(level)
        if n.right:
            euler_tour_depth(n.right, arr, level+1)
            arr.append(level)

    euler_tour_node_val(node, res1)
    res2 = []
    euler_tour_depth(node, res2, 0)

    return [res1, res2]


if __name__ == "__main__":
    tree = Node(1, Node(2, Node(3), Node(4)))
    assert euler_tour_tree(tree) == [[1, 2, 3, 2, 4, 2, 1], [0, 1, 2, 1, 2, 1, 0]]
    print(euler_tour_tree(tree))



