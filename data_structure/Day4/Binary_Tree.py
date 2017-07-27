"""
Binary Tree : 자식 노드가 최대 2개

lev0               root node
                /            \ edge
lev1        internal node  internal node
             /\                 /\
lev2      leaf node           leaf node

완전 이진 트리 : 위 -> 아래,왼쪽 -> 오른쪽

전위 순회                    중위 순회               후위 순회
부모 -> 왼쪽 -> 오른쪽    왼쪽 -> 부모 -> 오른쪽  왼쪽 -> 오른쪽 -> 부모
     1                       4                     7
   /   \                   /  \                  /  \
  2    5                  2    6                3    6
 / \  / \                / \  / \              / \  / \
3  4 6  7               1  3 5  7             1  2 4  5
"""


class TreeNode:
    def __init__(self):
        self._data = None
        self.left = None
        self.right = None

    def __del__(self):
        print('TreeNode of {} is deleted'.format(self.data))

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, data):
        self._data = data


# 이진트리를 구성하는 모든 기능들을 클래스화
class BinaryTree:
    def __init__(self):
        self.root = None

    def get_root(self):
        return self.root

    def set_root(self, r):
        self.root = r

    def make_node(self):
        new_node = TreeNode()
        return new_node

    def get_node_data(self, cur):
        return cur.data

    def set_node_data(self, cur, data):
        cur.data = data

    def get_left_sub_tree(self, cur):
        return cur.left

    def get_right_sub_tree(self, cur):
        return cur.right

    def make_left_sub_tree(self, cur, left):
        cur.left = left

    def make_right_sub_tree(self, cur, right):
        cur.right = right

    # 전위 순회
    def preorder_traverse(self, cur, func):
        if cur is None:
            return
        func(cur.data)
        self.preorder_traverse(cur.left, func)
        self.preorder_traverse(cur.right, func)

    # 중위 순회
    def inorder_traverse(self, cur, func):
        if not cur:
            return
        self.inorder_traverse(cur.left, func)
        func(cur.data)
        self.inorder_traverse(cur.right, func)

    # 후위 순회
    def postorder_traverse(self, cur, func):
        if not cur:
            return
        self.postorder_traverse(cur.left, func)
        self.postorder_traverse(cur.right, func)
        func(cur.data)


if __name__ == "__main__":
    f = lambda x: print(x, end=' ')
    bt = BinaryTree()

    n1 = bt.make_node()
    bt.set_node_data(n1, 1)

    n2 = bt.make_node()
    bt.set_node_data(n2, 2)

    n3 = bt.make_node()
    bt.set_node_data(n3, 3)

    n4 = bt.make_node()
    bt.set_node_data(n4, 4)

    n5 = bt.make_node()
    bt.set_node_data(n5, 5)

    n6 = bt.make_node()
    bt.set_node_data(n6, 6)

    n7 = bt.make_node()
    bt.set_node_data(n7, 7)

    bt.set_root(n1)
    bt.make_left_sub_tree(n1, n2)
    bt.make_right_sub_tree(n1, n3)

    bt.make_left_sub_tree(n2, n4)
    bt.make_right_sub_tree(n2, n5)

    bt.make_left_sub_tree(n3, n6)
    bt.make_right_sub_tree(n3, n7)

    bt.preorder_traverse(bt.get_root(), f)
    print("")
    bt.inorder_traverse(bt.get_root(), f)
    print("")
    bt.postorder_traverse(bt.get_root(), f)
    print("")

    # 특정 위치에 노드 삽입
    n8 = bt.make_node()
    bt.set_node_data(n8, 8)

    bt.make_right_sub_tree(n1, n8)
    bt.make_right_sub_tree(n8, n3)

    bt.inorder_traverse(bt.get_root(), f)
    print("")

    # 특정 위치의 노드 삭제

    bt.make_right_sub_tree(n6, n7)
    bt.make_right_sub_tree(n1, n6)
    del n3

    bt.inorder_traverse(bt.get_root(), f)
