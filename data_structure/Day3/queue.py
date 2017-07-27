"""
1. enqueue(data) -> None 맨 뒤에 추가
2. dequeue() -> data 맨 앞에 데이터 삭제 (삭제 된 데이터 반환)
3. empty() -> bool
4. peek() -> data 삭제 x 맨앞 데이터 반환
"""


class Queue(list):
    enqueue = list.append

    def dequeue(self):
        return self.pop(0)

    def empty(self):
        if not self:
            return True
        else:
            return False

    def peek(self):
        return self[0]


q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)

while not q.empty():
    data = q.dequeue()
    print(data, end=' ')

