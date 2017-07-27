def linear_search(data, target):
    for i in range(len(data)):
        if data[i] == target:
            return i
    return None


data = [i for i in range(10)]

target = 4
i = linear_search(data, target)

if i == None:
    print('{} 이 존재 하지 않습니다'.format(target))
else:
    print("index {} data {}".format(i, data[i]))
