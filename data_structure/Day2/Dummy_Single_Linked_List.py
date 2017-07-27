import sys


class Node:
    # 노드 생성
    def __init__(self, data):
        self.data = data
        self.next = None

    # 노드 삭제
    def __del__(self):
        print("data of {} is deleted".format(self.data))


class Linked_list:
    def __init__(self):
        # 노드의 시작
        self.head = None
        # 노드의 끝
        self.tail = None

        # 현재 위치의 이전 값
        self.before = None
        # 현재 위치의 값
        self.current = None
        # 데이터 개수???
        self.num_data = 0

    def empty(self):
        if self.num_data == 0:
            return True
        else:
            return False

    def size(self):
        return self.num_data

    # insert
    def append(self, data):
        new_node = Node(data)
        if self.empty():
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.num_data += 1

    def traverse(self, mode='next'):
        # self.empty가 밖에서 실행 해도 되지만,
        # first안에 있으면 first일경우에만 실행
        if self.empty():
            return None

        if mode == 'first':
            self.before = self.head
            self.current = self.head
        else:  # mode =='next'
            # if self.current == self.tail:
            if self.current.next is None:
                return None
            self.before = self.current
            self.current = self.current.next

        return self.current.data

    def remove(self):
        ret_data = self.current.data

        # 데이터가 1개일때
        if self.size() == 1:
            self.head = None
            self.tail = None
            self.current = None
            self.before = None
            # 전부 None을 바라보게하면 된다

        # current가 head랑 같을 때
        elif self.current is self.head:
            self.head = self.head.next
            self.before = self.before.next
            self.current = self.current.next

        else:
            # current 가 tail이랑 같을 때
            if self.current is self.tail:
                self.tail = self.before
            # 일반적
            self.before.next = self.current.next
            self.current = self.before

        self.num_data -= 1
        return ret_data


def show_list(_list):
    data = _list.traverse('first')
    # 데이터가 있다면
    if data:
        print(data, end=' ')
        # traverse default is next
        data = _list.traverse()
        while data:
            print(data, end='')
            data = _list.traverse()

    else:
        print('There is no data')


dummy = Linked_list()

dummy.append(1)
dummy.append(2)
dummy.append(3)
dummy.append(4)

show_list(dummy)
print('\n')

data = dummy.traverse('first')
while data:
    if data == 1:
        dummy.remove()
    data = dummy.traverse()

show_list(dummy)
print('\n')
