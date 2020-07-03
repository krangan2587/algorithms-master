# Another approach to memoization using dictionaries in python
class Fibonacci:
    def __init__(self):
        self.memo = {}

    def fib(self,n):
        if n < 0:
            raise ValueError("No Negative numbers")
        if n == 0 or n == 1:
            return n
        if n in self.memo.keys():
            return self.memo.get(n)
        print("computing fib(%i)" % n)
        result = self.fib(n - 1) + self.fib(n - 2)
        self.memo[n] = result
        return result

if __name__ == '__main__':
    number = int(input("Please enter a number "))
    f = Fibonacci()
    print(f.fib(number))