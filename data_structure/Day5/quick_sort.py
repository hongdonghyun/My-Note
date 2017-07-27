"""
단순 알고리즘     O(n^2)
1. bubble sort
2. insertion sort
3. selection sort

divide and conquer(분할 정복 기법)    어려운 문제를 쪼개서 해결한다
1. quick sort
2. merge sort

quick sort
"""


def quick_sort(data, start, end):  # data = list, start = start index, end = end index, target = 찾을 값
    # 재귀 탈출 조건
    if start > end:
        return

    left = start
    right = end

    pivot = data[(start + end) // 2]
    while left <= right:
        # left와 right가 교차할 때 까지
        while data[left] < pivot:
            left += 1
        while data[right] > pivot:
            right -= 1

        if left <= right:
            data[left], data[right] = data[right], data[left]
            left += 1
            right -= 1

    quick_sort(data, start, right)
    quick_sort(data, left, end)


data = [2, 3, 5, 6, 7, 9, 0, 1, 123, 443, 24543, 88, 22, 98]
quick_sort(data, 0, len(data) - 1)
print(data)
