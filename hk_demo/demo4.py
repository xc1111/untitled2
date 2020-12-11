class Rice:
    def __init__(self,number,g):
        self.g=g
        self.number=number
    def __str__(self):
        return print(f"被吃第{self.number}次,吃了{self.g}")

    def eat(self, number, g):
        self.g = g
        self.number = number
        print(f"被吃第{self.number}次,吃了{self.g}")




