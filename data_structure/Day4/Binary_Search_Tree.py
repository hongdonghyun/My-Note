from Day4.Binary_Tree import BinaryTree

"""
Binary Search Tree

전위 순회                    중위 순회               후위 순회
부모 -> 왼쪽 -> 오른쪽    왼쪽 -> 부모 -> 오른쪽  왼쪽 -> 오른쪽 -> 부모
     1                       4                     7
   /  \                    /  \                  /  \
  2    5                  2    6                3    6
 / \  / \                / \  / \              / \  / \
3   4 6  7              1   3 5  7            1   2 4  5
"""


class BinarySearchTree(BinaryTree):
    # 삽입
    def insert(self, data):
        # 삽입할 노드 생성 및 데이터 설정
        new_node = self.make_node()
        self.set_node_data(new_node, data)

        cur = self.get_root()

        # 예외 처리 root_node가 없을때
        if not cur:
            self.set_root(new_node)
            return

        # 위치 찾기
        while True:
            # 삽입할 데이터가 현재 노드 데이터보다 작을 때
            if data < self.get_node_data(cur):
                # 왼쪽 자식 노드가 존재 한다면
                if self.get_left_sub_tree(cur):
                    # cur변수에 왼쪽값을 넣는다
                    cur = self.get_left_sub_tree(cur)
                # 존재 하지 않는다면 노드 삽입
                else:
                    self.make_left_sub_tree(cur, new_node)
                    break
            # 삽입할 데이터가 현재 노트 데이터보다 클 때
            else:
                # 오른쪽 자식 노드가 존재 한다면
                if self.get_right_sub_tree(cur):
                    # cur변수에 오른쪽값을 넣는다
                    cur = self.get_right_sub_tree(cur)
                # 존재 하지 않는다면 노드 삽입
                else:
                    # new_node값을 넣는다
                    self.make_right_sub_tree(cur, new_node)
                    break

    # 찾기
    def search(self, target):
        cur = self.get_root()
        # 루트가 None아니라면
        while cur is not None:
            # 타겟 데이터를 찾으면 노드를 반환
            if target == self.get_node_data(cur):
                return cur
            # 타겟 데이터가 노드 데이터보다 작다면
            elif target < self.get_node_data(cur):
                cur = self.get_left_sub_tree(cur)
            # 타겟이 현재값보다 크다면
            else:
                cur = self.get_right_sub_tree(cur)
        return cur

    # 삭제
    def remove(self, target):
        del_parent = self.get_root()
        del_node = self.get_root()

        while True:
            # 찾는 데이터가 없을 경우
            if del_node is None:
                return None
            # 타겟이 지우려는 값과 같다면
            if target == self.get_node_data(del_node):
                break
            # 타겟이 작다면 왼쪽으로 탐색
            elif target < self.get_node_data(del_node):
                del_parent = del_node
                del_node = self.get_left_sub_tree(del_node)
            # 타겟이 크다면 오른쪽으로 탐색
            else:
                del_parent = del_node
                del_node = self.get_right_sub_tree(del_node)
        # 단말 노드일 경우
        if self.get_left_sub_tree(del_node) is None and self.get_right_sub_tree(del_node) is None:
            return self.remove_leaf(del_parent, del_node)

        # 자식노드가 하나일 경우
        elif self.get_left_sub_tree(del_node) is None or self.get_right_sub_tree(del_node) is None:
            return self.remove_one_child(del_parent, del_node)

        # 자식노드가 두개일 경우
        else:
            return self.remove_two_children(del_node)

    # def remove_left_sub_tree(self, cur):
    #     del_node = self.get_left_sub_tree(cur)
    #     self.make_left_sub_tree(cur, None)
    #     return del_node

    # def remove_right_sub_tree(self, cur):
    #     del_node = self.get_right_sub_tree(cur)
    #     self.make_right_sub_tree(cur, None)
    #     return del_node

    # 삭제할 노드가 단말노드일때
    def remove_leaf(self, parent, del_node):

        # 루트 노드 지울 때
        if del_node == self.get_root():
            self.set_root(None)
            return del_node

        # 왼쪽
        if self.get_left_sub_tree(parent) == del_node:
            self.make_left_sub_tree(parent, None)
        # 오른쪽
        else:
            self.make_left_sub_tree(parent, None)

        return del_node

    # 자식노드가 하나일때
    def remove_one_child(self, parent, del_node):
        # 삭제 노드가 루트 노드 일 때
        if del_node == self.get_root():
            if self.get_left_sub_tree(del_node):
                self.set_root(self.get_left_sub_tree(del_node))
            else:
                self.set_root(self.get_right_sub_tree(del_node))
            return del_node

        del_child = None
        # 왼쪽 트리가 있다면
        # 삭제한 노드의 자식노드를 받아온다
        if self.get_left_sub_tree(del_node):
            del_child = self.get_left_sub_tree(del_node)
        # 오른쪽 트리가 있다면
        # 삭제한 노드의 자식노드를 받아온다
        else:
            del_child = self.get_right_sub_tree(del_node)

        # 삭제노드의 부모 노드에 연결
        if self.get_left_sub_tree(parent) == del_node:
            self.make_left_sub_tree(parent, del_child)
        else:
            self.make_right_sub_tree(parent, del_child)

        return del_node

    # 자식노드가 두개일때
    def remove_two_children(self, del_node):
        # 값을 바꾸는 방식이라
        # 루트노드를 실제 삭제하는게 아님
        # 루트노드 삭제에 대한 예외처리가 필요 없음
        rep_parent = del_node
        # 삭제 노드의 왼쪽 서브 트리
        replace = self.get_left_sub_tree(rep_parent)

        # 가장 큰 데이터를 가진 노드를 찾음
        while self.get_right_sub_tree(replace):
            rep_parent = replace
            replace = self.get_right_sub_tree(replace)
        temp_data = self.get_node_data(replace)
        self.set_node_data(replace, self.get_node_data(del_node))
        self.set_node_data(del_node, temp_data)

        # 대체 노드 왼쪽에 서브트리가 있는 경우
        if self.get_left_sub_tree(rep_parent) == replace:
            self.make_left_sub_tree(rep_parent, self.get_left_sub_tree(replace))

        else:
            self.make_right_sub_tree(rep_parent, self.get_left_sub_tree(replace))
        return replace


q = BinarySearchTree()
q.insert(6)
q.insert(3)
q.insert(2)
q.insert(4)
q.insert(5)
q.insert(8)
q.insert(10)
q.insert(9)
q.insert(11)

f = lambda x: print(x, end=' ')

q.preorder_traverse(q.get_root(), f)
print("")

# q.remove(9) # 리프 노드일 때
# q.remove(8)  # 자식노드가 하나 일 때
q.remove(6)  # 자식노드가 두개 일 때
q.preorder_traverse(q.get_root(), f)
print("")
