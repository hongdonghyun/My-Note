import random

random_list = [random.randint(1, 100) for i in range(20)]

print('== 버블 정렬 전 리스트 ==\n {}'.format(random_list))


def bubble_sort(input_list):
    length = len(input_list) - 1

    for index in range(length):
        for index2 in range(length - index):
            if input_list[index2] > input_list[index2 + 1]:
                input_list[index2], input_list[index2 + 1] = input_list[index2 + 1], input_list[index2]
    return input_list


print('== 버블 정렬 후 리스트 ==\n ')
print(bubble_sort(random_list))
