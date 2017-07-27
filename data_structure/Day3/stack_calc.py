from Day3.stack import Stack


class Calculator:
    def __init__(self):
        # 중위 표기법 수식을 받는 변수
        self.org_exp = None
        # 후위 표기법 수식을 받는 변수
        self.postfix_exp = None
        self.result = None

    def set_org_exp(self, org_exp):
        # 스페이스를 빈값으로 대치
        self.org_exp = org_exp.replace(' ', '')
        self.postfix_exp = None
        self.result = None

    def get_org_exp(self):
        return self.org_exp

    # 가중치
    def get_weight(self, oprt):
        if oprt == "*" or oprt == '/':
            return 9
        elif oprt == '+' or oprt == '-':
            return 7
        elif oprt == '(':
            return 5
        # 에러처리
        else:
            return -1

    # 계산하는 함수
    def convert_to_postfix(self):
        exp_list = []
        oprt_stack = Stack()

        # 중위 연산수식의 끝까지
        for ch in self.get_org_exp():
            # 숫자라면?
            if ch.isdigit():
                exp_list.append(ch)
            else:
                # 스택이 비어있거나 ch가 '('라면?
                if oprt_stack.empty() or ch == '(':
                    oprt_stack.push(ch)
                # )
                elif ch == ')':
                    op = oprt_stack.pop()
                    while op != '(':
                        exp_list.append(op)
                        op = oprt_stack.pop()

                # +, -, *, /
                elif self.get_weight(ch) > self.get_weight(oprt_stack.peek()):
                    oprt_stack.push(ch)
                else:
                    while oprt_stack and self.get_weight(ch) <= self.get_weight(oprt_stack.peek()):
                        exp_list.append(oprt_stack.pop())
                    oprt_stack.push(ch)

        # 아직 남아있다면
        while oprt_stack:
            exp_list.append(oprt_stack.pop())

        self.postfix_exp = ''.join(exp_list)

    def get_postfix_exp(self):
        # 아직 전환이 되지 않은 상태라면
        if not self.postfix_exp:
            # convert함수를 사용해서 바꾼다.
            self.convert_to_postfix()

        return self.postfix_exp

    def calc_two_oprd(self, oprd1, oprd2, oprt):
        if oprt == '+':
            return oprd1 + oprd2
        elif oprt == '-':
            return oprd1 - oprd2
        elif oprt == '*':
            return oprd1 * oprd2
        elif oprt == '/':
            return oprd1 // oprd2

    def calculate(self):
        oprd_stack = Stack()

        for ch in self.get_postfix_exp():
            if ch.isdigit():  # 숫자일 경우
                oprd_stack.push(int(ch))
            else:  # 연산자일 경우
                oprd2 = oprd_stack.pop()
                oprd1 = oprd_stack.pop()
                oprd_stack.push(
                    self.calc_two_oprd(
                        oprd1,
                        oprd2,
                        ch
                    )
                )
        self.result = oprd_stack.pop()

    def get_result(self):
        if not self.result:
            self.calculate()
        return self.result


# if __name__ == "__main__":

calc = Calculator()
while 1:
    exp = input('수식을 입력하세요(종료 0) :')
    if exp == '0':
        break

    calc.set_org_exp(exp)
    print(calc.get_postfix_exp())
    print('{exp} = {result}'.format(
        exp=calc.get_org_exp(),
        result=calc.get_result()
    ))
