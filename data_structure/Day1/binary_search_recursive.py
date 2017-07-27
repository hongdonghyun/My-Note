"""
    이진 탐색을 위해선
    탐색하기 위한 선형 데이터 자료구조는
    이미 정렬이 되어있어야 한다.
"""


def binary_search_recursive(data, start, end, target):
    """
    정렬된 데이터 구조를 사용하세요.
    """
    mid = (start + end) // 2
    if start > end:
        return None

    if target == data[mid]:
        return mid
    elif target < data[mid]:
        end = mid - 1
        return binary_search_recursive(data, start, end, target)
    else:
        # target > data[mid]
        start = mid + 1
        return binary_search_recursive(data, start, end, target)


_list = [i for i in range(11)]
target = 1
start = 0
end = len(_list)
result = binary_search_recursive(_list, start, end, target)

if result:
    print(_list[result])
else:
    print('없다')
