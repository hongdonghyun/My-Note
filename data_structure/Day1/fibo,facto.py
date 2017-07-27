# def fibo(n):
#     if n <= 1:
#         return 1
#
#     return fibo(n - 2) + fibo(n - 1)
#
#
# for i in range(5):
#     print(fibo(i), end=' ')
#
#
# def fac(n):
#     if n <= 1:
#         return 1
#     return n * fac(n - 1)
#
#
# def fibo_gen(n):
#     a = b = 1
#
#     for i in range(n):
#         yield a
#         a, b = b, a + b
#
#
# if __name__ == "__main__":
#     f = fibo_gen(10)
#     for i in range(10):
#         print(next(f), end=' ')