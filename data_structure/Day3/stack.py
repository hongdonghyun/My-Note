"""
1. push(data) -> 삽입
2. pop() -> 맨위 데이터를 출력하고 삭제
3. empty() -> bool
4. peek() -> 데이터 확인
"""

__all__ = (
    'Stack',
)

class Stack(list):
    push = list.append  # push

    def empty(self):
        if not self:
            return True
        else:
            return False

    def peek(self):
        return self[-1]


# if __name__ == "__main__":
#
#     s = Stack()
#     s.push(1)
#     s.push(2)
#     s.push(3)
#     s.push(4)
#
#     while not s.empty():
#         data = s.pop()
#         print(data,end=' ')
