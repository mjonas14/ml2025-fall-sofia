class NumList():
    def __init__(self):
        self.numbers = []
    
    def insert_number(self, number):
        self.numbers.append(number)
    
    def find_number(self, x):
        try:
            return self.numbers.index(x) + 1
        except ValueError:
            return -1