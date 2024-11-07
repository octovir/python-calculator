class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        result = 0
        for i in range(abs(b)):
            result = self.add(result, a)
        if b < 0:
            result = -result
        return result

    def divide(self, a, b):
        
        if b == 0:
            raise ZeroDivisionError("Can't divide by zero")
        
        result = 0
        abs_a =abs(a)
        abs_b =abs(b)

        while abs_a >= abs_b:
            abs_a = self.subtract(abs_a, abs_b)
            result += 1
        if a<0:
            result = -result
        elif b<0:
            result = -result
        return result
    
    def modulo(self, a, b):
        if b == 0:
            raise ZeroDivisionError("Can't divide by zero")
        abs_a =abs(a)
        abs_b =abs(b)
        while abs_a >= abs_b:
            abs_a = self.subtract(abs_a, abs_b)
        return abs_a

# Example usage:
if __name__ == "__main__":
    calc = Calculator()
    print("This is a simple calculator class!")
    print("Example: addition: ", calc.add(1, 2))
    print("Example: subtraction: ", calc.subtract(4, 2))
    print("Example: multiplication: ", calc.multiply(-2, -3))
    print("Example: division: ", calc.divide(-20, 3))
    print("Example: modulo: ", calc.modulo(-20, 3))