iterations = int(input("Input a number of iterations: "))

#recursive
def recursive_fib(n):
    if n < 2:
        return n
    else:
        return recursive_fib(n-1) + recursive_fib(n-2)

#iterative
def iterative_fib(n):
    a = 0
    b = 1

    if a == 0:
        return a
    else:
        for k in range(n):
            c = a + b
            a = b
            b = c
        return b

print("\n****RECURSIVE****")
for num in range(iterations):
    print(recursive_fib(num))

print("\n****ITERATIVE****")
for num in range(iterations):
    print(iterative_fib(num))


