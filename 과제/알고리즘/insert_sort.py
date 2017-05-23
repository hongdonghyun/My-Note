import random

from tornado.util import xrange

random_list = random.sample(xrange(200),20)

def insert_sort(input_list):
    length = len(input_list)
    for index in range(1,length):
        key =input_list[index]
        i = index - 1
        while i>=0:
            if key < input_list[i]: # i번째 칸에 있던 수를 i+1번째칸으로 옮긴다 오른쪽
                input_list[i+1] = input_list[i]
                input_list[i] = key # 키값은 왼쪽의 i 번째 칸으로 옮긴다.
                i = i-1
            else:
                break



print('= 정렬 전 리스트 =\n {}'.format(random_list))
random_list = insert_sort(random_list)
print('= 정렬 후 리스트 =\n {}'.format(random_list))