from typing import Optional
from dataclasses import dataclass


@dataclass
class Node:
    value: int
    left: Optional['Node'] = None
    right: Optional['Node'] = None
    parent: Optional['Node'] = None


class BinaryTree:
    root: Node | None
    node_cls = Node

    def __init__(self, root: int | None = None):
        self.root = None
        if root is not None:
            self.root = self.node_cls(root)

    def insert(self, value: int) -> Node:
        node = self.node_cls(value)

        if self.root is None:
            self.root = node
            return node

        current = self.root
        while True:
            if value < current.value:
                if current.left is None:
                    current.left = node
                    node.parent = current
                    break

                current = current.left
                continue

            if current.right is None:
                current.right = node
                node.parent = current
                break

            current = current.right

        return node

    def search(self, value: int) -> Node | None:
        current = self.root

        while current:
            if value < current.value:
                current = current.left
            elif value > current.value:
                current = current.right
            else:
                return current

    def remove(self, value: int):
        node = self.search(value)
        if node is None:
            return

        # 2 children
        if node.left is not None and node.right is not None:
            for_delete = node.left
            while for_delete.right is not None:
                for_delete = for_delete.right

            for_delete.value, node.value = node.value, for_delete.value
            # После смены значений for_delete содержит либо одного, либо ноль детей.
            # Используем блоки кода ниже для обработки этого случая.
            node = for_delete

        parent = node.parent
        # 0 children
        if node.left is None and node.right is None:
            if parent.left is node:
                parent.left = None
            else:
                parent.right = None

            return

        # 1 child left
        if node.right is None and node.left is not None:
            new_node = node.left
            new_node.parent = parent

            if parent.left is node:
                parent.left = new_node
            else:
                parent.right = new_node

            return

        # 1 child right
        if node.right is not None and node.left is None:
            new_node = node.right
            new_node.parent = parent

            if parent.left is node:
                parent.left = new_node
            else:
                parent.right = new_node

            return
