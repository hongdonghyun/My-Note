# num은 원반의 개수 _from 시작기둥 , _by 중간기둥 ,_to 최종기둥
# def hanoi(num, _from, _by, _to):
#     if num == 1:
#         print('이동 {}에서 {}로 {}번째 원반을 이동'.format(_from, _to, num))
#
#         return
#     hanoi(num - 1, _from, _to, _by)
#     print('이동 {}에서 {}로 {}번째 원반을 이동'.format(_from, _to, num))
#     hanoi(num - 1, _by, _from, _to)
#
#
# while(1):
#     _input = int(input("원반의 개수를 입력하세요 "))
#     if _input == 0:
#         break
#     hanoi(_input,'a','b','c')
