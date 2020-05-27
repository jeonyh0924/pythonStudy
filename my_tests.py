import unittest


class Stack:
    EMPTY_POP = -1

    def __init__(self):
        self.s = []

    def push(self, val):
        self.s.append(val)

    def pop(self):
        if not self.s:
            return -1
        val = self.s.pop()
        return val

    def size(self):
        return len(self.s)

    def empty(self):
        if not self.s:
            # 비어있다면 1 리턴
            return self.EMPTY_POP
        # 비어있지 않다면 0 리턴
        return 0

    def top(self):
        if not self.s:
            # 스택에 들어있는 정수가 없다면 -1 출력
            return self.EMPTY_POP
        # 가장 위 정수 출력
        return self.s[-1]


class StackTestCase(unittest.TestCase):
    def setUp(self):
        # 테스트 코드 클래스에서 Stack의 인스턴스 생성.
        # 테스트 코드의 인스턴스를 생성 후 setUp()함수 호출 시 Stack클래스에 접근한다.
        self.stack = Stack()

    def test_pop(self):
        # assertEqual // 첫번째 인자와 두번째 인자의 값이 같지 않다면 assert Errror
        self.assertEqual(self.stack.pop(), -1)

    def test_pop_with_data(self):
        val = 10
        self.stack.push(val)
        self.assertEqual(self.stack.pop(), val)

    def test_empty(self):
        # 스택이 비어 있다면, 1 리턴
        self.assertEqual(self.stack.empty(), -1)

    def test_empty_with_data(self):
        val = 10
        self.stack.push(10)
        self.assertEqual(self.stack.empty(), 0)

    # top: 스택의 가장 위에 있는 정수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
    #     def
    # size : 스택에 들어있는 정수의 개수를 출력한다
