class DecoratorClass(object):
    def __init__(self, a_func):
        self.a_func = a_func

    def __call__(self):
        self.a_func()
        

def main():
    decorator = DecoratorClass(a_func)
    print("Test", decorator.a_func())

def a_func():
    print("Test Decorator")

if __name__ == "__main__":
    main()