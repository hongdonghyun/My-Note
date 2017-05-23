random_list = [5,1,3,7,2,9]


def selection(input_list):
    length = len(input_list)
    #리스트길이 -1번만큼 순회한다. 각인덱스는 index에 지정된다.
    for index in range(length-1):
        min_index=index
        # print('{}번째 loop입니다.'.format(index +1))

        #상위 루프 내부에서 다시 루프를 돌며 리스트길이 -index(상위 루프의 인덱스값)만큼 순회
        for index2 in range(index+1,length):
            # print('{}번째 loop내부의 {}번째 값 : {}'.format(index+1,index2,input_list[index2]))
            #비교를 시작한다. min_index가 가지는값과 index2가 가지는 값을 비교
            # min_index가 가지는 값이 index2가 가지는 값보다 클 때
            #뒤로가야하니까
            if input_list[min_index] >= input_list[index2]:
                min_index = index2

        input_list[index],input_list[min_index] = input_list[min_index],input_list[index]
        print(input_list)

selection(random_list)