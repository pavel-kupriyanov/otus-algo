from typing import Optional


class BalancedNode:
    value: int
    height: int = 1
    left: Optional['BalancedNode'] = None
    right: Optional['BalancedNode'] = None

    def __repr__(self):
        return f'Node {self.value}:' \
               f' left: {self.left.value if self.left else "None"}:' \
               f' right: {self.right.value if self.right else "None"}:'

    def __init__(self, value: int):
        self.value = value

    @property
    def balance(self) -> int:
        left_height = self.left.height if self.left else 0
        right_height = self.right.height if self.right else 0

        return right_height - left_height

    def set_height(self):
        left_height = self.left.height if self.left else 0
        right_height = self.right.height if self.right else 0

        self.height = max(left_height, right_height) + 1


class BalancedTree:
    root: BalancedNode = None

    def rotate_left(self, node: BalancedNode) -> BalancedNode:
        right = node.right
        node.right = right.left
        right.left = node

        node.set_height()
        right.set_height()

        if node is self.root:
            self.root = right

        return right

    def rotate_right(self, node: BalancedNode) -> BalancedNode:
        left = node.left
        node.left = left.right
        left.right = node

        node.set_height()
        left.set_height()

        if node is self.root:
            self.root = left

        return left

    def insert(self, value: int) -> BalancedNode:
        if self.root is None:
            self.root = self._insert(value)
            return self.root

        return self._insert(value, self.root)

    def remove(self, value: int) -> BalancedNode:
        return self._remove(value, self.root)

    def search(self, value: int) -> BalancedNode:
        return self._search(value, self.root)

    def balance(self, node: BalancedNode) -> BalancedNode:
        node.set_height()

        if node.balance == 2:
            if node.right and node.right.balance < 0:
                node.right = self.rotate_right(node.right)
            return self.rotate_left(node)

        if node.balance == -2:
            if node.left and node.left.balance > 0:
                node.left = self.rotate_left(node.left)
            return self.rotate_right(node)

        return node

    def _search(self, value: int, node: BalancedNode = None) -> Optional[BalancedNode]:
        if node is None:
            return None

        if value == node.value:
            return node

        if value < node.value:
            return self._search(value, node.left)
        else:
            return self._search(value, node.right)

    def _insert(self, value: int, target: BalancedNode = None) -> BalancedNode:
        if target is None:
            return BalancedNode(value)

        if value < target.value:
            target.left = self._insert(value, target.left)
        else:
            target.right = self._insert(value, target.right)

        return self.balance(target)

    def _remove(self, value: int, node: BalancedNode = None) -> Optional[BalancedNode]:
        if node is None:
            return None

        if value < node.value:
            node.left = self._remove(value, node.left)
        elif value > node.value:
            node.right = self._remove(value, node.right)
        else:
            left = node.left
            right = node.right
            if right is None:
                return left

            min_node = self._min(right)
            min_node.right = self._remove_min(right)
            min_node.left = left

            return self.balance(min_node)

        return self.balance(node)

    def _min(self, node: BalancedNode) -> BalancedNode:
        return self._min(node.left) if node.left else node

    def _remove_min(self, node: BalancedNode) -> BalancedNode:
        if node.left is None:
            return node.right

        node.left = self._remove_min(node.left)
        return self.balance(node)
