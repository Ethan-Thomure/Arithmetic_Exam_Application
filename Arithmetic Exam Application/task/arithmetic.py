class Arithmetic:

    def __init__(self, expression):
        # initializer accepts string and then converts it into its fundamental parts
        x, self.operator, y = expression.split()
        self.first_operand, self.second_operand = [int(x), int(y)]

    def evaluation(self):
        calculation = {"+": lambda x, y: x + y, "-": lambda x, y: x - y, "*": lambda x, y: x * y}
        return calculation[self.operator](self.first_operand, self.second_operand)


exam = Arithmetic(input())
print(exam.evaluation())
