class Fard(Exception):
    def __init__(self, number):
        super().__init__(f"The number {number} is odd, which is not allowed.")
        self.number = number

try:
    a = int(input("Enter a number: "))
    if a % 2 != 0:
        raise Fard(a)
except Fard as e:
    print(e)
