class Calculator:
    def __init__(self, x, y):
        self.firstnumber = x
        self.Secondnumber = y

    def divide(self):
        return self.firstnumber / self.Secondnumber

    def add(self):
        return self.firstnumber + self.Secondnumber

    def sub(self):
        return self.firstnumber - self.Secondnumber

    def multiply(self):
        return self.firstnumber * self.Secondnumber



def main():
    x = 10
    y = 20
    calci = Calculator(x, y)
    print(calci.multiply())


if __name__ == '__main__':
    main()