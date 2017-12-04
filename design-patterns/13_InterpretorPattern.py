class Expression(object):
    def interpret(self, text):
        pass

class TerminalExpression(Expression):
    def __init__(self, word):
        self.word = word
    
    def interpret(self, text):
        if self.word in text:
            return True
        else:
            return False

class OrExpression(Expression):
    def __init__(self, exp1, exp2):
        self.exp1 = exp1
        self.exp2 = exp2
    
    def interpret(self, text):
        return self.exp1.interpret(text) or self.exp2.interpret(text)

class AndExpression(Expression):
    def __init__(self, exp1, exp2):
        self.exp1 = exp1
        self.exp2 = exp2
    
    def interpret(self, text):
        return self.exp1.interpret(text) and self.exp2.interpret(text)

if __name__ == '__main__':
    john = TerminalExpression('John')
    henry = TerminalExpression('Henry')
    mary = TerminalExpression('Mary')
    sarah = TerminalExpression('Sarah')
    
    # And(Sarah , Or(Mary, And(John, Henry)))
    rule1 = AndExpression(john, henry)
    rule2 = OrExpression(mary, rule1)
    rule3 = AndExpression(sarah, rule2)
    
    print(rule3.interpret('Sarah'))
    print(rule3.interpret('Sarah Mary'))
    print(rule3.interpret('Sarah John'))
    print(rule3.interpret('Sarah John Henry'))