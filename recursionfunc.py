# def factorial(n):
#     if (n == 0 or n == 1):
#         return 1
#     else:
#         return n * factorial(n - 1)
    
# num = int(input("Enter Number for which factorial you want: "))
# fact = factorial(num)
# print(fact)


# #write a progrram to print a fibonacci sequence
# #f(0) = 0
# #f(1) = 1
# #f(2) = f(1) + f(0)
# #f(0) = f(n-1)+f(n-2)

# def fibonacci(n):
#     fib_series = [0,1]
#     while len(fib_series)<n:
#         fib_series.append(fib_series[-1] + fib_series[-2])
#     return fib_series[:n]
    
# num = int(input("Enter Number: "))
# result = fibonacci(num)
# print(result)

def fibonacci_recursive(n):
    if n <= 0:
        return []
    elif n==1:
        return [0]
    elif n==2:
        return [0,1]
    else:
        fib_series = fibonacci_recursive(n-1)
        fib_series.append(fib_series[-1] + fib_series[-2])
        return fib_series[:n]
    
num = int(input("Enter Number:"))
result = fibonacci_recursive(num)
print(result)