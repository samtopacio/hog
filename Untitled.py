def make_adder(x):
    def adder(n):
        return n + x
    return adder

def square(x):
    return x*x

def success(x):
    return x + 1

def compose1(f, g):
    def h(x):
        return f(g(x))
    return h


