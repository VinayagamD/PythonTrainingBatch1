class InvalidException(Exception):

    def __init__(self, message) -> None:
        self.message = message
        super().__init__(message)


class CalculatorUtil:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def addition(self):
        return self.a + self.b

    def subtraction(self):
        return self.a - self.b

    def multiplication(self):
        return self.a * self.b

    def division_float(self):
        if self.b == 0:
            raise InvalidException("B cannot be zero")
        return self.a / self.b

    def division(self):
        if self.b == 0:
            raise InvalidException("B cannot be zero")
        return self.a // self.b

    def remainder(self):
        if self.b == 0:
            raise InvalidException("B cannot be zero")
        return self.a % self.b

